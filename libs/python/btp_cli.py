import libs.python.helperArgParser as helperArgParser
from libs.python.helperJson import addKeyValuePair, dictToString, convertStringToJson, saveJsonToFile, getJsonFromFile
from libs.python.helperBtpTrust import delete_cf_service_key, runTrustFlow, get_cf_service_key
from libs.python.helperCommandExecution import executeCommandsFromUsecaseFile, runShellCommand, runCommandAndGetJsonResult, runShellCommandFlex, login_btp, login_cf
from libs.python.helperEnvCF import checkIfAllServiceInstancesCreated, checkIfCFEnvironmentAlreadyExists, checkIfCFSpaceAlreadyExists, try_until_cf_space_done, initiateCreationOfServiceInstances, get_cf_service_deletion_status
from libs.python.helperGeneric import buildUrltoSubaccount, getNamingPatternForServiceSuffix, createSubaccountName, createSubdomainID, createOrgName, getTimingsForStatusRequest
from libs.python.helperFileAccess import writeKubeConfigFileToDefaultDir
from libs.python.helperEnvKyma import extractKymaDashboardUrlFromEnvironmentDataEntry, getKymaEnvironmentInfoByClusterName, getKymaEnvironmentStatusFromEnvironmentDataEntry, extractKymaKubeConfigUrlFromEnvironmentDataEntry, getKymaEnvironmentIdByClusterName

import os
import re
import sys
import time
import requests
import json

