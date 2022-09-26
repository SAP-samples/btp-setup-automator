import libs.python.helperArgParser as helperArgParser
from libs.python.helperFolders import FOLDER_SCHEMA_LIBS
from libs.python.helperJson import addKeyValuePair, dictToString, convertStringToJson, getJsonFromFile
from libs.python.helperBtpTrust import runTrustFlow
from libs.python.helperCommandExecution import executeCommandsFromUsecaseFile, runShellCommand, runCommandAndGetJsonResult, runShellCommandFlex, login_btp, login_cf
from libs.python.helperEnvCF import checkIfCFEnvironmentAlreadyExists, checkIfCFSpaceAlreadyExists, try_until_cf_space_done, try_until_space_quota_created
from libs.python.helperServiceInstances import createServiceKey, deleteServiceInstance, deleteServiceKeysAndWait, getServiceDeletionStatus, initiateCreationOfServiceInstances, checkIfAllServiceInstancesCreated
from libs.python.helperGeneric import buildUrltoSubaccount, getNamingPatternForServiceSuffix, createSubaccountName, createSubdomainID, createOrgName, save_collected_metadata
from libs.python.helperFileAccess import writeKubeConfigFileToDefaultDir
from libs.python.helperEnvKyma import extractKymaDashboardUrlFromEnvironmentDataEntry, getKymaEnvironmentInfoByClusterName, getKymaEnvironmentStatusFromEnvironmentDataEntry, extractKymaKubeConfigUrlFromEnvironmentDataEntry, getKymaEnvironmentIdByClusterName
from libs.python.helperApiTest import APITest
import os
import sys
import time
import requests
import json
from libs.python.helperRolesAndUsers import assignUsersToEnvironments, assignUsersToGlobalAndSubaccount, getSubaccountAdmins, assignUsersToRoleCollectionsForServices, assignUsersToCustomRoleCollections

from libs.python.helperServices import BTPSERVICE, BTPSERVICEEncoder, getServiceParameterDefinition, readAllServicesFromUsecaseFile
from libs.python.helperLog import initLogger
import logging

log = logging.getLogger(__name__)


