from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperJson import getJsonFromFile
from libs.python.helperFolders import FOLDER_SCHEMA_LIBS, FOLDER_DOCS_TEMPLATES, FOLDER_DOCS_OUTPUT
import logging

log = logging.getLogger(__name__)


def updateDocumentation():

    data = getJsonFromFile(None, FOLDER_SCHEMA_LIBS + "btpsa-usecase.json")
    parameters = {"parameters": data.get("properties")}
    targetFilename = FOLDER_DOCS_OUTPUT + "PARAMETERS-SERVICES.md"
    renderTemplateWithJson(FOLDER_DOCS_TEMPLATES, "PARAMETERS-SERVICES.md", targetFilename, parameters)
    log.success("updated the documentation for use cases at >" + targetFilename + "<")

    data = getJsonFromFile(None, FOLDER_SCHEMA_LIBS + "btpsa-parameters.json")
    parameters = {"parameters": data.get("properties")}
    targetFilename = FOLDER_DOCS_OUTPUT + "PARAMETERS-BTPSA.md"
    renderTemplateWithJson(FOLDER_DOCS_TEMPLATES, "PARAMETERS-BTPSA.md", targetFilename, parameters)
    log.success("updated the documentation for btpsa parameters at >" + targetFilename + "<")