from libs.python.helperServices import BTPSERVICE, BTPSERVICEEncoder, readAllServicesFromUsecaseFile
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
        log.info("Git version >" + os.getenv('BTPSA_VERSION_GIT', "not set") + "<")

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

        self.definedServices = getServiceCategoryItemsFromUsecaseFile(self, allServices, ["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"])
        self.definedEnvironments = getEnvironmentsForUsecase(self, allServices)
        self.admins = getAdminsFromUsecaseFile(self)
        self.definedAppSubscriptions = getServiceCategoryItemsFromUsecaseFile(self, allServices, ["APPLICATION"])

        ##############################################################################################
        # From here on, we have all the data together that we need to move ahead
        ##############################################################################################

        login_btp(self)
        self.accountMetadata = get_globalaccount_details(self)
        save_collected_metadata(self)
        checkConfigurationInfo(self)

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
        log.header("Checking if all configured services & app subscriptions are available on your global account")

        availableForAccount = getListOfAvailableServicesAndApps(self)

        usecaseSupportsServices = check_if_account_can_cover_use_case_for_serviceType(self, availableForAccount)

        if usecaseSupportsServices is False:
            log.error("USE CASE NOT SUPPORTED IN YOUR GLOBAL ACCOUNT!")
            sys.exit(os.EX_PROTOCOL)
        else:
            log.success("Use case supported in your global account!")

    def prune_subaccount(self, subaccountid):
        login_btp(self)
        command = "btp delete accounts/subaccount \"" + subaccountid + "\" --global-account \"" + self.globalaccount + "\" --confirm  --force-delete"
        runShellCommand(self, command, "INFO", "delete directory >" + subaccountid + "<")

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
                command = "btp --format json list accounts/environment-instance --subaccount \"" + \
                    self.accountMetadata["subaccountid"] + "\""

                while timeoutInSeconds > current_time:
                    number_of_tries += 1
                    checkMessage = message + " (try " + str(number_of_tries) + \
                        " - trying again in " + \
                        str(self.pollingIntervalForKymaCreationInMinutes) + "min)"
                    result = runCommandAndGetJsonResult(self, command, "INFO", checkMessage)

                    entryOfKymaEnv = getKymaEnvironmentInfoByClusterName(result, kymaClusterName)

                    if getKymaEnvironmentStatusFromEnvironmentDataEntry(entryOfKymaEnv) == "OK":

                        log.info("Kyma Environment created - extracting kubeconfig URL")
                        self.accountMetadata = addKeyValuePair(accountMetadata, "kymaDashboardUrl", extractKymaDashboardUrlFromEnvironmentDataEntry(entryOfKymaEnv))
                        self.accountMetadata = addKeyValuePair(accountMetadata, "kymaKubeConfigUrl", extractKymaKubeConfigUrlFromEnvironmentDataEntry(entryOfKymaEnv))
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
                            log.error("Could not download kubeconfig from >" + self.accountMetadata["kymaKubeConfigUrl"] + "<")
                            return "ERROR"

                    time.sleep(pollingIntervalInSeconds)
                    current_time += pollingIntervalInSeconds

    def entitle_subaccount(self):
        log.header("Entitle sub account to use services and/or app subscriptions")
        envsToEntitle = []
        for myEnv in self.definedEnvironments:
            if myEnv.name != "cloudfoundry":
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
        self.accountMetadata = addKeyValuePair(accountMetadata, "subaccountid", subaccountid)

        if "subaccountid" not in accountMetadata or accountMetadata["subaccountid"] == "" or accountMetadata["subaccountid"] is None:

            log.warning("no subaccount id provided and tool will make up one for you")
            usecaseRegion = self.region

            subaccount = createSubaccountName(self)
            subdomain = createSubdomainID(self)

            log.success("using subaccount name >" + subaccount + "<")
            log.success("using subaccount domain >" + subdomain + "<")

            admins = build_admins_list(self)
            globalAccount = self.globalaccount

            log.header("Create sub account >" + subaccount + "< (if not already existing)")

            subaccountid = checkIfSubaccountAlreadyExists(self)

            if subaccountid is None:
                command = "btp --format json create accounts/subaccount \
                    --display-name \"" + subaccount + "\" \
                    --subdomain \"" + subdomain + "\" \
                    --region \"" + usecaseRegion + "\" \
                    --subaccount-admins '" + admins + "'"

                message = "Create sub account >" + subaccount + "<"
                result = runCommandAndGetJsonResult(self, command, "INFO", message)

                subaccountid = result["guid"]

                # Wait until the sub account has been created
                command = "btp --format json get accounts/subaccount \"" + subaccountid + "\" --global-account \"" + globalAccount + "\""
                result = try_until_done(self, command, message, "state", "OK", self.repeatstatusrequest, 100)
                if result == "ERROR":
                    log.error("Something went wrong while waiting for the subaccount >" + subaccount + "< with id >" + subaccountid + "<")

                log.success("created subaccount >" + subaccount + "< with id >" + subaccountid + "<")
            else:
                log.success("subaccount >" + subaccount + "< already exists with id >" + subaccountid + "<")
                self.subaccountid = subaccountid

            self.accountMetadata = addKeyValuePair(accountMetadata, "subaccountid", subaccountid)
            self.subaccountid = subaccountid
        else:
            log.header("USING CONFIGURED SUBACCOUNT WITH ID >" + self.subaccountid + "<")
            result = getDetailsAboutSubaccount(self, self.subaccountid)
            self.accountMetadata = addKeyValuePair(accountMetadata, "subdomain", result["subdomain"])

        save_collected_metadata(self)

    def initialize_environments(self):

        self.create_environments()

    def create_environments(self):

        accountMetadata = self.accountMetadata
        environments = self.definedEnvironments

        subaccountid = accountMetadata["subaccountid"]

        orgid = self.orgid
        self.accountMetadata = addKeyValuePair(accountMetadata, "orgid", orgid)

        if self.orgid is not None and self.orgid != "":
            self.accountMetadata = addKeyValuePair(accountMetadata, "orgid", self.orgid)

        if self.orgid is None or self.orgid == "":

            for environment in environments:

                if environment.name == "cloudfoundry":
                    orgid, org = checkIfCFEnvironmentAlreadyExists(self)

                    if org is None or orgid is None:

                        envName = environment.name
                        envPlan = environment.plan

                        log.header("Create environment >" + envName + "<")

                        org = createOrgName(self, envName)

                        accountMetadata = addKeyValuePair(accountMetadata, "org", org)

                        parameters = '{\"instance_name\": \"' + org + '\"}'

                        envLandscape = selectEnvironmentLandscape(self, environment)

                        if envLandscape is not None:
                            command = "btp --format json create accounts/environment-instance --subaccount \"" + subaccountid + "\" --environment " + envName + \
                                " --service " + environment.name + " --plan " + envPlan + " --parameters '" + str(parameters) + "' --landscape \"" + envLandscape + "\""
                        else:
                            command = "btp --format json create accounts/environment-instance --subaccount \"" + subaccountid + "\" --environment " + envName + \
                                " --service " + environment.name + " --plan " + envPlan + " --parameters '" + str(parameters) + "'"

                        message = "Create " + envName + " environment >" + org + "<"
                        result = runCommandAndGetJsonResult(self, command, "INFO", message)

                        orgid = result["id"]

                        # Wait until the org has been created
                        message = "is CF environment >" + org + "< created"
                        command = "btp --format json get accounts/environment-instance '" + orgid + "' --subaccount '" + subaccountid + "'"

                        result = try_until_done(self, command, message, "state", "OK", self.repeatstatusrequest, 100)
                        if result == "ERROR":
                            log.error("Something went wrong while waiting for creation of CF environment >" + org + "< with id >" + orgid + "<")

                        log.success("created CF environment >" + org + "< with id >" + orgid + "<")
                        self.orgid = orgid
                        self.org = org
                        self.accountMetadata = addKeyValuePair(accountMetadata, "orgid", orgid)
                        self.accountMetadata = addKeyValuePair(accountMetadata, "org", org)

                        save_collected_metadata(self)
                        self.create_new_cf_space(environment)

                    else:
                        log.success("CF environment >" + org + "< already available with id >" + orgid + "<")
                        self.orgid = orgid
                        self.org = org
                        self.accountMetadata = addKeyValuePair(accountMetadata, "orgid", orgid)
                        self.accountMetadata = addKeyValuePair(accountMetadata, "org", org)
                        save_collected_metadata(self)
                        self.create_new_cf_space(environment)

                elif environment.name == "kymaruntime":
                    kymaClusterName = environment.parameters["name"]

                    # Check if environment alraedy exists
                    message = "Check if Kyma cluster called " + kymaClusterName + "already exists"

                    command = "btp --format json list accounts/environment-instance --subaccount \"" + subaccountid + "\""

                    result = runCommandAndGetJsonResult(self, command, "INFO", message)

                    envEntry = getKymaEnvironmentInfoByClusterName(result, kymaClusterName)

                    if envEntry is not None:
                        log.info("Kyma environment with name >" + kymaClusterName + "< already exists - Creation skipped")
                        return

                    log.header("Create environment >" + environment.name + "<")

                    envName = environment.name
                    # Fix environment name for instance creation
                    btpEnvironment = "kyma"
                    clusterregion = None
                    parameters = None

                    parameters = dictToString(environment.parameters)

                    envLandscape = selectEnvironmentLandscape(self, environment)

                    # Difference between TRIAL and Prod => Prod has a cluster region, TRIAL has not
                    if environment.plan == "trial":
                        clusterregion = self.region
                    else:
                        clusterregion = environment.parameters["region"]

                    if envLandscape is not None:
                        command = "btp --format json create accounts/environment-instance --subaccount \"" + subaccountid + "\" --environment " + btpEnvironment + \
                            " --service " + environment.name + " --plan " + environment.plan + " --parameters '" + str(
                                parameters) + "' --landscape \"" + envLandscape + "\""
                    else:
                        command = "btp --format json create accounts/environment-instance --subaccount \"" + subaccountid + "\" --environment " + \
                            btpEnvironment + " --service " + \
                            environment.name + " --plan " + environment.plan + \
                            " --parameters '" + str(parameters) + "'"

                    message = "Create " + envName + " environment in cluster region >" + clusterregion + "<"

                    result = runCommandAndGetJsonResult(self, command, "INFO", message)
                else:
                    log.error("the BTP environment >" + environment.name + "< is currently not supported in this script.")
                    sys.exit(os.EX_DATAERR)

        else:
            command = "btp --format json list accounts/environment-instances --subaccount '" + subaccountid + "'"
            result = runCommandAndGetJsonResult(self, command, "INFO", "fetch org name")
            parameters = convertStringToJson(result["environmentInstances"][0]["parameters"])
            self.accountMetadata = addKeyValuePair(accountMetadata, "org", parameters["instance_name"])
            log.header("USING CONFIGURED ENVIRONMENT WITH ID >" + accountMetadata["orgid"] + "<")

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
                command = 'cf create-space "' + cfspacename + '" -o "' + org + '"'
                message = "Create CF space >" + cfspacename + "<"

                runShellCommand(self, command, "INFO", message)

                command = 'cf spaces'
                message = "Check when CF space >" + cfspacename + "< is ready"
                result = try_until_cf_space_done(
                    self, command, message, cfspacename, self.repeatstatusrequest, 120)

                if result == "ERROR":
                    log.error("Something went wrong while waiting for creation of CF space >" + cfspacename + "<")

                log.success("created CF space >" + cfspacename + "<")
                self.accountMetadata = addKeyValuePair(accountMetadata, "cfspacename", cfspacename)
            else:
                log.success("CF space >" + cfspacename + "< already exists")
                self.accountMetadata = addKeyValuePair(accountMetadata, "cfspacename", cfspacename)

            save_collected_metadata(self)

    def assignUsersToSubaccountAndRoles(self):
        assignUsersToSubaccount(self)
        set_all_cf_space_roles(self)
        set_all_cf_org_roles(self)

    def createRoleCollections(self):
        accountMetadata = self.accountMetadata
        subaccountid = accountMetadata["subaccountid"]
        rolecollections = getRoleCollectionsFromUsecaseFile(self)
        admins = getAdminsForUseCase(self)

        for rolecollection in rolecollections:
            rolecollectioname = rolecollection["name"]
            # Check the role collection was not created before
            message = "Check this role collection does not exist >" + rolecollectioname
            command = "btp get security/role-collection '" + rolecollectioname + "'"
            p = runShellCommandFlex(
                self, command, "INFO", message, False, False)
            result = p.stdout.decode()
            if "error: No entity found with values" in result:
                message = "Assign role collection >" + rolecollectioname
                command = "btp create security/role-collection '" + rolecollectioname + \
                    "' --description  '" + rolecollectioname + \
                    "' --subaccount '" + subaccountid + "'"
                runShellCommand(self, command, "INFO", message)
                for role in rolecollection["roles"]:
                    message = "Assign role " + \
                        role["name"] + " to role collection " + \
                        rolecollectioname
                    command = "btp add security/role '" + role["name"] + "' --to-role-collection  '" + rolecollectioname + \
                        "' --of-role-template '" + \
                        role["roletemplate"] + "' --of-app '" + \
                        role["app"] + "' --subaccount '" + subaccountid + "'"
                    runShellCommand(self, command, "INFO", message)

            for userEmail in admins:
                message = "assign user >" + userEmail + \
                    "< the role collection >" + rolecollectioname + "<"
                command = "btp --format json assign security/role-collection \"" + rolecollectioname + \
                    "\" --to-user " + userEmail + \
                    " --create-user-if-missing --subaccount \"" + subaccountid + "\""
                runCommandAndGetJsonResult(
                    self, command, "INFO", message)

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
        self.accountMetadata = track_creation_of_subscriptions_and_services(self)
        save_collected_metadata(self)

        ##################################################################################
        # Now check if service keys should be created
        ##################################################################################
        self.accountMetadata = self.createServiceKeys()
        save_collected_metadata(self)

        btp_assign_role_collection_to_admins(self)

        save_collected_metadata(self)

    def createServiceKeys(self):
        accountMetadata = self.accountMetadata

        if "createdServiceInstances" in accountMetadata and len(accountMetadata["createdServiceInstances"]) > 0:
            log.header("Create service keys if configured")
            for createdService in accountMetadata["createdServiceInstances"]:
                for service in self.definedServices:
                    if service.name == createdService["name"] and service.plan == createdService["plan"] and service.instancename is not None and service.instancename == createdService["instancename"] and "createServiceKeys" in createdService and createdService["createServiceKeys"] is not None:
                        for serviceKey in createdService["createServiceKeys"]:
                            result = get_cf_service_key(self, service.instancename, serviceKey)
                            if "createdServiceKeys" not in createdService:
                                createdService["createdServiceKeys"] = []
                            completeResult = {"keyname": serviceKey, "payload": result}
                            createdService["createdServiceKeys"].append(completeResult)

        return accountMetadata

    def finish(self):
        runTrustFlow(self)

        log.header("SUCCESSFULLY EXECUTED THE USE CASE")
        log.info("checkout your SAP BTP account and how it was setup for the use case")
        log.check("link to your SAP BTP sub account: " + buildUrltoSubaccount(self))

        if self.prunesubaccount is True:
            pruneUseCaseAssets(self)
            pruneSubaccount(self)
        else:
            if self.pruneusecase is True:
                pruneUseCaseAssets(self)

        log.header("SUCCESSFULLY FINISHED USE CASE EXECUTION")
        sys.exit(os.EX_OK)


