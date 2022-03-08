import re
from libs.python.helperJson import addKeyValuePair


def getTimingsForStatusRequest(btpUsecase, thisService):

    search_every_x_seconds = btpUsecase.repeatstatusrequest
    usecaseTimeout = btpUsecase.repeatstatustimeout

    # If the service has defined its own time to repeat a status request, take that time instead
    if "repeatstatusrequest" in thisService:
        search_every_x_seconds = int(thisService["repeatstatusrequest"])
    if "repeatstatustimeout" in thisService:
        usecaseTimeout = int(thisService["repeatstatustimeout"])

    return search_every_x_seconds, usecaseTimeout


def getServiceByServiceName(btpUsecase, serviceName):
    for service in btpUsecase.definedServices:
        if service["name"] == serviceName:
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
    if "instancename" in service:
        return service["instancename"]
    else:
        result = service["name"] + "_" + btpUsecase.suffixinstancename
    result = re.sub(r"[^\w\s]", '_', result)
    result = result.replace("__", "_")
    if result[len(result) - 1] == "_":
        result = result[:-1]

    result = result[:40]

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
