from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperLog import initLogger
from libs.python.helperCommandExecution import login_btp, runCommandAndGetJsonResult
from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperJson import getJsonFromFile
from libs.python.helperJsonSchemas import getJsonSchemaDefsContent
import logging
import sys
import os

log = logging.getLogger(__name__)

CATEGORIES = {}
CATEGORIES["SERVICE"] = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"]
CATEGORIES["APPLICATION"] = ["APPLICATION"]
CATEGORIES["ENVIRONMENT"] = ["ENVIRONMENT"]


class BTPUSECASE_GEN:
    def __init__(self):
        self.myemail = getEnvVariableValue("BTPSA_PARAM_MYEMAIL")
        self.mypassword = getEnvVariableValue("BTPSA_PARAM_MYPASSWORD")
        self.globalaccount = getEnvVariableValue("BTPSA_PARAM_GLOBALACCOUNT")
        self.templatefoler = "./"
        self.btpcliapihostregion = "eu10"
        self.loginmethod = "basicAuthentication"
        self.logcommands = False
        self.region = "us10"
        self.envvariables = None
        self.logfile = "./log/generator.log"
        self.metadatafile = "./log/generator_metadata.json"

        initLogger(self)

        if self.myemail is None:
            log.error("missing email address")
            sys.exit(os.EX_DATAERR)

        if self.mypassword is None:
            log.error("missing your BTP password")
            sys.exit(os.EX_DATAERR)

        if self.globalaccount is None:
            log.error("missing your BTP globalaccount subdomain id")
            sys.exit(os.EX_DATAERR)

    def fetchEntitledServiceList(self, updateServiceData, mainDataJsonFile):

        if updateServiceData:
            login_btp(self)

            globalaccount = self.globalaccount
            usecaseRegion = self.region
            command = "btp --format json list accounts/entitlement --global-account '" + globalaccount + "'"
            message = "Get list of available services and app subsciptions for defined region >" + usecaseRegion + "<"
            temp = runCommandAndGetJsonResult(self, command, "INFO", message)

            del temp["assignedServices"]
            temp = temp["entitledServices"]
            result = convertToServiceListByCategory(temp)

            self.entitledServices = {"btpservicelist": result}
            addSchemaInfoToServiceList(self)
            addNumSection(self)
        else:
            temp = getJsonFromFile(None, mainDataJsonFile)
            self.entitledServices = temp

    def applyServiceListOnTemplate(self, templateFile, targetFilename):

        serviceList = self.entitledServices
        renderTemplateWithJson(templateFile, targetFilename, serviceList)
        log.success("applied SAP BTP service list on template file >" + templateFile + "< and created the target file >" + targetFilename + "<")


def addNumSection(btpusecase_gen):
    buildEnums(btpusecase_gen.entitledServices)


def addSchemaInfoToServiceList(btpusecase_gen):
    entitledServices = btpusecase_gen.entitledServices

    defsContent = getJsonSchemaDefsContent()

    for defBlock in defsContent:
        for category in entitledServices.get("btpservicelist"):
            for service in category.get("list"):
                # defBlockCategory = defBlock.get("category")
                defBlockServiceName = defBlock.get("name")
                serviceName = service.get("name")
                if defBlockServiceName == serviceName:
                    for thisDefBlock in defBlock.get("defs"):
                        if thisDefBlock.get("ref-level") == "plan":
                            for plan in service.get("servicePlans"):
                                if plan.get("name") == thisDefBlock.get("ref-value"):
                                    if not service.get("jsonSchemaDefs"):
                                        service["jsonSchemaDefs"] = []
                                    service["jsonSchemaDefs"].append(thisDefBlock)


def convertToServiceListByCategory(rawData):

    result = []
    for category in CATEGORIES:
        list = {"name": category + "S", "list": getBtpCategory(category, rawData)}
        result.append(list)

    return result


def getBtpCategory(category, rawData):

    services = None

    if category in CATEGORIES["SERVICE"]:
        services = getServicesForCategory("SERVICE", rawData)
    if category in CATEGORIES["APPLICATION"]:
        services = getServicesForCategory("APPLICATION", rawData)
    if category in CATEGORIES["ENVIRONMENT"]:
        services = getServicesForCategory("ENVIRONMENT", rawData)
    if services is None:
        log.error("the category >" + category + "< can't be assigned to one of the defined service categories")

    return services