class BTPUSECASE:
    def __init__(self):
        myArgs = helperArgParser.setupParamsBtpsa()
        # Take args and add them to self
        for arg in vars(myArgs):
            value = getattr(myArgs, arg)
            setattr(self, arg, value)

        initLogger(self)

        log.header("BTP-SETUP-AUTOMATOR")
        log.info("Git version >" +
                 os.getenv('BTPSA_VERSION_GIT', "not set") + "<")

        # If no suffix for service names was provided, create one (with getNamingPatternForServiceSuffix())
        if self.suffixinstancename is None or self.suffixinstancename == "":
            self.suffixinstancename = getNamingPatternForServiceSuffix(self)

        self.timeScriptStarted = time.time()

        self = helperArgParser.checkProvidedArguments(self)

        self.outputCurrentBtpUsecaseVariables()

        self.timeLastCliLogin = None
        self.definedAppSubscriptions = None
        self.definedServices = None
        self.accountMetadata = None

        allServices = readAllServicesFromUsecaseFile(self)
        self.availableCategoriesService = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"]
        self.availableCategoriesApplication = ["APPLICATION", "QUOTA_BASED_APPLICATION"]
        self.enableAPITest = getServiceTestStatusFromUsecaseFile(self.usecasefile)
        self.definedServices = getServiceCategoryItemsFromUsecaseFile(
            self, allServices, self.availableCategoriesService)
        self.definedEnvironments = getEnvironmentsForUsecase(self, allServices)
        self.definedAppSubscriptions = getServiceCategoryItemsFromUsecaseFile(
            self, allServices, self.availableCategoriesApplication)
        usecaseFileContent = getJsonFromFile(self.usecasefile)
        self.definedRoleCollections = usecaseFileContent.get(
            "assignrolecollections")

        ##############################################################################################
        # From here on, we have all the data together that we need to move ahead
        ##############################################################################################

        login_btp(self)
        self.accountMetadata = get_globalaccount_details(self)
        self.accountMetadata = addKeyValuePair(
            self.accountMetadata, "myemail", self.myemail)
        save_collected_metadata(self)
        checkConfigurationInfo(self)
        self.__api_test = APITest()

    def outputCurrentBtpUsecaseVariables(self):
        # First detect the maximum string length of the parameter and values
        maxLenParameter = 0
        for arg in vars(self):
            myLenParameter = len(arg)
            if myLenParameter > maxLenParameter:
                maxLenParameter = myLenParameter

        for arg in vars(self):
            blanks = " " * (maxLenParameter - len(arg))
            value = str(getattr(self, arg))
            message = str(arg) + blanks + " : " + value
            # Only print out the parameters if it's not the password, and if the parameter is not None
            if arg != "log" and "password" not in arg and value != "None":
                log.info(message)

    def check_if_account_can_cover_use_case(self):
        if self.rundefaulttests is True:
            log.header(
                "Checking if all configured services & app subscriptions are available on your global account")

            availableForAccount = getListOfAvailableServicesAndApps(self)
            availableCustomApps = getListOfAvailableCustomApps(self)
            usecaseSupportsServices = check_if_account_can_cover_use_case_for_serviceType(
                self, availableForAccount, availableCustomApps)

            if usecaseSupportsServices is False:
                log.error("USE CASE NOT SUPPORTED IN YOUR GLOBAL ACCOUNT!")
                sys.exit(os.EX_PROTOCOL)
            else:
                log.success("Use case supported in your global account!")

    def assignUsersToSubaccountAndRoles(self):
        assignUsersToGlobalAndSubaccount(self)
        assignUsersToEnvironments(self)

    def prune_subaccount(self, subaccountid):
        login_btp(self)
        command = "btp delete accounts/subaccount '" + subaccountid + \
            "' --global-account '" + self.globalaccount + "' --confirm  --force-delete"
        runShellCommand(self, command, "INFO",
                        "delete directory >" + subaccountid + "<")

    def executeBeforeAccountSetup(self):
        message = "Execute commands before account is prepared"
        jsonSection = "executeBeforeAccountSetup"
        executeCommandsFromUsecaseFile(self, message, jsonSection)

    def executeAfterAccountSetup(self):
        message = "Execute commands after account is setup and prepared"
        jsonSection = "executeAfterAccountSetup"
        executeCommandsFromUsecaseFile(self, message, jsonSection)

    def executeAfterEnvironmentAvailability(self):
        for environment in self.definedEnvironments:
            if environment.name == "kymaruntime" and self.waitForKymaEnvironmentCreation is True:

                accountMetadata = self.accountMetadata
                kymaClusterName = environment.parameters["name"]

                current_time = 0
                number_of_tries = 0
                timeoutInSeconds = self.timeoutLimitForKymaCreationInMinutes * 60
                pollingIntervalInSeconds = self.pollingIntervalForKymaCreationInMinutes * 60
                message = "Check status of Kyma provisioning - be patient this could take a while"

                log.header("Fetch and Store Kubeconfig")
                # Fetch Data from SAP btp CLI for URL of Dashboard and Kubeconfig
                command = "btp --format json list accounts/environment-instance --subaccount '" + \
                    self.accountMetadata["subaccountid"] + "'"

                while timeoutInSeconds > current_time:
                    number_of_tries += 1
                    checkMessage = message + " (try " + str(number_of_tries) + \
                        " - trying again in " + \
                        str(self.pollingIntervalForKymaCreationInMinutes) + "min)"
                    result = runCommandAndGetJsonResult(
                        self, command, "INFO", checkMessage)

                    entryOfKymaEnv = getKymaEnvironmentInfoByClusterName(
                        result, kymaClusterName)

                    if getKymaEnvironmentStatusFromEnvironmentDataEntry(entryOfKymaEnv) == "OK":

                        log.info(
                            "Kyma Environment created - extracting kubeconfig URL")
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "kymaDashboardUrl", extractKymaDashboardUrlFromEnvironmentDataEntry(entryOfKymaEnv))
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "kymaKubeConfigUrl", extractKymaKubeConfigUrlFromEnvironmentDataEntry(entryOfKymaEnv))
                        save_collected_metadata(self)

                        # Download kubeconfig
                        resp = requests.get(
                            self.accountMetadata["kymaKubeConfigUrl"])

                        # Store kubeconfig in .kube folder for execution of subsequent commands
                        if resp.status_code == 200:
                            writeKubeConfigFileToDefaultDir(resp.text)
                            log.info("Kubeconfig stored locally under ~/.kube")
                            return "DONE"
                        else:
                            log.error("Could not download kubeconfig from >" +
                                      self.accountMetadata["kymaKubeConfigUrl"] + "<")
                            return "ERROR"

                    time.sleep(pollingIntervalInSeconds)
                    current_time += pollingIntervalInSeconds

    def entitle_subaccount(self):
        log.header("Entitle sub account to use services and/or app subscriptions")
        envsToEntitle = []
        for myEnv in self.definedEnvironments:
            if myEnv.name != "cloudfoundry" and myEnv.name != "sapbtp":
                envsToEntitle.append(myEnv)
        doAllEntitlements(self, envsToEntitle)

        allNonCfCupServices = []
        for service in self.definedServices:
            if service.category != "CF_CUP_SERVICE":
                allNonCfCupServices.append(service)
        doAllEntitlements(self, allNonCfCupServices)

        doAllEntitlements(self, self.definedAppSubscriptions)

    def create_subaccount(self):

        accountMetadata = self.accountMetadata
        subaccountid = self.subaccountid
        self.accountMetadata = addKeyValuePair(
            accountMetadata, "subaccountid", subaccountid)

        if "subaccountid" not in accountMetadata or accountMetadata["subaccountid"] == "" or accountMetadata["subaccountid"] is None:

            log.warning(
                "no subaccount id provided and tool will make up one for you")
            usecaseRegion = self.region

            subaccount = createSubaccountName(self)
            subdomain = createSubdomainID(self)

            log.success("using subaccount name >" + subaccount + "<")
            log.success("using subaccount domain >" + subdomain + "<")

            subaccountadmins = getSubaccountAdmins(self)
            globalAccount = self.globalaccount

            log.header("Create sub account >" + subaccount +
                       "< (if not already existing)")

            subaccountid = checkIfSubaccountAlreadyExists(self)

            if subaccountid is None:
                command = "btp --format json create accounts/subaccount \
                    --display-name '" + subaccount + "' \
                    --subdomain '" + subdomain + "' \
                    --region '" + usecaseRegion + "' \
                    --subaccount-admins '" + subaccountadmins + "'"

                message = "Create sub account >" + subaccount + "<"
                result = runCommandAndGetJsonResult(
                    self, command, "INFO", message)

                subaccountid = result["guid"]

                # Wait until the sub account has been created
                command = "btp --format json get accounts/subaccount '" + \
                    subaccountid + "' --global-account '" + globalAccount + "'"
                result = try_until_done(
                    self, command, message, "state", "OK", self.repeatstatusrequest, 100)
                if result == "ERROR":
                    log.error("Something went wrong while waiting for the subaccount >" +
                              subaccount + "< with id >" + subaccountid + "<")

                log.success("created subaccount >" + subaccount +
                            "< with id >" + subaccountid + "<")
            else:
                log.success("subaccount >" + subaccount +
                            "< already exists with id >" + subaccountid + "<")
                self.subaccountid = subaccountid

            self.accountMetadata = addKeyValuePair(
                accountMetadata, "subaccountid", subaccountid)
            self.subaccountid = subaccountid
        else:
            log.header("USING CONFIGURED SUBACCOUNT WITH ID >" +
                       self.subaccountid + "<")
            if self.subdomain and self.rundefaulttests is False:
                self.accountMetadata = addKeyValuePair(
                    accountMetadata, "subdomain", self.subdomain)
            else:
                if self.subdomain:
                    self.accountMetadata = addKeyValuePair(
                        accountMetadata, "subdomain", self.subdomain)
                else:
                    result = getDetailsAboutSubaccount(self, self.subaccountid)
                    self.accountMetadata = addKeyValuePair(
                        accountMetadata, "subdomain", result["subdomain"])

        save_collected_metadata(self)

    def initialize_environments(self):

        self.create_environments()

    def create_environments(self):

        accountMetadata = self.accountMetadata
        environments = self.definedEnvironments

        subaccountid = accountMetadata["subaccountid"]

        orgid = self.orgid

        if self.orgid is not None and self.orgid != "":
            self.accountMetadata = addKeyValuePair(
                accountMetadata, "orgid", self.orgid)

        if self.orgid is None or self.orgid == "":

            for environment in environments:

                if environment.name == "cloudfoundry":
                    orgid, org = checkIfCFEnvironmentAlreadyExists(self)

                    if org is None or orgid is None:

                        envName = environment.name
                        envPlan = environment.plan

                        log.header("Create environment >" + envName + "<")

                        org = createOrgName(self, envName)

                        accountMetadata = addKeyValuePair(
                            accountMetadata, "org", org)

                        parameters = '{\"instance_name\": \"' + org + '\"}'

                        envLandscape = selectEnvironmentLandscape(
                            self, environment)

                        if envLandscape is not None:
                            command = "btp --format json create accounts/environment-instance --subaccount '" + subaccountid + "' --environment '" + envName + \
                                "' --service '" + environment.name + "' --plan '" + envPlan + \
                                "' --parameters '" + \
                                str(parameters) + "' --landscape '" + \
                                envLandscape + "'"
                        else:
                            command = "btp --format json create accounts/environment-instance --subaccount '" + subaccountid + "' --environment '" + envName + \
                                "' --service '" + environment.name + "' --plan '" + \
                                envPlan + "' --parameters '" + \
                                str(parameters) + "'"

                        message = "Create " + envName + " environment >" + org + "<"
                        result = runCommandAndGetJsonResult(
                            self, command, "INFO", message)

                        orgid = None
                        labels = convertStringToJson(result.get("labels"))
                        if labels.get("Org ID:"):
                            orgid = labels.get("Org ID:")
                        if labels.get("Org ID"):
                            orgid = labels.get("Org ID")

                        # Wait until the org has been created
                        message = "is CF environment >" + org + "< created"
                        command = "btp --format json get accounts/environment-instance '" + \
                            result.get("id") + "' --subaccount '" + \
                            subaccountid + "'"

                        result = try_until_done(
                            self, command, message, "state", "OK", self.repeatstatusrequest, 100)
                        if result == "ERROR":
                            log.error(
                                "Something went wrong while waiting for creation of CF environment >" + org + "< with id >" + orgid + "<")

                        log.success("created CF environment >" +
                                    org + "< with id >" + orgid + "<")
                        self.orgid = orgid
                        self.org = org
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "orgid", orgid)
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "org", org)

                        save_collected_metadata(self)
                        self.create_new_cf_space(environment)
                        self.create_and_assign_quota_plan(environment)

                    else:
                        log.success("CF environment >" + org +
                                    "< already available with id >" + orgid + "<")
                        self.orgid = orgid
                        self.org = org
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "orgid", orgid)
                        self.accountMetadata = addKeyValuePair(
                            accountMetadata, "org", org)
                        save_collected_metadata(self)
                        self.create_new_cf_space(environment)
                        self.create_and_assign_quota_plan(self, environment)

                elif environment.name == "kymaruntime":
                    kymaClusterName = environment.parameters["name"]

                    # Set Cluster region: the cluster region can be globally defined via the parameters file
                    # or for each environment in the usecase file. Therefore we need to consolidate the setting here
                    # In addition the difference between TRIAL and Prod must be considered => Prod has a cluster region, TRIAL has not
                    clusterregion = None

                    if environment.plan == "trial":
                        clusterregion = self.region
                    else:
                        if "region" in environment.parameters:
                            if environment.parameters["region"] != "":
                                clusterregion = environment.parameters["region"]
                            else:
                                clusterregion = self.clusterregion
                                environment.parameters["region"] = clusterregion
                        else:
                            clusterregion = self.clusterregion
                            environment.parameters["region"] = clusterregion

                    if clusterregion is None or clusterregion == "":
                        log.error(
                            "A value for the > CLUSTER REGION < was not provided but is necessary for the setup of the BTP environment >" + environment.name + "<.")
                        sys.exit(os.EX_DATAERR)

                    # Check if environment alraedy exists
                    message = "Check if Kyma cluster called " + kymaClusterName + "already exists"

                    command = "btp --format json list accounts/environment-instance --subaccount '" + \
                        subaccountid + "'"

                    result = runCommandAndGetJsonResult(
                        self, command, "INFO", message)

                    envEntry = getKymaEnvironmentInfoByClusterName(
                        result, kymaClusterName)

                    if envEntry is not None:
                        log.info("Kyma environment with name >" +
                                 kymaClusterName + "< already exists - Creation skipped")
                        continue

                    log.header("Create environment >" + environment.name + "<")

                    envName = environment.name
                    # Fix environment name for instance creation
                    btpEnvironment = "kyma"
                    parameters = None

                    envLandscape = selectEnvironmentLandscape(
                        self, environment)

                    parameters = dictToString(environment.parameters)

                    if envLandscape is not None:
                        command = "btp --format json create accounts/environment-instance --subaccount '" + subaccountid + "' --environment '" + btpEnvironment + \
                            "' --service '" + environment.name + "' --plan '" + environment.plan + \
                            "' --parameters '" + \
                            str(parameters) + "' --landscape '" + \
                            envLandscape + "'"
                    else:
                        command = "btp --format json create accounts/environment-instance --subaccount '" + subaccountid + "' --environment '" + \
                            btpEnvironment + "' --service '" + environment.name + "' --plan '" + \
                            environment.plan + "' --parameters '" + \
                            str(parameters) + "'"

                    message = "Create " + envName + \
                        " environment in cluster region >" + clusterregion + "<"

                    result = runCommandAndGetJsonResult(
                        self, command, "INFO", message)

                elif environment.name == "sapbtp":
                    log.info("the BTP environment >" + environment.name +
                             "< is automatically supported.")

                else:
                    log.error("the BTP environment >" + environment.name +
                              "< is currently not supported in this script.")
                    sys.exit(os.EX_DATAERR)

        else:
            foundOrg = False
            for environment in environments:
                if environment.name == "cloudfoundry":

                    command = "btp --format json list accounts/environment-instances --subaccount '" + \
                        subaccountid + "'"
                    result = runCommandAndGetJsonResult(
                        self, command, "INFO", "fetch org name")
                    envInstances = result["environmentInstances"]
                    for envInstance in envInstances:
                        if "labels" in envInstance and envInstance["labels"] is not None and envInstance["environmentType"] == "cloudfoundry":
                            labels = convertStringToJson(envInstance["labels"])
                            thisOrgId = labels.get("Org ID:")
                            thisOrg = labels.get("Org Name:")
                            if thisOrgId is None:
                                thisOrgId = labels.get("Org ID")
                            if thisOrg is None:
                                thisOrg = labels.get("Org Name")

                            if thisOrgId == orgid:
                                self.accountMetadata = addKeyValuePair(
                                    accountMetadata, "org", thisOrg)
                                log.header(
                                    "USING CONFIGURED ENVIRONMENT WITH ID >" + accountMetadata["orgid"] + "<")
                                foundOrg = True
            if foundOrg is False:
                log.error("could not find Cloud Foundry org with id >" +
                          orgid + "< that you've defined in your parameters.json file.")
                sys.exit(os.EX_DATAERR)

        save_collected_metadata(self)

    def create_new_cf_space(self, environment):
        cfEnvironment = False
        if environment.name == "cloudfoundry":
            cfEnvironment = True

        if cfEnvironment is True:

            accountMetadata = self.accountMetadata

            cfspacename = self.cfspacename
            org = self.org
            log.header("Create CF space >" + cfspacename + "<")

            login_cf(self)

            result = checkIfCFSpaceAlreadyExists(self)
            log.check("cfspacename >" + str(cfspacename) + "<")
            log.check("org         >" + str(org) + "<")

            if result is False:
                command = "cf create-space '" + cfspacename + "' -o '" + org + "'"
                message = "Create CF space >" + cfspacename + "<"

                runShellCommand(self, command, "INFO", message)

                command = 'cf spaces'
                message = "Check when CF space >" + cfspacename + "< is ready"
                result = try_until_cf_space_done(
                    self, command, message, cfspacename, self.repeatstatusrequest, 120)

                if result == "ERROR":
                    log.error(
                        "Something went wrong while waiting for creation of CF space >" + cfspacename + "<")

                log.success("created CF space >" + cfspacename + "<")
                self.accountMetadata = addKeyValuePair(
                    accountMetadata, "cfspacename", cfspacename)
            else:
                log.success("CF space >" + cfspacename + "< already exists")
                self.accountMetadata = addKeyValuePair(
                    accountMetadata, "cfspacename", cfspacename)

            command = 'cf target -s ' + "'" + cfspacename + "'"
            message = "Set CF target to space >" + cfspacename + "<"
            runShellCommand(self, command, "INFO", message)

            save_collected_metadata(self)

    def create_and_assign_quota_plan(self, environment):
        if environment.name == "cloudfoundry" and self.cfspacequota is not None:

            if self.cfspacequota.get("createQuotaPlan") is True:
                command = "cf create-space-quota " + \
                    self.cfspacequota.get("spaceQuotaName")

                if self.cfspacequota.get("spaceQuotaInstanceMemory") and self.cfspacequota.get("spaceQuotaInstanceMemory") is not None and self.cfspacequota.get("spaceQuotaInstanceMemory") != "":
                    command = command + " -i " + \
                        self.cfspacequota.get("spaceQuotaInstanceMemory")

                if self.cfspacequota.get("spaceQuotaTotalMemory") and self.cfspacequota.get("spaceQuotaTotalMemory") is not None and self.cfspacequota.get("spaceQuotaTotalMemory") != "":
                    command = command + " -m " + \
                        self.cfspacequota.get("spaceQuotaTotalMemory")

                if self.cfspacequota.get("self.spaceQuotaRoutes") and self.cfspacequota.get("self.spaceQuotaRoutes") is not None:
                    command = command + " -r " + \
                        str(self.cfspacequota.get("self.spaceQuotaRoutes"))

                if self.cfspacequota.get("spaceQuotaServiceInstances") and self.cfspacequota.get("spaceQuotaServiceInstances") is not None:
                    command = command + " -s " + \
                        str(self.cfspacequota.get("spaceQuotaServiceInstances"))

                if self.cfspacequota.get("spaceQuotaAppInstances") and self.cfspacequota.get("spaceQuotaAppInstances") is not None:
                    command = command + " -a " + \
                        str(self.cfspacequota.get("spaceQuotaAppInstances"))

                if self.cfspacequota.get("spaceQuotaReservedRoutePorts") and self.cfspacequota.get("spaceQuotaReservedRoutePorts") is not None:
                    command = command + " --reserved-route-ports " + \
                        str(self.cfspacequota.get("spaceQuotaReservedRoutePorts"))

                if self.cfspacequota.get("spaceQuotaAllowPaidServicePlans") and self.cfspacequota.get("spaceQuotaAllowPaidServicePlans") is True:
                    command = command + " --allow-paid-service-plans"

                runShellCommand(self, command, "INFO", "assign cf space quota")

                command = 'cf space-quotas'
                message = "Check when CF space quota >" + \
                    self.cfspacequota.get("spaceQuotaName") + "< is ready"

                result = try_until_space_quota_created(self, command, message, self.cfspacequota.get(
                    "spaceQuotaName"), self.repeatstatusrequest, 120)

                if result == "ERROR":
                    log.error(
                        "Something went wrong while waiting for creation of CF space quota >" + self.cfspacequota.get("spaceQuotaName") + "<")

                log.success("created CF space quota >" +
                            self.cfspacequota.get("spaceQuotaName") + "<")

                command = "cf set-space-quota " + \
                    self.accountMetadata["cfspacename"] + " " + \
                    self.cfspacequota.get("spaceQuotaName")
                runShellCommand(self, command, "INFO", "assign cf space quota to space")

    def createRoleCollections(self):
        assignUsersToRoleCollectionsForServices(self)
        assignUsersToCustomRoleCollections(self)

    def create_configured_app_subscriptions_and_services(self):

        ##################################################################################
        # Initiate all app subscriptions
        ##################################################################################
        initiateAppSubscriptions(self)

        ##################################################################################
        # Initiate creation of all services instances
        ##################################################################################
        initiateCreationOfServiceInstances(self)

        ##################################################################################
        # Now check when all services and subscriptions are available
        ##################################################################################
        log.header("Track creation of service instances and app subscriptions")
        self.accountMetadata = track_creation_of_subscriptions_and_services(
            self)
        save_collected_metadata(self)

        ##################################################################################
        # Now check if service keys should be created
        ##################################################################################
        self.accountMetadata = self.createServiceKeys()
        save_collected_metadata(self)

        # btp_assign_role_collection_to_admins(self)

        save_collected_metadata(self)

    def createServiceKeys(self):
        accountMetadata = self.accountMetadata

        if "createdServiceInstances" in accountMetadata and len(accountMetadata["createdServiceInstances"]) > 0:
            log.header("Create service keys if configured")
            for createdService in accountMetadata["createdServiceInstances"]:
                for service in self.definedServices:
                    if service.name == createdService["name"] and service.plan == createdService["plan"] and service.instancename is not None and service.instancename == createdService["instancename"] and "createServiceKeys" in createdService and createdService["createServiceKeys"] is not None:
                        for serviceKey in createdService["createServiceKeys"]:
                            result = createServiceKey(
                                serviceKey, service, self)
                            if "createdServiceKeys" not in createdService:
                                createdService["createdServiceKeys"] = []
                            completeResult = {
                                "keyname": serviceKey, "payload": result}
                            createdService["createdServiceKeys"].append(
                                completeResult)

        return accountMetadata

    def execute_api_test(self):
        if hasattr(self, "enableAPITest"):
            apiCheckStatus = self.enableAPITest
            if apiCheckStatus:
                log.info("\n###########---Beginning of API Testing---############\n")
                _ = self.__api_test(self)
                log.info("\n###########---API Testing Completed---############\n")

    def finish(self):
        runTrustFlow(self)

        log.header("SUCCESSFULLY EXECUTED THE USE CASE")
        log.info(
            "checkout your SAP BTP account and how it was setup for the use case")
        log.check("link to your SAP BTP sub account: " +
                  buildUrltoSubaccount(self))

        if self.prunesubaccount is True:
            pruneUseCaseAssets(self)
            pruneSubaccount(self)
        else:
            if self.pruneusecase is True:
                pruneUseCaseAssets(self)

        log.header("SUCCESSFULLY FINISHED USE CASE EXECUTION")
        sys.exit(os.EX_OK)


