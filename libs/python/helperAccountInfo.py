import logging
import os
from libs.python.helperCommandExecution import runCommandAndGetJsonResult

log = logging.getLogger(__name__)


def getServiceInfo(btpUsecase):
    usecaseRegion = btpUsecase.region

    command = "btp --format json list accounts/entitlement --global-account '" + btpUsecase.globalaccount + "'"
    message = "Get list of available services and app subsciptions for defined region >" + usecaseRegion + "<"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

    return result


def getAllDatacenters(services):
    resultCF = []

    for service in services:
        for plan in service["servicePlans"]:
            for dataCenter in plan["dataCenters"]:
                if dataCenter["name"] not in resultCF:
                    resultCF.append(dataCenter["name"])
    return resultCF


def getDataCenterFromService(service):
    result = []
    for plan in service["servicePlans"]:
        for dataCenter in plan["dataCenters"]:
            if dataCenter["name"] not in result:
                result.append(dataCenter["name"])
    result.sort()
    return result


def createCSVForEntitledServicesInDatacenters(btpUsecase, foldername, data):
    filename = foldername + "info_datacenter_coverage_" + btpUsecase.globalaccount + ".csv"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    dcsCF = getAllDatacenters(data["entitledServices"])
    string = "Service;Description;"
    for dc in dcsCF:
        string += dc + ";"
    string += "\n"

    result = []
    for entitledService in data["entitledServices"]:
        string += entitledService["name"] + ";" + entitledService["displayName"] + ";"
        serviceDCs = getDataCenterFromService(entitledService)
        myService = {"name": entitledService["name"]}
        for dc in dcsCF:
            if dc in serviceDCs:
                myService[dc] = "X"
                string += "X;"
            else:
                myService[dc] = ""
                string += ";"
        result.append(myService)
        string += "\n"
    text_file = open(filename, "w")
    text_file.write(string)
    text_file.close()


def createInfoPackage(btpUsecase):
    data = getServiceInfo(btpUsecase)

    createCSVForEntitledServicesInDatacenters(btpUsecase, "logs/", data)
    createCSVServices(btpUsecase, "logs/", data)


def createCSVServices(btpUsecase, foldername, data):
    filename = foldername + "info_services_" + btpUsecase.globalaccount + ".csv"

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    text_file = open(filename, "w")
    seperator = ";"

    if data and data.get("entitledServices"):

        for service in data.get("entitledServices"):
            name = service.get("name")
            displayName = service.get("displayName")
            plans = ""
            if service.get("servicePlans"):
                for plan in service.get("servicePlans"):
                    planName = plan.get("name")
                    planDisplayName = plan.get("displayName")
                    planCategory = plan.get("category")
                    dcs = ""
                    if plan.get("dataCenters"):
                        for dc in plan.get("dataCenters"):
                            dcs += dc.get("name")
                    if "free" in planDisplayName:
                        plans += planName + "(" + planDisplayName + " - " + planCategory + ")"
            row = name + seperator + displayName + seperator + plans + "\n"
            text_file.write(row)
    text_file.close()
