from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperJson import getJsonFromFile
from libs.python.helperFolders import FOLDER_SCHEMA_LIBS, FOLDER_SCHEMA_TEMPLATES
import logging

log = logging.getLogger(__name__)


def updateDocumentation():

    data = getJsonFromFile(None, FOLDER_SCHEMA_LIBS + "btpsa-usecase.json")
    parameters = data.get("properties")
    targetFilename = "./docs/PARAMETERS-SERVICES.md"
    renderTemplateWithJson(FOLDER_SCHEMA_TEMPLATES, "PARAMETERS-SERVICES.md", targetFilename, parameters)
    log.success("updated the documentation for use cases at >" + targetFilename + "<")

    data = getJsonFromFile(None, FOLDER_SCHEMA_LIBS + "btpsa-parameters.json")
    parameters = data.get("properties")
    targetFilename = "./docs/PARAMETERS-BTPSA.md"
    renderTemplateWithJson(FOLDER_SCHEMA_TEMPLATES, "PARAMETERS-BTPSA.md", targetFilename, parameters)
    log.success("updated the documentation for btpsa parameters at >" + targetFilename + "<")