def getEnvironmentsForUsecase(btpUsecase: BTPUSECASE, allServices):
    items = []
    environments = []

    paramServicesFile = FOLDER_SCHEMA_LIBS + "btpsa-usecase.json"
    paramDefinition = getJsonFromFile(paramServicesFile)

    for usecaseService in allServices:
        category = usecaseService.category
        name = usecaseService.name
        if category == "ENVIRONMENT" and name not in items:
            items.append(name)
            environments.append(usecaseService)

    for usecaseService in allServices:
        environmentServices = usecaseService.targetenvironment
        if environmentServices not in items and usecaseService.category != "ENVIRONMENT" and usecaseService.targetenvironment != "sapbtp":
            items.append(environmentServices)
            paramDefinitionServices = getServiceParameterDefinition(
                paramDefinition)
            thisUsecaseService = {"name": usecaseService.targetenvironment,
                                  "category": "ENVIRONMENT", "plan": "standard"}
            thisEnv = BTPSERVICE(paramDefinitionServices,
                                 thisUsecaseService, btpUsecase)
            environments.append(thisEnv)

    return environments


def getServiceCategoryItemsFromUsecaseFile(btpUsecase: BTPUSECASE, allServices, categories):
    items = []
    for usecaseService in allServices:
        thisCategory = usecaseService.category
        if thisCategory in categories:
            usecaseService.status = "NOT READY"
            usecaseService.servicebroker = None
            usecaseService.successInfoShown = False
            items.append(usecaseService)
    return items


