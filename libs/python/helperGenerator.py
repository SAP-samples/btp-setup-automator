from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperLog import initLogger
from libs.python.helperCommandExecution import login_btp, runCommandAndGetJsonResult
from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperFolders import FOLDER_BTPBASE_TEMPLATES
from libs.python.helperJsonSchemas import getDataForJsonSchemaTemplate
import logging
import sys
import os

log = logging.getLogger(__name__)


class BTPUSECASE_GEN:
    def __init__(self):
        self.myemail = getEnvVariableValue("BTPSA_PARAM_MYEMAIL")
        self.mypassword = getEnvVariableValue("BTPSA_PARAM_MYPASSWORD")
        self.globalaccount = getEnvVariableValue("BTPSA_PARAM_GLOBALACCOUNT")
        self.templatefoler = "./"
        self.btpcliapihostregion = "eu10"
        self.loginmethod = "basicAuthentication"
        self.logcommands = False
        self.region = "us10"
        self.envvariables = None
        self.logfile = "./log/generator.log"
        self.metadatafile = "./log/generator_metadata.json"

        initLogger(self)

        if self.myemail is None:
            log.error("missing email address")
            sys.exit(os.EX_DATAERR)

        if self.mypassword is None:
            log.error("missing your BTP password")
            sys.exit(os.EX_DATAERR)

        if self.globalaccount is None:
            log.error("missing your BTP globalaccount subdomain id")
            sys.exit(os.EX_DATAERR)

    def fetchEntitledServiceList(self):
        login_btp(self)

        globalaccount = self.globalaccount
        usecaseRegion = self.region

        command = "btp --format json list accounts/entitlement --global-account '" + globalaccount + "'"
        message = "Get list of available services and app subsciptions for defined region >" + usecaseRegion + "<"
        result = runCommandAndGetJsonResult(self, command, "INFO", message)

        # del result["asignedServices"]

        data = getDataForJsonSchemaTemplate(result)

        self.entitledServices = data

    def applyServiceListOnTemplate(self, targetFilename, templateFile):

        serviceList = self.entitledServices
        renderTemplateWithJson(FOLDER_BTPBASE_TEMPLATES, templateFile, targetFilename, serviceList)
        log.success("applied SAP BTP service list on template file >" + templateFile + "< and created the target file >" + targetFilename + "<")
