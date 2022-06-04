from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperLog import initLogger
from libs.python.helperCommandExecution import login_btp, runCommandAndGetJsonResult
from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperFolders import FOLDER_BTPBASE_TEMPLATES
import logging
import sys
import os

log = logging.getLogger(__name__)


def getBtpCategory(category, rawData):
    categoriesServices = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"]
    categoriesApplications = ["APPLICATION"]
    categoriesEnvironments = ["ENVIRONMENT"]

    result = None

    if category in categoriesServices:
        services = getServicesForCategory(categoriesServices, rawData)
        result = {"name": "SERVICE", "services": services}
    if category in categoriesApplications:
        services = getServicesForCategory(categoriesApplications, rawData)
        result = {"name": "APPLICATION", "services": services}
    if category in categoriesEnvironments:
        services = getServicesForCategory(categoriesEnvironments, rawData)
        result = {"name": "ENVIRONMENT", "services": services}
    if result is None:
        log.error("the category >" + category + "< can't be assigned to one of the defined service categories")
        sys.exit(os.EX_DATAERR)
    return result


def getBtpService(rawData, servicePlans):
    name = rawData["name"]
    displayName = rawData.get("displayName")
    description = rawData.get("description")
    iconBase64 = rawData.get("iconBase64")
    servicePlans = servicePlans
    result = {"name": name, "displayName": displayName, "description": description, "iconBase64": iconBase64, "servicePlans": servicePlans}
    return result


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

    def fetchEntitledServiceList(self):
        login_btp(self)

        globalaccount = self.globalaccount
        usecaseRegion = self.region

        command = "btp --format json list accounts/entitlement --global-account '" + globalaccount + "'"
        message = "Get list of available services and app subsciptions for defined region >" + usecaseRegion + "<"
        temp = runCommandAndGetJsonResult(self, command, "INFO", message)

        del temp["assignedServices"]
        temp = temp["entitledServices"]
        temp = sorted(temp, key=lambda d: d['name'], reverse=False)

        result = convertToServiceListByCategory(temp)
        self.entitledServices = {"btpservicelist": result}

    def applyServiceListOnTemplate(self, targetFilename, templateFile):

        serviceList = self.entitledServices
        renderTemplateWithJson(FOLDER_BTPBASE_TEMPLATES, templateFile, targetFilename, serviceList)
        log.success("applied SAP BTP service list on template file >" + templateFile + "< and created the target file >" + targetFilename + "<")


def convertToServiceListByCategory(rawData):
    listOfCategories = ["SERVICE", "APPLICATION", "ENVIRONMENT"]

    result = []
    for category in listOfCategories:
        list = {"name": category, "list": getBtpCategory(category, rawData)}
        result.append(list)

    return result


def getServicesForCategory(categories, rawData):
    result = []

    for category in categories:
        for service in rawData:
            servicePlans = getServicePlansForCategory(service, category)
            if servicePlans:
                thisService = getBtpService(service, servicePlans)
                result.append(thisService)
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


def getBtpServicePlan(rawData):
    name = rawData.get("name")
    displayName = rawData.get("displayName")
    description = rawData.get("description")
    uniqueIdentifier = rawData.get("uniqueIdentifier")
    category = rawData.get("category")
    dataCenters = []

    for plan in rawData.get("dataCenters"):
        dataCenters.append(getBtpDataCenter(plan))

    result = {"name": name, "displayName": displayName, "description": description, "uniqueIdentifier": uniqueIdentifier, "category": category, "dataCenters": dataCenters}
    return result


def getServicePlansForCategory(service, category):
    result = []

    for plan in service.get("servicePlans"):
        thisCategory = plan.get("category")
        if thisCategory == category:
            result.append(getBtpServicePlan(plan))
    return result