def getAdminsFromUsecaseFile(btpUsecase: BTPUSECASE):
    usecase = getJsonFromFile(btpUsecase.usecasefile)

    items = []
    if "admins" in usecase:
        for admin in usecase["admins"]:
            items.append(admin)
    else:
        log.warning(
            "no admins defined in your use case configuration file (other than you)")

    return items


def getServiceTestStatusFromUsecaseFile(btpUsecase: str):
    usecase = getJsonFromFile(btpUsecase)
    if not usecase.get("enableAPITest", False):
        return False
    return True


def check_if_account_can_cover_use_case_for_serviceType(btpUsecase: BTPUSECASE, availableForAccount, availableCustomApps):

    usecaseRegion = btpUsecase.region
    fallbackServicePlan = None

    if btpUsecase.fallbackserviceplan is not None and btpUsecase.fallbackserviceplan != "":
        fallbackServicePlan = btpUsecase.fallbackserviceplan

    usecaseSupported = True

    # Put all service types together into one
    allServices = []
    for service in btpUsecase.definedServices:
        if service.category != "CF_CUP_SERVICE":
            allServices.append(service)
    for app in btpUsecase.definedAppSubscriptions:
        allServices.append(app)

    for usecaseService in allServices:
        usecaseServiceName = usecaseService.name
        usecaseServicePlan = usecaseService.plan
        if usecaseService.category is None or usecaseService.category == "":
            log.warning("the service >" + usecaseServiceName +
                        "< is missing the category key/value in the use case config file. Script will assume that category is >SERVICE<")

        supported = False
        supportedFallbackServicePlan = False

        for accountService in availableForAccount["entitledServices"]:
            accountServiceName = accountService["name"]
            if (accountServiceName == usecaseServiceName):
                for accountServicePlan in accountService["servicePlans"]:
                    accountServicePlanName = accountServicePlan["name"]
                    accountServicePlanCategory = accountServicePlan["category"]
                    if fallbackServicePlan is not None and accountServicePlanName == fallbackServicePlan:
                        for accountServicePlanDataCenter in accountServicePlan["dataCenters"]:
                            accountServicePlanRegion = accountServicePlanDataCenter["region"]
                            if (accountServicePlanRegion == usecaseRegion) and (isService(btpUsecase, accountServicePlanCategory, usecaseService.category)):
                                supportedFallbackServicePlan = True
                    if (accountServicePlanName == usecaseServicePlan) and (isService(btpUsecase, accountServicePlanCategory, usecaseService.category)):
                        for accountServicePlanDataCenter in accountServicePlan["dataCenters"]:
                            accountServicePlanRegion = accountServicePlanDataCenter["region"]
                            if (accountServicePlanRegion == usecaseRegion):
                                supported = True

        # Special Case for custom apps (exist only in subaccount)
        if supported is False and usecaseService.category == "APPLICATION" and usecaseService.customerDeveloped is True and len(availableCustomApps) != 0:
            # Custom apps are only available in subaccount as app => check "availableCustomApps"
            for customApp in availableCustomApps:
                if customApp["appName"] == usecaseService.name:
                    supported = True

        if (supported is True):
            log.success("service  >" + usecaseServiceName + "< with plan >" +
                        usecaseServicePlan + "< in region >" + usecaseRegion + "< IS AVAILABLE")
        else:
            if fallbackServicePlan is not None and supportedFallbackServicePlan is True:
                log.warning("defined plan >" + usecaseServicePlan + "< not available, but using configured default fallback plan >" +
                            fallbackServicePlan + "< for service >" + usecaseServiceName + "<")
                log.success("service  >" + usecaseServiceName + "< with default fallback plan >" +
                            fallbackServicePlan + "< in region >" + usecaseRegion + "< IS AVAILABLE")
                usecaseService.plan = fallbackServicePlan
            else:
                log.error("service >" + usecaseServiceName + "< with plan >" +
                          usecaseServicePlan + "< in region >" + usecaseRegion + "< IS NOT AVAILABLE")
                usecaseSupported = False

    return usecaseSupported


