from libs.python.helperJson import dictToJson
from libs.python.helperJinja2 import renderTemplateWithJson
import logging

log = logging.getLogger(__name__)


def getDataForJsonSchemaTemplate(accountEntitlements):

    enumServiceList = buildEnumForServices(accountEntitlements)
    enumPlanList = buildEnumForServicePlans(accountEntitlements)
    enumDatacenterList = buildEnumForDatacenters(accountEntitlements)
    serviceStructure = buildServiceStructure(accountEntitlements)
    servicePlanStructure = buildServiceStructure(accountEntitlements)
    categoryStructure = buildCategoryStructure(accountEntitlements)

    result = {"enumServiceList": enumServiceList, "enumPlanList": enumPlanList, "enumDatacenterList": enumDatacenterList, "services": serviceStructure, "servicePlans": servicePlanStructure, "categoryStructure": categoryStructure}

    return result


def getServicesForCategories(categories, data):
    thisList = []
    for service in data.get("entitledServices"):
        serviceName = service.get("name")
        for servicePlan in service.get("servicePlans"):
            category = servicePlan.get("category")
            if category in categories and serviceName not in thisList:
                thisList.append(serviceName)
    thisList = sorted(thisList, key=str.casefold)
    thisList = list(dict.fromkeys(thisList))
    return thisList


def buildCategoryStructure(accountEntitlements):

    list = []
    services_SERVICE = getServicesForCategories(["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"], accountEntitlements)
    services_APPLICATION = getServicesForCategories(["APPLICATION"], accountEntitlements)
    services_ENVIRONMENT = getServicesForCategories(["ENVIRONMENT"], accountEntitlements)

    list.append({"categoryName": "SERVICE", "services": services_SERVICE})
    list.append({"categoryName": "APPLICATION", "services": services_APPLICATION})
    list.append({"categoryName": "ENVIRONMENT", "services": services_ENVIRONMENT})

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
        myService = {"serviceName": serviceName, "servicePlans": theseServicePlans}
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
        myPlan = {"planName": plan, "services": theseServices}
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


def buildJsonSchemaFile(TEMPLATE_FILE, TARGET_FILE, accountEntitlements):
    data = getDataForJsonSchemaTemplate(accountEntitlements)

    templateFilename = TEMPLATE_FILE
    targetFilename = TARGET_FILE

    renderTemplateWithJson(templateFilename, targetFilename, data)