def assignUsersToSubaccount(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    subaccountid = accountMetadata["subaccountid"]
    admins = getAdminsForUseCase(btpUsecase)

    log.header("Set global account and sub account administrators")
    for userEmail in admins:
        role = "Subaccount Administrator"
        message = "assign user >" + userEmail + "< the role >" + role + "<"
        command = "btp --format json assign security/role-collection \"" + role + "\" --to-user " + \
            userEmail + " --create-user-if-missing --subaccount \"" + subaccountid + "\""
        runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

        role = "Subaccount Service Administrator"
        message = "assign user >" + userEmail + "< the role >" + role + "<"
        command = "btp --format json assign security/role-collection \"" + role + "\" --to-user " + \
            userEmail + " --create-user-if-missing --subaccount \"" + subaccountid + "\""
        runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

        # Do not add user as global admin for Trial accounts
        if btpUsecase.accountMetadata["licenseType"] != "TRIAL":
            role = "Global Account Administrator"
            message = "assign user >" + userEmail + "< the role >" + role + "<"
            # Add user to GA with suffix -ga
            command = "btp --format json assign security/role-collection \"" + \
                role + "\" --to-user " + userEmail + " --create-user-if-missing -ga"
            runCommandAndGetJsonResult(
                btpUsecase, command, "INFO", message)


def set_all_cf_space_roles(btpUsecase: BTPUSECASE):
    environments = btpUsecase.definedEnvironments

    for environment in environments:
        if environment.name == "cloudfoundry":
            admins = getAdminsForUseCase(btpUsecase)

            accountMetadata = btpUsecase.accountMetadata
            log.header("Set all CF space roles")

            org = accountMetadata["org"]
            cfspacename = btpUsecase.cfspacename
            accountMetadata = addKeyValuePair(accountMetadata, "cfspacename", cfspacename)

            spaceRoles = ["SpaceManager", "SpaceDeveloper", "SpaceAuditor"]

            for spaceRole in spaceRoles:
                for admin in admins:
                    message = "Assign space role >" + spaceRole + "< to user >" + admin + "<"
                    command = "cf set-space-role '" + admin + "' '" + \
                        org + "' '" + cfspacename + "' '" + spaceRole + "'"
                    p = runShellCommandFlex(
                        btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + spaceRole + "<")

            save_collected_metadata(btpUsecase)


def set_all_cf_org_roles(btpUsecase: BTPUSECASE):
    environments = btpUsecase.definedEnvironments

    for environment in environments:
        if environment.name == "cloudfoundry":
            admins = getAdminsForUseCase(btpUsecase)

            accountMetadata = btpUsecase.accountMetadata
            log.header("Set all CF org roles")

            org = accountMetadata["org"]

            orgRoles = ["OrgManager", "OrgAuditor"]

            for orgRole in orgRoles:
                for admin in admins:
                    message = "Assign org role >" + orgRole + "< to user >" + admin + "<"
                    command = "cf set-org-role '" + admin + "' '" + org + "' '" + orgRole + "'"
                    p = runShellCommandFlex(
                        btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + orgRole + "<")

            save_collected_metadata(btpUsecase)


def getEnvironmentsForUsecase(btpUsecase: BTPUSECASE, allServices):
    items = []
    environments = []

    paramServicesFile = "libs/json/paramServices.json"
    paramDefinitionServices = getJsonFromFile(None, paramServicesFile)

    for usecaseService in allServices:
        environmentServices = usecaseService.targetenvironment
        if environmentServices not in items and usecaseService.category != "ENVIRONMENT":
            items.append(environmentServices)
            thisUsecaseService = {"name": usecaseService.targetenvironment, "category": "ENVIRONMENT", "plan": "standard"}
            thisEnv = BTPSERVICE(paramDefinitionServices, thisUsecaseService, btpUsecase)
            environments.append(thisEnv)

    for usecaseService in allServices:
        category = usecaseService.category
        name = usecaseService.name
        if category == "ENVIRONMENT" and name not in items:
            items.append(name)
            environments.append(usecaseService)

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
    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)

    items = []
    if "admins" in usecase:
        for admin in usecase["admins"]:
            items.append(admin)
    else:
        log.warning("no admins defined in your use case configuration file (other than you)")

    return items