def isService(btpUsecase: BTPUSECASE, accountServicePlanCategory, category):
    result = False
    categoryService = btpUsecase.availableCategoriesService
    categoryApplication = btpUsecase.availableCategoriesApplication

    if accountServicePlanCategory in categoryService or accountServicePlanCategory in categoryApplication:
        if category in categoryService or category in categoryApplication:
            result = True
    return result


def checkIfSubaccountAlreadyExists(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    command = "btp --format json list accounts/subaccount --global-account '" + \
        btpUsecase.globalaccount + "'"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    if "subaccount" in accountMetadata:
        subaccountName = accountMetadata["subaccount"]

        for account in result["value"]:
            if account["displayName"] == subaccountName:
                return account["guid"]
        # If the for loop didn't return any value, the subaccount wasn't found
        return None
    else:
        return None


def getListOfAvailableServicesAndApps(btpUsecase: BTPUSECASE):
    globalaccount = btpUsecase.globalaccount
    usecaseRegion = btpUsecase.region

    command = "btp --format json list accounts/entitlement --global-account '" + \
        globalaccount + "'"
    message = "Get list of available services and app subsciptions for defined region >" + \
        usecaseRegion + "<"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

    return result


def getListOfAvailableCustomApps(btpUsecase: BTPUSECASE):
    customAppProviderSubaccountId = btpUsecase.customAppProviderSubaccountId
    result = []
    if btpUsecase.customAppProviderSubaccountId is not None:
        command = "btp --format json list accounts/subscription --subaccount '" + \
            customAppProviderSubaccountId + "'"
        message = "Get list of available apps subsciptions for provider subaccount id >" + \
            customAppProviderSubaccountId + "<"
        resultSubaccount = runCommandAndGetJsonResult(
            btpUsecase, command, "INFO", message)

        for appSubaccount in resultSubaccount["applications"]:
            if appSubaccount["customerDeveloped"] is True:
                result.append(appSubaccount)

    return result


def get_globalaccount_details(btpUsecase: BTPUSECASE):
    globalaccount = btpUsecase.globalaccount

    log.header(
        "Get accountdetails for your global account with subdomain id >" + globalaccount + "<")
    # Create a new json variable for collected metadata
    metadata = convertStringToJson("{}")

    command = "btp --format json get accounts/global-account --global-account '" + \
        globalaccount + "'"
    message = "Get global account details for account with subdomain ID >" + globalaccount + "<"

    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)
    license_type = result["licenseType"]
    commercial_model = result["commercialModel"]
    global_account_id = result["guid"]

    if btpUsecase.cfspacename is None or btpUsecase.cfspacename == "":
        btpUsecase.cfspacename = "development"

    metadata = addKeyValuePair(
        metadata, "globalaccount", btpUsecase.globalaccount)
    metadata = addKeyValuePair(
        metadata, "global_account_id", global_account_id)
    metadata = addKeyValuePair(metadata, "licenseType", license_type)
    metadata = addKeyValuePair(metadata, "commercialModel", commercial_model)

    return metadata


def getDetailsAboutSubaccount(btpUsecase: BTPUSECASE, subaccountid):
    command = "btp --format json get accounts/subaccount '" + \
        subaccountid + "' --global-account '" + btpUsecase.globalaccount + "'"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)
    return result


