import re
from libs.python.helperJson import addKeyValuePair
import os
import logging
from libs.python.helperJson import dictToJson

from libs.python.helperServices import BTPSERVICE

log = logging.getLogger(__name__)


def getTimingsForStatusRequest(btpUsecase, thisService):
    search_every_x_seconds = btpUsecase.repeatstatusrequest
    usecaseTimeout = btpUsecase.repeatstatustimeout

    # If the service has defined its own time to repeat a status request, take that time instead
    if isinstance(thisService, BTPSERVICE):
        if thisService.repeatstatusrequest is not None:
            search_every_x_seconds = thisService.repeatstatusrequest
        if thisService.repeatstatustimeout is not None:
            usecaseTimeout = thisService.repeatstatustimeout
    else:
        if "repeatstatusrequest" in thisService:
            search_every_x_seconds = thisService["repeatstatusrequest"]
        if "repeatstatustimeout" in thisService:
            usecaseTimeout = thisService["repeatstatustimeout"]

    return search_every_x_seconds, usecaseTimeout


def getServiceByServiceName(btpUsecase, serviceName):
    for service in btpUsecase.definedServices:
        if service.name == serviceName:
            return service
    return None


def getNamingPattern(btpUsecase, prefix, suffix):
    result = None
    if prefix is None:
        prefix = ""
    if suffix is None:
        suffix = ""

    if prefix is None:
        prefix = ""
    if suffix is None:
        suffix = ""
    result = prefix + suffix
    result = re.sub(r"[^\w\s]", '-', result)
    result = result.replace(" ", "-").lower()
    result = result.replace("_", "-").lower()

    return result


def getNamingPatternForServiceSuffix(btpUsecase):
    result = getNamingPattern(btpUsecase, " instance ", None)
    return result


def getNamingPatternForIdsNEW(btpUsecase):
    usecaseRegion = btpUsecase.region
    prefix = "BTP setup automator"
    suffix = usecaseRegion

    result = getNamingPattern(btpUsecase, prefix, suffix)
    return result


def createSubaccountName(btpUsecase):
    result = None
    if btpUsecase.subaccountname is not None and btpUsecase.subaccountname != "":
        result = btpUsecase.subaccountname.strip()
    else:
        result = "BTP setup automator (" + btpUsecase.region + ")"

    btpUsecase.accountMetadata = addKeyValuePair(btpUsecase.accountMetadata, "subaccount", result)

    return result


def createInstanceName(btpUsecase, service):
    result = "instance"
    if service.category != "CF_CUP_SERVICE":
        if service.instancename is not None:
            return service.instancename
        else:
            result = service.name + "_" + service.plan + "_" + btpUsecase.suffixinstancename

        result = re.sub(r"[^\w\s]", '_', result)
        result = result.replace("__", "_")
        if result[len(result) - 1] == "_":
            result = result[:-1]

        result = result[:40]
    else:
        result += "_" + service.name

    return result


def createSubdomainID(btpUsecase):
    result = None
    if btpUsecase.subdomain is not None and btpUsecase.subdomain != "":
        result = btpUsecase.subdomain.strip()
    else:
        result = btpUsecase.accountMetadata["subaccount"] + "-" + btpUsecase.accountMetadata["global_account_id"]

    result = re.sub(r"[^\w\s]", '-', result)
    result = result.replace(" ", "-")
    result = result.replace("_", "-")
    result = result.replace("--", "-")

    if result[len(result) - 1] == "-":
        result = result[:-1]
    result = result[:60].lower()

    btpUsecase.accountMetadata = addKeyValuePair(btpUsecase.accountMetadata, "subdomain", result)

    return result


def createOrgName(btpUsecase, envName):
    result = None
    result = envName + "-" + btpUsecase.accountMetadata["subdomain"]

    result = re.sub(r"[^\w\s]", '-', result)
    result = result.replace(" ", "-").lower()
    result = result.replace("_", "-").lower()
    result = result.replace("--", "-").lower()
    result = result[:60]

    return result


def buildUrltoSubaccount(btpUsecase):
    region = btpUsecase.region

    url = ""
    if btpUsecase.accountMetadata["licenseType"] == "TRIAL":
        url = "https://cockpit.hanatrial.ondemand.com/trial/#/"
    else:
        url = "https://cockpit." + region + ".hana.ondemand.com/cockpit/#/"

    url += "globalaccount/" + btpUsecase.accountMetadata["global_account_id"] + "/"
    url += "subaccount/" + btpUsecase.accountMetadata["subaccountid"] + "/service-instances"

    return url


def getDictWithEnvVariables(btpUsecase):
    result = None
    if btpUsecase.envvariables is not None:
        for key, value in btpUsecase.envvariables:
            os.environ[key] = value
        result = dict(os.environ)

    return result


def setEnvVariables(btpUsecase, parameters):
    for key, value in parameters.items():
        # avoid having "None" as value in case value was not set
        if value is None:
            value = ""
        envVariableAlreadyThere = False
        if btpUsecase.envvariables is None:
            btpUsecase.envvariables = []

        if btpUsecase.envvariables is not None and len(btpUsecase.envvariables) > 0:
            for myVariable in btpUsecase.envvariables:
                if myVariable["key"] == key:
                    envVariableAlreadyThere = True

        if envVariableAlreadyThere is False:
            newEnvVar = {"key": key, "value": value}
            btpUsecase.envvariables.append(newEnvVar)
        else:
            newEnvVar = {"key": key, "value": value}
            btpUsecase.envvariables.update(newEnvVar)

        os.environ[key] = value
        # log.info("set environment variable >" + str(key) + "< to value >" + str(value) + "<")


def showEnvVariables():
    for k, v in sorted(os.environ.items()):
        log.info(str(k) + ': ' + str(v))
