import sys
import os
import requests
import logging
import json
import jinja2
from pathlib import Path

log = logging.getLogger(__name__)


def fetchEntitledServiceList(mainDataJsonFile, datacenterFile):
    resultServices = getJsonFromFile(mainDataJsonFile)
    resultDCs = getJsonFromFile(datacenterFile)
    btpservicelist = resultServices["services"]
    addManuallyMaintainedServiceSchema(btpservicelist)

    resultDCs = sorted(resultDCs, key=lambda d: (d['region'].lower()), reverse=False)

    thisResult = {"btpservicelist": btpservicelist, "datacenterslist": resultDCs}
    return thisResult


# This function will add schema information to service plans
# in case they are not provided in the fetched metadata
# and manually maintained in the folder config/services-jsonschemas
def addManuallyMaintainedServiceSchema(btpservicelist):
    FOLDER_WITH_MANUAL_SCHEMAS = Path(__file__, "..", "..", "..", "config", "services-jsonschemas").resolve()

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

    for serviceType in btpservicelist:
        for service in serviceType.get("list"):
            for plan in service.get("servicePlans"):
                resultingSchemas = [thisSchema for thisSchema in manuallyMaintainedSchemas if thisSchema.get("name") == service.get("name") and thisSchema.get("plan") == plan.get("name")]
                if resultingSchemas and len(resultingSchemas) > 0:
                    if len(resultingSchemas) == 1:
                        plan["schemas"] = resultingSchemas[0].get("schemas")
                        resultingSchemas = resultingSchemas
                    else:
                        print("ERROR: Can't add multiple schema info to a service plan!")


def renderTemplateWithJson(templateFilename, targetFilename, parameters):

    templateFolder = os.path.dirname(templateFilename)
    templateBasename = os.path.basename(templateFilename)

    templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(templateBasename)

    renderedText = template.render(parameters)  # this is where to put args to the template renderer

    with open(targetFilename, 'w') as f:
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
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
        if log is not None:
            log.error(message)
        else:
            print(message)
        sys.exit(os.EX_DATAERR)
    return data