def try_until_done(btpUsecase: BTPUSECASE, command, message, key, value, search_every_x_seconds, timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        checkMessage = message + " (try " + str(number_of_tries) + \
            " - trying again in " + str(search_every_x_seconds) + "s)"
        result = runCommandAndGetJsonResult(
            btpUsecase, command, "CHECK", checkMessage)
        status = result[key]
        if status == value:
            return "DONE"
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds

    return result


def assign_entitlement(btpUsecase: BTPUSECASE, service):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    serviceName = service.name
    servicePlan = service.plan

    baseCommand = "btp --format json assign accounts/entitlement \
    --to-subaccount '" + subaccountid + "' \
    --for-service '" + serviceName + "' \
    --plan '" + servicePlan + "'"

    command = baseCommand + " --distribute --enable"

    message = "Assign entitlement for >" + \
        serviceName + "< and plan >" + servicePlan + "<"
    # Run script, but don't exit, if not successfull
    p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
    returnCode = p.returncode

    if returnCode != 0:
        log.warning(
            "this entitlement wasn't sucesssfull. Trying to entitle with amount parameter instead.")

        if service.amount is not None and service.amount > 0:
            command = baseCommand + " --auto-distribute-amount " + \
                str(service.amount) + " --amount " + str(service.amount)
        else:
            command = baseCommand + " --auto-distribute-amount 1  --amount 1"

        message = "Try again to assign entitlement for >" + serviceName + \
            "< and plan >" + servicePlan + "< with amount parameter set to 1."
        p = runShellCommand(btpUsecase, command, "INFO", message)
        returnCode = p.returncode

    # Wait untile the service and service plan is entitled in the subaccount
    if returnCode == 0:
        command = "btp --format json list accounts/entitlement \
        --subaccount '" + subaccountid + "'"
        message = "Check if entitlement for >" + \
            serviceName + "< and plan >" + servicePlan + "< is available"

        # Tun through this loop
        current_time = 0
        number_of_tries = 0
        timeout_after_x_seconds = 60
        search_every_x_seconds = 2
        serviceEntitled = False
        # Repeat checking whether the entitlement was successfull
        while timeout_after_x_seconds > current_time and serviceEntitled is False:
            number_of_tries += 1
            checkMessage = message + " (try " + str(number_of_tries) + \
                " - trying again in " + str(search_every_x_seconds) + "s)"
            result = runCommandAndGetJsonResult(
                btpUsecase, command, "CHECK", checkMessage)
            for entry in result.get("quotas"):
                if entry.get("plan") == servicePlan and entry.get("service") == serviceName:
                    serviceEntitled = True
                    returnCode = 0
                    break
            if serviceEntitled == False:
                time.sleep(search_every_x_seconds)
                current_time += search_every_x_seconds
                returnCode = 1

    return returnCode


def subscribe_app_to_subaccount(btpUsecase: BTPUSECASE, app, plan):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    command = "btp subscribe accounts/subaccount \
    --subaccount '" + subaccountid + "' \
    --to-app '" + app + "' \
    --plan '" + plan + "'"

    isAlreadySubscribed = checkIfAppIsSubscribed(btpUsecase, app, plan)
    if isAlreadySubscribed is False:
        message = "subscribe sub account to >" + app + "< and plan >" + plan + "<"
        runShellCommand(btpUsecase, command, "INFO", message)
    else:
        log.info("subscription already there for >" +
                 app + "< and plan >" + plan + "<")


def checkIfAppIsSubscribed(btpUsecase: BTPUSECASE, appName, appPlan):
    result = False
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    command = "btp --format json get accounts/subscription --subaccount '" + \
        subaccountid + "' --of-app '" + appName + "' --plan '" + appPlan + "'"
    resultCommand = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", "check if app already subscribed")

    if "state" in resultCommand and resultCommand["state"] == "SUBSCRIBED":
        result = True

    return result


def doAllEntitlements(btpUsecase: BTPUSECASE, allItems):

    # Ensure to have a list of all entitlements as combination of service name and plan
    entitlements = []
    for service in allItems:
        thisName = service.name
        thisPlan = service.plan
        # Exclude custom developed services as they cannot be entitled
        if not any(d.name == thisName and d.plan == thisPlan for d in entitlements) and service.customerDeveloped is False:
            entitlements.append(service)

    # Now set the amount for the entitlement right
    # Simply sum-up all amounts to one amount per name/plan combination
    for entitlement in entitlements:
        amount = 0
        thisName = entitlement.name
        thisPlan = entitlement.plan
        for service in allItems:
            serviceName = service.name
            servicePlan = service.plan
            serviceAmount = service.amount
            if (serviceName == thisName and servicePlan == thisPlan):
                amount += serviceAmount
        entitlement.amount = amount

    for service in entitlements:
        # Quickly assign all entitlements (without waiting until they are all done)
        assign_entitlement(btpUsecase, service)


def initiateAppSubscriptions(btpUsecase: BTPUSECASE):
    if btpUsecase.definedAppSubscriptions is not None and len(btpUsecase.definedAppSubscriptions) > 0:

        log.header("Initiate subscriptions to apps")

        # Now do all the subscriptions
        for appSubscription in btpUsecase.definedAppSubscriptions:
            appName = appSubscription.name
            appPlan = appSubscription.plan
            if appSubscription.entitleonly is False:
                subscribe_app_to_subaccount(btpUsecase, appName, appPlan)


def get_subscription_status(btpUsecase: BTPUSECASE, app):
    accountMetadata = btpUsecase.accountMetadata

    app_name = app.name
    app_plan = app.plan
    subaccountid = accountMetadata["subaccountid"]

    command = "btp --format json list accounts/subscription --subaccount '" + subaccountid + "'"
    message = "subscription status of >" + app_name + "<"
    p = runShellCommand(btpUsecase, command, "CHECK", message)
    result = p.stdout.decode()
    result = convertStringToJson(result)

    for application in result["applications"]:
        thisAppName = application["appName"]
        thisAppPlan = application["planName"]
        if (thisAppName == app_name and thisAppPlan == app_plan):
            return application

    log.error("COULD NOT FIND SUBSCRIPTON TO >" +
              app_name + "< and plan >" + app_plan + "<")
    sys.exit(os.EX_DATAERR)


def get_subscription_deletion_status(btpUsecase: BTPUSECASE, app):
    accountMetadata = btpUsecase.accountMetadata

    app_name = app["name"]
    app_plan = app["plan"]
    subaccountid = accountMetadata["subaccountid"]

    command = "btp --format json list accounts/subscription --subaccount '" + subaccountid + "'"
    message = "subscription status of >" + app_name + "<"
    p = runShellCommandFlex(btpUsecase, command,
                            "CHECK", message, False, False)
    result = p.stdout.decode()
    result = convertStringToJson(result)

    for application in result["applications"]:
        thisAppName = application["appName"]
        thisAppPlan = application["planName"]
        status = application["state"]
        if (thisAppName == app_name and thisAppPlan == app_plan):
            if status == "NOT_SUBSCRIBED":
                return "deleted"
            if status == "UNSUBSCRIBE_FAILED":
                return "UNSUBSCRIBE_FAILED"
    return "not deleted"


def checkIfAllSubscriptionsAreAvailable(btpUsecase: BTPUSECASE):
    command = "btp --format json list accounts/subscription --subaccount '" + \
        btpUsecase.subaccountid + "'"
    resultCommand = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", "check status of app subscriptions")

    allSubscriptionsAvailable = True
    for app in btpUsecase.definedAppSubscriptions:
        for thisJson in resultCommand["applications"]:
            name = thisJson.get("appName")
            plan = thisJson.get("planName")
            status = thisJson.get("state")
            tenantId = thisJson.get("tenantId")

            if app.name == name and app.plan == plan and app.successInfoShown is False:
                if status == "SUBSCRIBE_FAILED":
                    log.error(
                        "BTP account reported that subscription on >" + app.name + "< has failed.")
                    sys.exit(os.EX_DATAERR)

                if status != "SUBSCRIBED":
                    allSubscriptionsAvailable = False
                    app.status = status
                    app.successInfoShown = False
                    app.statusResponse = thisJson
                else:
                    log.success("subscription to app >" + app.name +
                                "< (plan " + app.plan + ") is now available")
                    app.tenantId = tenantId
                    app.successInfoShown = True
                    app.statusResponse = thisJson
                    app.status = "SUBSCRIBED"

    return allSubscriptionsAvailable


def determineTimeToFetchStatusUpdates(btpUsecase: BTPUSECASE):
    maxTiming = int(btpUsecase.repeatstatusrequest)

    for service in btpUsecase.definedServices:
        status = service.status
        if service.repeatstatusrequest is not None:
            repeatstatusrequest = service.repeatstatusrequest
            if repeatstatusrequest > maxTiming and status != "create succeeded":
                maxTiming = repeatstatusrequest

    return maxTiming


def track_creation_of_subscriptions_and_services(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    current_time = 0

    usecaseTimeout = btpUsecase.repeatstatustimeout
    while usecaseTimeout > current_time:
        areAllInstancesCreated = True
        areAllSubscriptionsCreated = True

        if len(btpUsecase.definedServices) > 0:
            areAllInstancesCreated = checkIfAllServiceInstancesCreated(
                btpUsecase)

        if len(btpUsecase.definedAppSubscriptions) > 0:
            areAllSubscriptionsCreated = checkIfAllSubscriptionsAreAvailable(
                btpUsecase)

        if (areAllInstancesCreated is True and areAllSubscriptionsCreated is True):
            log.success(
                "All service instances and subscriptions are now available".upper())
            accountMetadata = addCreatedServicesToMetadata(btpUsecase)
            return accountMetadata

        search_every_x_seconds = determineTimeToFetchStatusUpdates(btpUsecase)
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds

    log.error(
        "Could not get all services and/or app subscriptions up and running. Sorry.")


def addCreatedServicesToMetadata(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    if "createdServiceInstances" not in accountMetadata:
        accountMetadata = addKeyValuePair(
            accountMetadata, "createdServiceInstances", [])

    if "createdAppSubscriptions" not in accountMetadata:
        accountMetadata = addKeyValuePair(
            accountMetadata, "createdAppSubscriptions", [])

    if len(btpUsecase.definedAppSubscriptions) > 0:
        for service in btpUsecase.definedAppSubscriptions:
            thisService = convertStringToJson(json.dumps(
                service, indent=4, cls=BTPSERVICEEncoder))
            accountMetadata["createdAppSubscriptions"].append(thisService)

    if len(btpUsecase.definedServices) > 0:
        for service in btpUsecase.definedServices:
            thisService = convertStringToJson(json.dumps(
                service, indent=4, cls=BTPSERVICEEncoder))
            accountMetadata["createdServiceInstances"].append(thisService)

    return accountMetadata


def checkConfigurationInfo(btpUsecase: BTPUSECASE):

    # checkEmailsinUsecaseConfig(btpUsecase)
    None


def pruneSubaccount(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    command = "btp --format json delete accounts/subaccount '" + \
        accountMetadata["subaccountid"] + "' --global-account '" + \
        btpUsecase.globalaccount + "' --confirm"
    message = "Delete sub account"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    search_every_x_seconds = btpUsecase.repeatstatusrequest
    usecaseTimeout = btpUsecase.repeatstatustimeout

    current_time = 0
    while usecaseTimeout > current_time:
        command = "btp --format json list accounts/subaccount"
        message = "Check if account deleted"
        result = runCommandAndGetJsonResult(
            btpUsecase, command, "CHECK", message)
        if "value" in result:
            accountStillThere = False
            for item in result["value"]:
                if item["guid"] == accountMetadata["subaccountid"]:
                    accountStillThere = True
            if accountStillThere is True:
                time.sleep(search_every_x_seconds)
                current_time += search_every_x_seconds
            else:
                log.success("Deleted sub account")
                return True

    log.error("Could not deleted sub account")
    sys.exit(os.EX_DATAERR)


def pruneUseCaseAssets(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    log.header("Remove assets created for this use case")

    # Execute commands defined in the use case file to be done to remove assets that are not covered from the services and app subscriptions
    executeCommandsFromUsecaseFile(
        btpUsecase, "execute commands from use case file", "executeToPruneUseCase")

    if "createdAppSubscriptions" in accountMetadata and len(accountMetadata["createdAppSubscriptions"]) > 0:
        log.info("Unsubscribe from apps")
        for service in accountMetadata["createdAppSubscriptions"]:
            command = "btp --format json unsubscribe accounts/subaccount --subaccount '" + \
                accountMetadata["subaccountid"] + \
                "' --from-app '" + service["name"] + "' --confirm"
            message = "Remove app subscription >" + \
                service["name"] + "< from subaccount"
            result = runCommandAndGetJsonResult(
                btpUsecase, command, "INFO", message)
        # check status of deletion
        search_every_x_seconds = btpUsecase.repeatstatusrequest
        usecaseTimeout = btpUsecase.repeatstatustimeout
        current_time = 0
        allServicesDeleted = False
        # Set the deletion status to "not deleted"
        for service in accountMetadata["createdAppSubscriptions"]:
            service["deletionStatus"] = "not deleted"

        while usecaseTimeout > current_time and allServicesDeleted is False:
            for service in accountMetadata["createdAppSubscriptions"]:
                if service["deletionStatus"] == "deleted":
                    continue
                status = get_subscription_deletion_status(btpUsecase, service)
                if (status == "deleted" and service["deletionStatus"] != "deleted"):
                    log.success("app subscription for app >" +
                                service["name"] + "< now deleted")
                    service["deletionStatus"] = "deleted"
                if (status == "UNSUBSCRIBE_FAILED"):
                    log.error(
                        "unsubscribing app >" + service["name"] + "< failed. Returned status >" + status + "<")
                    service["deletionStatus"] = "UNSUBSCRIBE_FAILED"
                    log.info(
                        "trying again to remove the subscription to app >" + service["name"] + "<")
                    result = runCommandAndGetJsonResult(
                        btpUsecase, command, "INFO", message)
                    service["deletionStatus"] = status
                else:
                    service["deletionStatus"] = status
            time.sleep(search_every_x_seconds)
            current_time += search_every_x_seconds
            allServicesDeleted = True
            for service in accountMetadata["createdAppSubscriptions"]:
                if service["deletionStatus"] != "deleted":
                    allServicesDeleted = False

    if "createdServiceInstances" in accountMetadata and len(accountMetadata["createdServiceInstances"]) > 0:
        log.info("Delete service instances")

        # Initiate deletion of service instances
        for service in accountMetadata["createdServiceInstances"]:
            if "createdServiceKeys" in service:
                for key in service["createdServiceKeys"]:
                    deleteServiceKeysAndWait(key, service, btpUsecase)

            if "instancename" in service and service["instancename"] is not None and service["instancename"] != "":
                deleteServiceInstance(service, btpUsecase)

        log.info("Check deletion status for service instances")
        # check status of deletion
        search_every_x_seconds = btpUsecase.repeatstatusrequest
        usecaseTimeout = btpUsecase.repeatstatustimeout
        current_time = 0
        allServicesDeleted = False
        # Set the deletion status to "not deleted"
        for service in accountMetadata["createdServiceInstances"]:
            service["deletionStatus"] = "not deleted"
            service["failedDeletions"] = 0
        maxRetriesForFailedDeletion = 5    
        while usecaseTimeout > current_time and allServicesDeleted is False:
            for service in accountMetadata["createdServiceInstances"]:
                if "instancename" not in service:
                    status = "deleted"
                    service["deletionStatus"] = status
                    log.info("no service instance available for service >" +
                             service["name"] + "<. Deletion not needed.")
                    continue

                status = getServiceDeletionStatus(service, btpUsecase)

                if (status == "delete failed"):
                    log.warning("couldn't delete service instance >" +
                                service["instancename"] + "< for service >" + service["name"] + "<.")
                    if service["failedDeletions"] <= maxRetriesForFailedDeletion:
                        log.info("trying again to delete service instance >" +
                                 service["instancename"] + "< for service >" + service["name"] + "<.")
                        deleteServiceInstance(service, btpUsecase)
                        service["deletionStatus"] = "not deleted"
                        service["failedDeletions"] = service["failedDeletions"] + 1
                    else:
                        log.error("tried " + str(service["failedDeletions"]) + "times, but could not delete service instance >" +
                                  service["instancename"] + "< for service >" + service["name"] + "<.")
                        sys.exit(os.EX_DATAERR)

                if (status == "deleted"):
                    log.success(
                        "service instance >" + service["instancename"] + "< for service >" + service["name"] + "< now deleted.")
                    service["deletionStatus"] = "deleted"
                else:
                    service["deletionStatus"] = status
            time.sleep(search_every_x_seconds)
            current_time += search_every_x_seconds
            allServicesDeleted = True
            for service in accountMetadata["createdServiceInstances"]:
                if service["deletionStatus"] != "deleted":
                    allServicesDeleted = False
        log.success("all service instances now deleted.")

    for environment in btpUsecase.definedEnvironments:
        if environment.name == "cloudfoundry":
            log.info("Cloud Foundry envorinment will be deleted automatically with the deletion of the sub account. No separate deletion needed.")

        if environment.name == "kymaruntime":
            # Get Kyma runtime ID
            message = "Get Kyma environment ID for subaccount > " + \
                btpUsecase.accountMetadata["subaccountid"] + " < by name > " + \
                btpUsecase.accountMetadata["subaccountid"] + " <"
            command = "btp --format json list accounts/environment-instance --subaccount '" + \
                btpUsecase.accountMetadata["subaccountid"] + "'"

            result = runCommandAndGetJsonResult(
                btpUsecase, command, "INFO", message)

            kymaEnvironmentID = getKymaEnvironmentIdByClusterName(
                result, environment.parameters["name"])

            # Delete Kyma runtime via SAP btp CLI
            message = "Trigger deletion of Kyma environment > " + \
                environment.parameters["name"] + \
                " < in subaccount > " + \
                btpUsecase.accountMetadata["subaccountid"] + " <"

            command = "btp --format json delete accounts/environment-instance '" + kymaEnvironmentID + \
                "' --subaccount '" + \
                btpUsecase.accountMetadata["subaccountid"] + "' --confirm"

            result = runCommandAndGetJsonResult(
                btpUsecase, command, "INFO", message)

            log.info("Check deletion status for Kyma environment")

            environmentDeprovisioningPollFrequencyInSeconds = btpUsecase.pollingIntervalForKymaDeprovisioningInMinutes * 60
            environmentDeprovisioningTimeoutInSeconds = btpUsecase.timeoutLimitForKymaDeprovisioningInMinutes * 60
            current_time = 0
            numberOfTries = 0

            while environmentDeprovisioningTimeoutInSeconds > current_time:
                numberOfTries += 1
                message = "Check Kyma deletion status for subaccount > " + \
                    btpUsecase.accountMetadata["subaccountid"] + " < named > " + \
                    environment.parameters["name"] + " < (try " + str(numberOfTries) + " - trying again in " + \
                    str(btpUsecase.pollingIntervalForKymaDeprovisioningInMinutes) + "min)"
                command = "btp --format json list accounts/environment-instance --subaccount '" + \
                    btpUsecase.accountMetadata["subaccountid"] + "'"

                result = runCommandAndGetJsonResult(
                    btpUsecase, command, "INFO", message)

                kymaEnvironmentID = getKymaEnvironmentIdByClusterName(
                    result, environment.parameters["name"])

                if kymaEnvironmentID is None:
                    log.success("KYMA ENVIRONMENT DELETED.")
                    return "DONE"

                time.sleep(environmentDeprovisioningPollFrequencyInSeconds)
                current_time += environmentDeprovisioningPollFrequencyInSeconds


def selectEnvironmentLandscape(btpUsecase: BTPUSECASE, environment):
    accountMetadata = btpUsecase.accountMetadata

    region = None

    if environment.name == "cloudfoundry":
        region = btpUsecase.region
    elif environment.name == "kymaruntime" and environment.plan != "trial":
        region = environment.parameters["region"]
    else:
        region = btpUsecase.region

    subaccountid = accountMetadata["subaccountid"]

    message = "Check for available environment landscapes in subaccount >" + \
        subaccountid + "< and region >" + region + "<"
    command = "btp --format json list accounts/available-environment --subaccount '" + \
        subaccountid + "'"

    # Entitlements may not be available ad hoc, so we need to have a few retries
    # Values for retries are hard coded, but maybe candidate for configuration seeting.
    number_of_tries = 0
    current_time = 0
    timeout_after_x_seconds = 15
    search_every_x_seconds = 3

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        checkMessage = message + " (try " + str(number_of_tries) + \
            " - trying again in " + str(search_every_x_seconds) + "s)"
        result = runCommandAndGetJsonResult(
            btpUsecase, command, "INFO", checkMessage)
        if "availableEnvironments" in result:
            for item in result["availableEnvironments"]:
                servicePlan = item["planName"]
                environmentType = item["environmentType"]
                if "landscapeLabel" not in item:
                    return None
                # Simply take the first landscape that is found, matching the environment and the plan
                if environment.plan == servicePlan and environment.name == environmentType:
                    return item["landscapeLabel"]
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds

    log.error("No matching environment found >" +
              environment["name"] + "< for >" + region + "<")
    sys.exit(os.EX_DATAERR)
