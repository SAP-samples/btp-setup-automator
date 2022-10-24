import re
from libs.python.helperJson import addKeyValuePair, saveJsonToFile
import os
import logging

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


def createDirectoryName(btpUsecase):
    result = None
    if btpUsecase.directoryname is not None and btpUsecase.directoryname != "":
        result = btpUsecase.directoryname.strip()
    else:
        result = "BTP setup automator (Directory)"

    btpUsecase.accountMetadata = addKeyValuePair(
        btpUsecase.accountMetadata, "directory", result)

    return result


def createSubaccountName(btpUsecase):
    result = None
    if btpUsecase.subaccountname is not None and btpUsecase.subaccountname != "":
        result = btpUsecase.subaccountname.strip()
    else:
        result = "BTP setup automator (" + btpUsecase.region + ")"

    btpUsecase.accountMetadata = addKeyValuePair(
        btpUsecase.accountMetadata, "subaccount", result)

    return result


def createInstanceName(btpUsecase, service):
    result = "instance"
    if service.category != "CF_CUP_SERVICE":
        if service.instancename is not None:
            return service.instancename
        else:
            result = service.name + "-" + service.plan + "-" + btpUsecase.suffixinstancename

        result = re.sub(r"[^\w\s]", '-', result)
        result = result.replace("--", "-")
        result = result.replace("_", "-")
        if result[len(result) - 1] == "-":
            result = result[:-1]

        result = result[:40]
    else:
        result += "-" + service.name

    return result


def createSubdomainID(btpUsecase):
    result = None
    if btpUsecase.subdomain is not None and btpUsecase.subdomain != "":
        result = btpUsecase.subdomain.strip()
    else:
        result = btpUsecase.accountMetadata["subaccount"] + \
            "-" + btpUsecase.accountMetadata["global_account_id"]

    result = re.sub(r"[^\w\s]", '-', result)
    result = result.replace(" ", "-")
    result = result.replace("_", "-")
    result = result.replace("--", "-")

    if result[len(result) - 1] == "-":
        result = result[:-1]
    result = result[:60].lower()

    btpUsecase.accountMetadata = addKeyValuePair(
        btpUsecase.accountMetadata, "subdomain", result)

    return result


def createOrgName(btpUsecase, envName):
    result = None
    if envName == "cloudfoundry":
        if btpUsecase.org is not None and btpUsecase.org != "":
            result = btpUsecase.org
        else:
            result = "cf-" + btpUsecase.accountMetadata["subdomain"]
    if envName == "kymaruntime":
        result = "kyma-" + btpUsecase.accountMetadata["subdomain"]
    if envName != "kymaruntime" and envName != "cloudfoundry":
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

    url += "globalaccount/" + \
        btpUsecase.accountMetadata["global_account_id"] + "/"
    url += "subaccount/" + \
        btpUsecase.accountMetadata["subaccountid"] + "/service-instances"

    return url


def getDictWithEnvVariables(btpUsecase):
    result = None
    if btpUsecase.envvariables is not None and len(btpUsecase.envvariables) > 0:
        for variable, value in btpUsecase.envvariables.items():
            os.environ[variable] = value
        result = dict(os.environ)

    return result


def getEnvVariableValue(variable):
    result = None
    if (os.environ.get(variable)):
        result = os.environ[variable]
    return result


def showEnvVariables():
    for k, v in sorted(os.environ.items()):
        # Avoid to show env variables whose name already contains "password" is been displayed to the user
        kNormalized = k.capitalize
        if "password".capitalize in kNormalized:
            v = "************"
        log.info(str(k) + ': ' + str(v))


def save_collected_metadata(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata
    filename = btpUsecase.metadatafile
    saveJsonToFile(filename, accountMetadata)
