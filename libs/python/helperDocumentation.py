from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperJson import getJsonFromFile
import logging

log = logging.getLogger(__name__)


def updateDocumentation():

    data = getJsonFromFile(None, "./schemas/btpsa_usecase.json")
    parameters = data.get("properties")
    targetFilename = "./docs/PARAMETERS-SERVICES.md"
    renderTemplateWithJson("PARAMETERS-SERVICES.md", targetFilename, parameters)
    log.success("updated the documentation for use cases at >" + targetFilename + "<")

    data = getJsonFromFile(None, "./schemas/btpsa_parameters.json")
    parameters = data.get("properties")
    targetFilename = "./docs/PARAMETERS-BTPSA.md"
    renderTemplateWithJson("PARAMETERS-BTPSA.md", targetFilename, parameters)
    log.success("updated the documentation for btpsa parameters at >" + targetFilename + "<")