def check_if_account_can_cover_use_case_for_serviceType(btpUsecase: BTPUSECASE, availableForAccount):

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
            log.warning("the service >" + usecaseServiceName + "< is missing the category key/value in the use case config file. Script will assume that category is >SERVICE<")

        supported = False
        supportedFallbackServicePlan = False

        for accountService in availableForAccount["entitledServices"]:
            accountServiceName = accountService["name"]
            if (accountServiceName == usecaseServiceName):
                for accountServicePlan in accountService["servicePlans"]:
                    accountServicePlanName = accountServicePlan["name"]
#                   accountServicePlanCategory = accountServicePlan["category"]
                    if fallbackServicePlan is not None and accountServicePlanName == fallbackServicePlan:
                        for accountServicePlanDataCenter in accountServicePlan["dataCenters"]:
                            accountServicePlanRegion = accountServicePlanDataCenter["region"]
                            if (accountServicePlanRegion == usecaseRegion):
                                supportedFallbackServicePlan = True
                    if (accountServicePlanName == usecaseServicePlan):
                        for accountServicePlanDataCenter in accountServicePlan["dataCenters"]:
                            accountServicePlanRegion = accountServicePlanDataCenter["region"]
                            if (accountServicePlanRegion == usecaseRegion):
                                supported = True

        if (supported is True):
            log.success("service  >" + usecaseServiceName + "< with plan >" + usecaseServicePlan + "< in region >" + usecaseRegion + "< IS AVAILABLE")
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


