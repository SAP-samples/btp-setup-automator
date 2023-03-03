import sys
import os
import requests
import logging
import json
import jinja2
from pathlib import Path
import glob
from copy import deepcopy

log = logging.getLogger(__name__)

CATEGORIES = {}
CATEGORIES["SERVICE"] = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM"]
CATEGORIES["APPLICATION"] = ["APPLICATION", "QUOTA_BASED_APPLICATION"]
CATEGORIES["ENVIRONMENT"] = ["ENVIRONMENT"]


def loadJSONFiles(folder, pattern):
    result = []

    for file in glob.glob(str(folder) + "/" + pattern):
        result.append(getJsonFromFile(file))

    return result


def fetchEntitledServiceList(mainDataJsonFilesFolder):
    serviceListRaw = loadJSONFiles(mainDataJsonFilesFolder, "*.json")
    btpServiceList = convertToServiceListByCategory(serviceListRaw)

    # determine all data centers
    regions = set()
    allDataCenters = []
    for service in serviceListRaw:
        for plan in service.get("servicePlans"):
            for dataCenter in plan.get("dataCenters"):
                region = dataCenter.get("region")
                if region and region not in regions:
                    regions.add(region)
                    allDataCenters.append(dataCenter)
    allDataCenters = sorted(
        allDataCenters, key=lambda d: (d["region"].lower()), reverse=False
    )

    addManuallyMaintainedServiceSchema(btpServiceList)

    thisResult = {"btpservicelist": btpServiceList, "datacenterslist": allDataCenters}
    return thisResult


# This function will add schema information to service plans
# in case they are not provided in the fetched metadata
# and manually maintained in the folder config/services-jsonschemas
def addManuallyMaintainedServiceSchema(btpServiceList):
    FOLDER_WITH_MANUAL_SCHEMAS = Path(
        __file__, "..", "..", "..", "config", "services-jsonschemas"
    ).resolve()

    # first get the manually maintained json schemas
    manuallyMaintainedSchemaFiles = []
    for root, dirs, files in os.walk(FOLDER_WITH_MANUAL_SCHEMAS):
        for file in files:
            if file.endswith(".json"):
                manuallyMaintainedSchemaFiles.append(os.path.join(root, file))

    manuallyMaintainedSchemas = []
    for thisFile in manuallyMaintainedSchemaFiles:
        schemaInfo = getJsonFromFile(thisFile)
        for thisSchemaInfo in schemaInfo:
            manuallyMaintainedSchemas.append(thisSchemaInfo)

    for serviceType in btpServiceList:
        for service in serviceType.get("list"):
            for plan in service.get("servicePlans"):
                resultingSchemas = [
                    thisSchema
                    for thisSchema in manuallyMaintainedSchemas
                    if thisSchema.get("name") == service.get("name")
                    and thisSchema.get("plan") == plan.get("name")
                ]
                if resultingSchemas and len(resultingSchemas) > 0:
                    if len(resultingSchemas) == 1:
                        plan["schemas"] = resultingSchemas[0].get("schemas")
                        resultingSchemas = resultingSchemas
                    else:
                        print(
                            "ERROR: Can't add multiple schema info to a service plan!"
                        )


def renderTemplateWithJson(templateFilename, targetFilename, parameters):
    templateFolder = os.path.dirname(templateFilename)
    templateBasename = os.path.basename(templateFilename)

    templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(templateBasename)

    renderedText = template.render(
        parameters
    )  # this is where to put args to the template renderer

    with open(targetFilename, "w") as f:
        f.write(renderedText)


def getJsonFromFile(filename):
    data = None
    foundError = False
    f = None

    if "http://" in filename or "https://" in filename:
        data = None
        try:
            thisRequest = requests.get(filename)
            data = json.loads(thisRequest.text)
        except Exception as e:
            log.error("please check the json file >" + filename + "<: " + str(e))
            sys.exit(os.EX_DATAERR)
        return data

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    except ValueError as err:
        message = (
            "There is an issue in the json file >"
            + filename
            + "<. Issue starts on character position "
            + str(err.pos)
            + ": "
            + err.msg
        )
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = (
            "Can't run the use case before the error(s) mentioned above are not fixed"
        )
        if log is not None:
            log.error(message)
        else:
            print(message)
        sys.exit(os.EX_DATAERR)
    return data


def convertToServiceListByCategory(rawData):
    result = []
    for category in CATEGORIES:
        list = {"name": category, "list": getBtpCategory(category, rawData)}
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
        print(
            "ERROR: the category >"
            + category
            + "< can't be assigned to one of the defined service categories"
        )

    return services


def getServicesForCategory(category, rawData):
    result = []

    for service in rawData:
        servicePlans = getServicePlansForCategory(service, category)
        thisService = None
        if servicePlans:
            thisService = deepcopy(service)
            thisService["servicePlans"] = servicePlans
            result.append(thisService)
    sortedResult = sorted(result, key=lambda d: (d["name"].lower()), reverse=False)

    return sortedResult


def getServicePlansForCategory(service, category):
    result = []

    for plan in service.get("servicePlans"):
        thisCategory = plan.get("category")
        if thisCategory in CATEGORIES.get(category):
            alreadyExistsInResult = False
            for temp in result:
                if temp.get("name") == plan.get("name"):
                    alreadyExistsInResult = True
            if not alreadyExistsInResult:
                result.append(getBtpServicePlan(plan))

    return result


def getBtpServicePlan(rawData):
    name = rawData.get("name")
    displayName = rawData.get("displayName")
    description = rawData.get("description")
    uniqueIdentifier = rawData.get("uniqueIdentifier")
    category = rawData.get("category")
    schemas = rawData.get("schemas")
    dataCenters = rawData.get("dataCenters")

    dataCenters = sorted(dataCenters, key=lambda d: d["region"], reverse=False)
    result = {
        "name": name,
        "displayName": displayName,
        "description": description,
        "uniqueIdentifier": uniqueIdentifier,
        "category": category,
        "dataCenters": dataCenters,
        "provisioningMethod": rawData.get("provisioningMethod"),
        "schemas": schemas,
    }

    return result