def getServicesForCategory(category, rawData):
    result = []

    for service in rawData:
        servicePlans = getServicePlansForCategory(service, category)
        if servicePlans:
            thisService = getBtpService(service, servicePlans)
            addAdditionalMetadata(thisService, service)

            result.append(thisService)
    sortedResult = sorted(result, key=lambda d: (d['name'].lower()), reverse=False)

    return sortedResult


def getBtpService(rawData, servicePlans):
    name = rawData["name"]
    displayName = rawData.get("displayName")
    description = rawData.get("description")
    iconBase64 = rawData.get("iconBase64")
    servicePlans = servicePlans
    result = {"name": name, "displayName": displayName, "description": description, "iconBase64": iconBase64, "servicePlans": servicePlans}
    return result


def getServicePlansForCategory(service, category):
    result = []

    for plan in service.get("servicePlans"):
        thisCategory = plan.get("category")
        if thisCategory in CATEGORIES.get(category):
            result.append(getBtpServicePlan(plan))
    return result


def getBtpServicePlan(rawData):
    name = rawData.get("name")
    displayName = rawData.get("displayName")
    description = rawData.get("description")
    uniqueIdentifier = rawData.get("uniqueIdentifier")
    category = rawData.get("category")
    dataCenters = []

    for plan in rawData.get("dataCenters"):
        dataCenters.append(getBtpDataCenter(plan))

    dataCenters = sorted(dataCenters, key=lambda d: d['region'], reverse=False)

    result = {"name": name, "displayName": displayName, "description": description, "uniqueIdentifier": uniqueIdentifier, "category": category, "dataCenters": dataCenters}
    return result


def getBtpDataCenter(rawData):
    result = {}

    result["name"] = rawData.get("name")
    result["displayName"] = rawData.get("displayName")
    result["region"] = rawData.get("region")
    result["environment"] = rawData.get("environment")
    result["provisioningServiceUrl"] = rawData.get("provisioningServiceUrl")
    result["saasRegistryServiceUrl"] = rawData.get("saasRegistryServiceUrl")
    result["domain"] = rawData.get("domain")
    result["geoAccess"] = rawData.get("geoAccess")

    return result


def buildEnums(accountEntitlements):

    enumList = []

    for category in accountEntitlements.get("btpservicelist"):
        for service in category.get("list"):
            for servicePlan in service.get("servicePlans"):
                for accountServicePlanDataCenter in servicePlan["dataCenters"]:
                    accountServicePlanRegion = accountServicePlanDataCenter["region"]
                    enumList.append(accountServicePlanRegion)

    enumList.sort()
    enumList = list(dict.fromkeys(enumList))
    accountEntitlements["btpenums"] = {}
    accountEntitlements["btpenums"]["regions"] = enumList


def addAdditionalMetadata(serviceResult, serviceDataRaw):

    appCoordinates = serviceDataRaw.get("applicationCoordinates")

    if appCoordinates:
        # Fetch icon format
        serviceResult["iconFormat"] = appCoordinates.get("iconFormat")

        # Fetch service ids
        if appCoordinates.get("inventoryIds"):
            ids=[]
            for theseIds in appCoordinates.get("inventoryIds"):
                if theseIds:
                    if type(theseIds) == str:
                        ids.append(theseIds.get("key"))
                    if type(theseIds) == list:
                        for id in theseIds:
                            ids.append(id.get("key"))
            if ids and len(ids) > 0:
                serviceResult["serviceIds"] = ids

        # Fetch links
        if appCoordinates.get("serviceDescription"):
            serviceResult["links"] = appCoordinates.get("serviceDescription")

        # Fetch service categories
        if appCoordinates.get("serviceCategories"):
            serviceResult["serviceCategories"] = []
            for thisCategory in appCoordinates.get("serviceCategories"):
                serviceResult["serviceCategories"].append(thisCategory.get("name"))

    # Fetch business categories
    if serviceDataRaw.get("businessCategories"):
        serviceResult["businessCategories"] = []
        for thisCategory in serviceDataRaw.get("businessCategories"):
            serviceResult["serviceCategories"].append(thisCategory.get("displayName"))
