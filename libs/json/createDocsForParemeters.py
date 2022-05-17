#!/usr/bin/python
import jinja2
import json


def getJsonFromFile(filename):
    data = None
    foundError = False
    f = None

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        print(message)
        foundError = True
    except ValueError as err:
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg

        print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
        print(message)
    return data


def renderTemplateWithJson(TEMPLATE_FILE, PARAMETER_FILE):

    templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(TEMPLATE_FILE)
    parameters = getJsonFromFile(PARAMETER_FILE)

    renderedText = template.render(params=parameters)  # this is where to put args to the template renderer

    with open('../../docs/' + TEMPLATE_FILE, 'w') as f:
        f.write(renderedText)


renderTemplateWithJson("PARAMETERS-SERVICES.md", "paramServices.json")
renderTemplateWithJson("PARAMETERS-BTPSA.md", "paramBtpSetupAutomator.json")
