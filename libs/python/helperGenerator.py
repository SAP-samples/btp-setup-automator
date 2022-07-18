import sys
import os
import requests
import logging
import json
import jinja2

log = logging.getLogger(__name__)

def fetchEntitledServiceList(mainDataJsonFile, datacenterFile):
    resultServices = getJsonFromFile(mainDataJsonFile)
    resultDCs = getJsonFromFile(datacenterFile)
    btpservicelist = resultServices["services"]

    resultDCs = sorted(resultDCs, key=lambda d: (d['region'].lower()), reverse=False)

    thisResult = {"btpservicelist": btpservicelist, "datacenterslist": resultDCs}
    return thisResult


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
