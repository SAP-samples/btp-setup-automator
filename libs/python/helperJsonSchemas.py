from libs.python.helperJson import dictToJson, getJsonFromFile
from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperFolders import FOLDER_SCHEMA_LIBS, FOLDER_SCHEMA_TEMPLATES

import logging
import glob

log = logging.getLogger(__name__)


def getDataForJsonSchemaTemplate(accountEntitlements):

    enumServiceList = buildEnumForServices(accountEntitlements)
    enumPlanList = buildEnumForServicePlans(accountEntitlements)
    enumDatacenterList = buildEnumForDatacenters(accountEntitlements)
    serviceStructure = buildServiceStructure(accountEntitlements)
    categoryStructure = buildCategoryStructure(accountEntitlements)

    defsContent = getJsonSchemaDefsContent()

    jsonSchemaDefs = retrieveJsonSchemaDefs(defsContent)

    result = {"enumServiceList": enumServiceList, "enumPlanList": enumPlanList, "enumDatacenterList": enumDatacenterList, "services": serviceStructure, "categoryStructure": categoryStructure, "jsonSchemaDefs": jsonSchemaDefs}

    return result


def removeNonPrintableChars(myString):
    if myString:
        filtered_characters = list(s for s in myString if s.isprintable())
        myString = ''.join(filtered_characters)
    return myString


def getServicesForCategories(categories, data):
    thisList = []
    listOfServices = []
    for service in data.get("entitledServices"):
        serviceName = service.get("name")
        for servicePlan in service.get("servicePlans"):
            category = servicePlan.get("category")
            if category in categories and serviceName not in listOfServices:
                listOfServices.append(serviceName)
                plans = getPlansForService(serviceName, data)
                description = removeNonPrintableChars(service.get("description"))
                displayName = removeNonPrintableChars(service.get("displayName"))
                myService = {"name": serviceName, "displayName": displayName, "description": description, "plans": plans}
                thisList.append(myService)
    if thisList:
        thisList = sorted(thisList, key=lambda k: k['name'], reverse=False)

    thisList = addJsonSchemaServiceParameters(thisList)

    return thisList


def getPlansForService(serviceName, data):
    result = []
    for service in data.get("entitledServices"):
        thisServiceName = service["name"]
        if thisServiceName == serviceName:
            listOfServicePlans = []
            for servicePlan in service.get("servicePlans"):
                servicePlanName = servicePlan.get("name")
                if servicePlanName not in listOfServicePlans:
                    listOfServicePlans.append((servicePlanName))
                    dcs = []
                    for datacenter in servicePlan.get("dataCenters"):
                        dataCenterInfo = datacenter.get("region") + " - " + datacenter.get("displayName")
                        dcs.append(dataCenterInfo)
                    dcs = sorted(dcs, reverse=False)
                    thisPlan = {"name": servicePlanName, "dataCenters": dcs}
                    result.append(thisPlan)
            result = sorted(result, key=lambda k: k['name'], reverse=False)
    return result


def buildCategoryStructure(accountEntitlements):

    list = []
    services_SERVICE = getServicesForCategories(["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"], accountEntitlements)
    services_APPLICATION = getServicesForCategories(["APPLICATION"], accountEntitlements)
    services_ENVIRONMENT = getServicesForCategories(["ENVIRONMENT"], accountEntitlements)

    list.append({"name": "SERVICE", "services": services_SERVICE})
    list.append({"name": "APPLICATION", "services": services_APPLICATION})
    list.append({"name": "ENVIRONMENT", "services": services_ENVIRONMENT})

    return list


def buildServiceStructure(accountEntitlements):

    enumList = []
    for service in accountEntitlements.get("entitledServices"):
        serviceName = service["name"]
        theseServicePlans = []
        for servicePlan in service.get("servicePlans"):
            servicePlanName = servicePlan.get("name")
            theseServicePlans.append(servicePlanName)
        theseServicePlans.sort()
        theseServicePlans = list(dict.fromkeys(theseServicePlans))
        myService = {"name": serviceName, "plans": theseServicePlans}
        enumList.append(myService)

    return enumList


def buildServicPlanStructure(accountEntitlements):

    servicePlans = buildEnumForServicePlans(accountEntitlements)

    enumList = []
    for plan in servicePlans:
        for service in accountEntitlements.get("entitledServices"):
            theseServices = []
            for thisServicePlan in service.get("servicePlans"):
                servicePlanName = thisServicePlan.get("name")
                if servicePlanName == plan:
                    theseServices.append(service["name"])
        myPlan = {"name": plan, "services": theseServices}
        enumList.append(myPlan)

    return enumList


def buildEnumForServicePlans(accountEntitlements):

    enumPlanList = []
    for service in accountEntitlements.get("entitledServices"):
        for servicePlan in service.get("servicePlans"):
            servicePlanName = servicePlan.get("name")
            enumPlanList.append(servicePlanName)

    enumPlanList.sort()
    enumPlanList = list(dict.fromkeys(enumPlanList))
    enumPlanList = dictToJson(enumPlanList)
    return enumPlanList


def buildEnumForServices(accountEntitlements):

    enumServiceList = []
    for service in accountEntitlements.get("entitledServices"):
        serviceName = service["name"]
        enumServiceList.append(serviceName)

    enumServiceList.sort()
    enumServiceList = list(dict.fromkeys(enumServiceList))
    enumServiceList = dictToJson(enumServiceList)

    return enumServiceList


def buildEnumForDatacenters(accountEntitlements):

    enumList = []

    for service in accountEntitlements.get("entitledServices"):
        for servicePlan in service.get("servicePlans"):
            for accountServicePlanDataCenter in servicePlan["dataCenters"]:
                accountServicePlanRegion = accountServicePlanDataCenter["region"]
                enumList.append(accountServicePlanRegion)

    enumList.sort()
    enumList = list(dict.fromkeys(enumList))
    enumList = dictToJson(enumList)

    return enumList


def buildJsonSchemaFile(TEMPLATE_FILE, targetFilename, accountEntitlements):
    data = getDataForJsonSchemaTemplate(accountEntitlements)

    templateFilename = TEMPLATE_FILE
    targetFile = FOLDER_SCHEMA_LIBS + targetFilename

    renderTemplateWithJson(FOLDER_SCHEMA_TEMPLATES, templateFilename, targetFile, data)


def getJsonSchemaDefsContent():
    folderParameterFiles = FOLDER_SCHEMA_TEMPLATES + "parameters/"

    result = []

    for filename in glob.iglob(folderParameterFiles + '**/*.json', recursive=True):
        content = getJsonFromFile(None, filename)
        result.append(content)

    return result


def retrieveJsonSchemaDefs(contents):

    result = []
    for content in contents:
        defs = content.get("defs")
        for thisDef in defs:
            name = thisDef.get("def-name")
            struct = thisDef.get("def-structure")
            thisResult = {}
            thisResult["name"] = name
            thisResult["value"] = struct
            result.append(thisResult)

    return result


def addJsonSchemaServiceParameters(servicesList):

    folderParameterFiles = FOLDER_SCHEMA_TEMPLATES + "parameters/"

    for filename in glob.iglob(folderParameterFiles + '**/*.json', recursive=True):
        content = getJsonFromFile(None, filename)
        category = content.get("category")
        name = content.get("name")
        plan = content.get("plan")

        for thisService in servicesList:
            thisServiceCategory = thisService.category
            thisServiceName = thisService.name
            thisServicePlan = thisService.plan

    return servicesList
