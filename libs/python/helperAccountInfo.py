import json
import logging
from libs.python.helperCommandExecution import runCommandAndGetJsonResult

log = logging.getLogger(__name__)


def getServiceInfo(btpUsecase):
    usecaseRegion = btpUsecase.region

    command = "btp --format json list accounts/entitlement --global-account \"" + \
        btpUsecase.globalaccount + "\""
    message = "Get list of available services and app subsciptions for defined region >" + \
        usecaseRegion + "<"
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


def getJsonFromFile(filename):
    data = None
    foundError = False

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        print("Can't open json file >" + filename + "<")
        foundError = True
    except ValueError as err:
        print("There is an issue in the json file >" + filename +
              "<. Issue starts on character position " + str(err.pos) + ": " + err.msg)
        foundError = True
    finally:
        f.close()

    if foundError is True:
        print("Can't run the use case before the error(s) mentioned above are not fixed")
        exit()
    return data


def getDataCenterFromService(service):
    result = []
    for plan in service["servicePlans"]:
        for dataCenter in plan["dataCenters"]:
            if dataCenter["name"] not in result:
                result.append(dataCenter["name"])
    result.sort()
    return result


def createCSVForEntitledServicesInDatacenters(btpUsecase):

    data = getServiceInfo(btpUsecase)

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

    text_file = open("dcCoverageEntitledServices.csv", "w")
    text_file.close()