def checkIfSubaccountAlreadyExists(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    command = "btp --format json list accounts/subaccount --global-account " + \
        btpUsecase.globalaccount
    result = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", None)

    if "subaccount" in accountMetadata:
        subaccountName = accountMetadata["subaccount"]

        for account in result["value"]:
            if account["displayName"] == subaccountName:
                return account["guid"]
        # If the for loop didn't return any value, the subaccount wasn't found
        return None
    else:
        return None


def save_collected_metadata(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata
    filename = btpUsecase.metadatafile
    saveJsonToFile(filename, accountMetadata)


def getListOfAvailableServicesAndApps(btpUsecase: BTPUSECASE):
    globalaccount = btpUsecase.globalaccount
    usecaseRegion = btpUsecase.region

    command = "btp --format json list accounts/entitlement --global-account \"" + \
        globalaccount + "\""
    message = "Get list of available services and app subsciptions for defined region >" + \
        usecaseRegion + "<"
    result = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", message)

    return result


def get_globalaccount_details(btpUsecase: BTPUSECASE):
    globalaccount = btpUsecase.globalaccount

    log.header("Get accountdetails for your global account with subdomain id >" + globalaccount + "<")
    # Create a new json variable for collected metadata
    metadata = convertStringToJson("{}")

    command = "btp --format json get accounts/global-account --global-account \"" + \
        globalaccount + "\""
    message = "Get global account details for account with subdomain ID >" + globalaccount + "<"

    result = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", message)
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
    command = "btp --format json get accounts/subaccount " + \
        subaccountid + " --global-account " + btpUsecase.globalaccount
    result = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", None)
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


def btp_assign_role_collection_to_admins(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    admins = getAdminsForUseCase(btpUsecase)
    subaccountid = accountMetadata["subaccountid"]

    if admins is not None and len(admins) > 0:
        for appSubscription in btpUsecase.definedAppSubscriptions:
            if appSubscription.requiredrolecollections is not None:
                roleCollections = appSubscription.requiredrolecollections
                for roleCollection in roleCollections:
                    for admin in admins:
                        message = "Assign role collection >" + roleCollection + "< to user >" + admin + "<"
                        command = "btp assign security/role-collection '" + roleCollection + \
                            "' --to-user '" + admin + "' --subaccount '" + subaccountid + "'"
                        runShellCommand(btpUsecase, command, "INFO", message)


def assign_entitlement(btpUsecase: BTPUSECASE, service):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    serviceName = service.name
    servicePlan = service.plan

    command = "btp --format json assign accounts/entitlement \
    --to-subaccount \"" + subaccountid + "\" \
    --for-service \"" + serviceName + "\" \
    --plan \"" + servicePlan + "\""

    if service.amount is not None and service.amount > 0:
        command = command + " --auto-distribute-amount " + \
            str(service.amount) + " --amount " + str(service.amount)
    else:
        command = command + " --distribute --enable"

    message = "Assign entitlement for >" + \
        serviceName + "< and plan >" + servicePlan + "<"
    # Run script, but don't exit, if not successfull
    p = runShellCommandFlex(btpUsecase, command,
                            "INFO", message, False, False)
    returnCode = p.returncode

    if returnCode != 0:
        log.warning("this entitlement wasn't sucesssfull. Trying to entitle with amount parameter instead.")
        command = "btp --format json assign accounts/entitlement \
        --to-subaccount \"" + subaccountid + "\" \
        --for-service \"" + serviceName + "\" \
        --plan \"" + servicePlan + "\""

        if service.amount is not None and service.amount > 0:
            command = command + " --auto-distribute-amount " + \
                str(service.amount) + " --amount " + str(service.amount)
        else:
            command = command + " --auto-distribute-amount " + str(service.amount) + " --amount " + str(service.amount)

        message = "Try again to assign entitlement for >" + serviceName + \
            "< and plan >" + servicePlan + "< with amount parameter set to 1."
        p = runShellCommand(btpUsecase, command, "INFO", message)
        returnCode = p.returncode

    return returnCode


def subscribe_app_to_subaccount(btpUsecase: BTPUSECASE, app, plan):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    command = "btp subscribe accounts/subaccount \
    --subaccount \"" + subaccountid + "\" \
    --to-app \"" + app + "\" \
    --plan \"" + plan + "\""

    isAlreadySubscribed = checkIfAppIsSubscribed(btpUsecase, app, plan)
    if isAlreadySubscribed is False:
        message = "subscribe sub account to >" + app + "< and plan >" + plan + "<"
        runShellCommand(btpUsecase, command, "INFO", message)
    else:
        log.info("subscription already there for >" + app + "< and plan >" + plan + "<")


def checkIfAppIsSubscribed(btpUsecase: BTPUSECASE, appName, appPlan):
    result = False
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    command = "btp --format json get accounts/subscription --subaccount " + \
        subaccountid + " --of-app " + appName + " --plan " + appPlan
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
        if not any(d.name == thisName and d.plan == thisPlan for d in entitlements):
            entitlements.append(service)

    # Now set the amount for the entitlement right
    # Simply sum-up all amounts to one amount per name/plan combination
    for entitlement in entitlements:
        amount = 0
        thisName = service.name
        thisPlan = service.plan
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

    command = "btp --format json list accounts/subscription --subaccount \"" + \
        subaccountid + "\""
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

    command = "btp --format json list accounts/subscription --subaccount \"" + \
        subaccountid + "\""
    message = "subscription status of >" + app_name + "<"
    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
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
    command = "btp --format json list accounts/subscription --subaccount " + btpUsecase.subaccountid
    resultCommand = runCommandAndGetJsonResult(btpUsecase, command, "INFO", "check status of app subscriptions")

    allSubscriptionsAvailable = True
    for thisJson in resultCommand["applications"]:
        name = thisJson["appName"]
        plan = thisJson["planName"]
        status = thisJson["state"]
        tenantId = thisJson["tenantId"]
        for app in btpUsecase.definedAppSubscriptions:
            if app.name == name and app.plan == plan and app.successInfoShown is False:
                if status == "SUBSCRIBE_FAILED":
                    log.error("BTP account reported that subscription on >" + app.name + "< has failed.")
                    sys.exit(os.EX_DATAERR)

                if status != "SUBSCRIBED":
                    allSubscriptionsAvailable = False
                    app.status = status
                    app.successInfoShown = False
                    app.statusResponse = thisJson
                else:
                    log.success("subscription to app >" + app.name + "< (plan " + app.plan + ") is now available")
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
            areAllInstancesCreated = checkIfAllServiceInstancesCreated(btpUsecase)

        if len(btpUsecase.definedAppSubscriptions) > 0:
            areAllSubscriptionsCreated = checkIfAllSubscriptionsAreAvailable(btpUsecase)

        if (areAllInstancesCreated is True and areAllSubscriptionsCreated is True):
            log.success("All service instances and subscriptions are now available".upper())
            accountMetadata = addCreatedServicesToMetadata(btpUsecase)
            return accountMetadata

        search_every_x_seconds = determineTimeToFetchStatusUpdates(btpUsecase)
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds

    log.error("Could not get all services and/or app subscriptions up and running. Sorry.")


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
            thisService = convertStringToJson(json.dumps(service, indent=4, cls=BTPSERVICEEncoder))
            accountMetadata["createdAppSubscriptions"].append(thisService)

    if len(btpUsecase.definedServices) > 0:
        for service in btpUsecase.definedServices:
            thisService = convertStringToJson(json.dumps(service, indent=4, cls=BTPSERVICEEncoder))
            accountMetadata["createdServiceInstances"].append(thisService)

    # if "createdAppSubscriptions" in accountMetadata:
    #     for service in accountMetadata["createdAppSubscriptions"]:
    #         if "status" in service:
    #             del service.status

    # if "createdServiceInstances" in accountMetadata:
    #     for service in accountMetadata["createdServiceInstances"]:
    #         if service.successInfoShown is not None:
    #             del service.successInfoShown
    #         if service.repeatstatusrequest is not None:
    #             del service.repeatstatusrequest
    #         if service.repeatstatustimeout is not None:
    #             del service.repeatstatustimeout
    #         if service.status is not None:
    #             del service.status

    return accountMetadata


def checkConfigurationInfo(btpUsecase: BTPUSECASE):

    checkEmailsinUsecaseConfig(btpUsecase)


def getListOfUsersOnAccount(btpUsecase: BTPUSECASE):
    result = None

    command = "btp --format json list security/user"
    result = runCommandAndGetJsonResult(
        btpUsecase, command, "INFO", None)

    return result


def getAdminsForUseCase(btpUsecase: BTPUSECASE):
    licenseType = None
    result = []
    myUser = btpUsecase.myemail

    licenseType = btpUsecase.accountMetadata["licenseType"]

    if licenseType != "TRIAL":
        for admin in btpUsecase.admins:
            email = admin
            result.append(email)

    result.append(myUser)
    # remove duplicates in admins list
    result = list(dict.fromkeys(result))

    return result


def getRoleCollectionsFromUsecaseFile(btpUsecase: BTPUSECASE):
    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if "requiredrolecollections" in usecase:
        for rolecollection in usecase["requiredrolecollections"]:
            items.append(rolecollection)
    else:
        log.info("no role collections defined in your use case configuration file")

    return items


def build_admins_list(btpUsecase: BTPUSECASE):
    admins = getAdminsForUseCase(btpUsecase)
    # Remove duplicates
    admins = list(dict.fromkeys(admins))
    result = "["

    for admin in admins:
        if admin == admins[-1]:
            result += '"' + admin + '"]'
        else:
            result += '"' + admin + '" , '

    return result


def getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase: BTPUSECASE):
    allEmails = None
    adminsList = btpUsecase.admins

    # Create a copy of the usecase, as we might have to remove pieces prior the analysis
    thisUsecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)

    # Remove the use case author from the usecase to be analyzed
    if "aboutThisUseCase" in thisUsecase and "author" in thisUsecase["aboutThisUseCase"]:
        del thisUsecase["aboutThisUseCase"]["author"]

    # Convert the usecase dict to a string to detect any other email-adresses added in other parameters of the file
    usecaseString = dictToString(thisUsecase)
    allEmails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', usecaseString)

    # Before checking all other email addresses, remove from the result all the email addresses that already have been covered in the admins section
    for admin in adminsList:
        if admin in allEmails:
            allEmails.remove(admin)

    return allEmails


def checkEmailsinUsecaseConfig(btpUsecase: BTPUSECASE):
    allowedUsers = getListOfUsersOnAccount(btpUsecase)
    foundError = False

    adminsList = getAdminsForUseCase(btpUsecase)

    for admin in adminsList:
        if admin in allowedUsers:
            log.success("user >" + admin + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
        else:
            log.warning("user >" + admin + "< (defined in admins section of file >" + btpUsecase.usecasefile + "<) has no access to this global account")

    emailAddresses = getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase)

    # Now we can run the email check for the other email addresses
    for emailAddress in emailAddresses:
        if emailAddress in allowedUsers:
            log.success("user >" + emailAddress + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
        else:
            log.warning("email address >" + emailAddress + "< was found in the usecase definition, but that user has no access to this global account. Please check!")
    if foundError is True:
        log.error("Can't move on with the use case, before the errors above are not fixed")
        sys.exit(os.EX_DATAERR)

    return None


def pruneSubaccount(btpUsecase: BTPUSECASE):
    accountMetadata = btpUsecase.accountMetadata

    command = "btp --format json delete accounts/subaccount " + accountMetadata["subaccountid"] + " --global-account " + btpUsecase.globalaccount + " --confirm"
    message = "Delete sub account"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    search_every_x_seconds = btpUsecase.repeatstatusrequest
    usecaseTimeout = btpUsecase.repeatstatustimeout

    current_time = 0
    while usecaseTimeout > current_time:
        command = "btp --format json list accounts/subaccount"
        message = "Check if account deleted"
        result = runCommandAndGetJsonResult(btpUsecase, command, "CHECK", message)
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
            command = "btp --format json unsubscribe accounts/subaccount --subaccount " + accountMetadata["subaccountid"] + " --from-app " + service["name"] + " --confirm"
            message = "Remove app subscription >" + service["name"] + "< from subaccount"
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
                    log.success("app subscription for app >" + service["name"] + "< now deleted")
                    service["deletionStatus"] = "deleted"
                if (status == "UNSUBSCRIBE_FAILED"):
                    log.error("unsubscribing app >" + service["name"] + "< failed. Returned status >" + status + "<")
                    service["deletionStatus"] = "UNSUBSCRIBE_FAILED"
                    log.info("trying again to remove the subscription to app >" + service["name"] + "<")
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
        # login_cf(btpUsecase)
        # Initiate deletion of service instances
        for environment in btpUsecase.definedEnvironments:
            if environment.name == "cloudfoundry":
                for service in accountMetadata["createdServiceInstances"]:
                    if "createdServiceKeys" in service:
                        for key in service["createdServiceKeys"]:
                            delete_cf_service_key(btpUsecase, service["instancename"], key["keyname"])
                        search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(btpUsecase, service)
                        current_time = 0
                        while usecaseTimeout > current_time:
                            command = "cf service-key " + service["instancename"] + " " + key["keyname"]
                            # Calling the command with the goal to get back the "FAILED" status, as this means that the service key was not found (because deletion was successfull)
                            # If the status is not "FAILED", this means that the deletion hasn't been finished so far
                            message = "check if service key >" + key["keyname"] + "< for service instance >" + service["instancename"] + "<"
                            p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
                            result = p.stdout.decode()
                            if "FAILED" in result:
                                usecaseTimeout = current_time - 1
                            time.sleep(search_every_x_seconds)
                            current_time += search_every_x_seconds
                    if "instancename" in service and service["instancename"] is not None and service["instancename"] != "":
                        command = "cf delete-service " + '"' + service["instancename"] + '"' + " -f"
                        message = "Delete CF service instance >" + service["instancename"] + "< from subaccount"
                        result = runShellCommand(btpUsecase, command, "INFO", message)

                log.info("Check deletion status for service instances")

                # check status of deletion
                search_every_x_seconds = btpUsecase.repeatstatusrequest
                usecaseTimeout = btpUsecase.repeatstatustimeout
                current_time = 0
                allServicesDeleted = False
                # Set the deletion status to "not deleted"
                for service in accountMetadata["createdServiceInstances"]:
                    service["deletionStatus"] = "not deleted"

                while usecaseTimeout > current_time and allServicesDeleted is False:
                    for service in accountMetadata["createdServiceInstances"]:
                        if "instancename" not in service:
                            status = "deleted"
                            service["deletionStatus"] = status
                            log.info("no service instance available for service >" + service["name"] + "<. Deletion not needed.")
                            continue
                        status = get_cf_service_deletion_status(btpUsecase, service)
                        if (status == "deleted"):
                            log.success("service instance >" + service["instancename"] + "< for service >" + service["name"] + "< now deleted.")
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

            if environment.name == "kymaruntime":
                # Get Kyma runtime ID
                message = "Get Kyma environment ID for subaccount > " + \
                    btpUsecase.accountMetadata["subaccountid"] + " < by name > " + \
                    btpUsecase.accountMetadata["subaccountid"] + " <"
                command = "btp --format json list accounts/environment-instance --subaccount \"" + \
                    btpUsecase.accountMetadata["subaccountid"] + "\""

                result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

                kymaEnvironmentID = getKymaEnvironmentIdByClusterName(result, environment.parameters["name"])

                # Delete Kyma runtime via SAP btp CLI
                message = "Trigger deletion of Kyma environment > " + \
                    environment.parameters["name"] + \
                    " < in subaccount > " + \
                    btpUsecase.accountMetadata["subaccountid"] + " <"

                command = "btp --format json delete accounts/environment-instance " + kymaEnvironmentID + \
                    " --subaccount \"" + \
                    btpUsecase.accountMetadata["subaccountid"] + "\"" + " --confirm"

                result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

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
                    command = "btp --format json list accounts/environment-instance --subaccount \"" + \
                        btpUsecase.accountMetadata["subaccountid"] + "\""

                    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

                    kymaEnvironmentID = getKymaEnvironmentIdByClusterName(result, environment.parameters["name"])

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

    message = "Check for available environment landscapes in subaccount >" + subaccountid + "< and region >" + region + "<"
    command = "btp --format json list accounts/available-environment --subaccount \"" + \
        subaccountid + "\""

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
