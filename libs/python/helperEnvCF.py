import os
import sys
from libs.python.helperCommandExecution import runShellCommand, runCommandAndGetJsonResult, runShellCommandFlex
from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperJson import convertCloudFoundryCommandForSingleServiceToJson, convertStringToJson, dictToString
import time
import logging

log = logging.getLogger(__name__)


def getKeyFromCFOutput(cfoutput, key):
    result = None

    lines = cfoutput.splitlines()
    for line in lines:
        thisLineSplit = line.split(":")
        firstCol = thisLineSplit[0]
        if firstCol:
            firstCol = firstCol.strip()
        if len(thisLineSplit) == 2 and firstCol == key:
            result = thisLineSplit[1].strip()
    return result


def get_cf_service_key(btpUsecase, instanceName, keyName):
    result = None

    command = "cf create-service-key '" + instanceName + "' '" + keyName + "'"
    message = "create service key from XSUAA instance >" + \
        instanceName + "< for keyname >" + keyName + "<"
    p = runShellCommand(btpUsecase, command, "INFO", message)
    returnCode = p.returncode

    if returnCode == 0:
        command = "cf service-key '" + instanceName + "' '" + keyName + "'"
        message = "get service key for instance >" + \
            instanceName + "< and keyname >" + keyName + "<"
        response = runShellCommand(btpUsecase, command, "CHECK", message)
        # Delete the first 2 lines of the CF result string as they don't contain json data
        result = response.stdout.decode()
        result = result.split('\n', 2)[-1]
        result = convertStringToJson(result)
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)
    return result


def deleteCFServiceKeysAndWait(key, service, btpUsecase):
    delete_cf_service_key(btpUsecase, service["instancename"], key["keyname"])

    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
        btpUsecase, service)
    current_time = 0
    while usecaseTimeout > current_time:
        command = "cf service-key '" + \
            service["instancename"] + "' " + key["keyname"]
        # Calling the command with the goal to get back the "FAILED" status, as this means that the service key was not found (because deletion was successfull)
        # If the status is not "FAILED", this means that the deletion hasn't been finished so far
        message = "check if service key >" + \
            key["keyname"] + "< for service instance >" + \
            service["instancename"] + "< is deleted"
        p = runShellCommandFlex(btpUsecase, command,
                                "CHECK", message, False, False)
        result = p.stdout.decode()
        if "FAILED" in result:
            usecaseTimeout = current_time - 1
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds


def delete_cf_service_key(btpUsecase, instanceName, keyName):
    command = "cf delete-service-key '" + instanceName + "' '" + keyName + "' -f"
    message = "delete service key from instance >" + \
        instanceName + "< for key >" + keyName + "<"
    runShellCommand(btpUsecase, command, "INFO", message)


def deleteCFServiceInstance(service, btpUsecase):
    command = "cf delete-service '" + service["instancename"] + "' -f"
    message = "Delete CF service instance >" + \
        service["instancename"] + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def checkIfCFEnvironmentAlreadyExists(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata
    orgid = None
    org = None

    command = "btp --format json list account/environment-instance --subaccount '" + \
        accountMetadata["subaccountid"] + "'"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    if "orgid" in accountMetadata:
        orgid = accountMetadata["orgid"]

    # If the for loop didn't return any value, the orgid wasn't found
    for instance in result["environmentInstances"]:
        if instance["subaccountGUID"] == btpUsecase.subaccountid and instance["environmentType"] == "cloudfoundry":
            labels = convertStringToJson(instance["labels"])
            org = labels.get("Org Name:")
            if org is None:
                org = labels.get("Org Name")

            return instance["platformId"], org

    return orgid, org


def checkIfCFSpaceAlreadyExists(btpUsecase):
    cfspacename = btpUsecase.cfspacename

    command = "cf spaces"
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    lines = result.splitlines()

    for line in lines:
        if cfspacename == line:
            return True
    return False


def getCfApiEndpointByUseCase(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata
    cf_api_endpoint = None

    command = "btp --format json list account/environment-instance --subaccount '" + \
        accountMetadata["subaccountid"] + "'"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    for instance in result["environmentInstances"]:
        if instance["subaccountGUID"] == btpUsecase.subaccountid and instance["environmentType"] == "cloudfoundry":
            labels = convertStringToJson(instance["labels"])

            if labels.get("API Endpoint"):
                cf_api_endpoint = labels.get("API Endpoint")
                break

    return cf_api_endpoint


def getCfApiEndpointFromLabels(labelsAsJson):
    cf_api_endpoint = None

    if labelsAsJson.get("API Endpoint"):
        cf_api_endpoint = labelsAsJson.get("API Endpoint")

    return cf_api_endpoint


def getStatusResponseFromCreatedInstance(btpUsecase, instancename):
    command = "cf service '" + instancename + "'"
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    jsonResults = convertCloudFoundryCommandForSingleServiceToJson(result)
    return jsonResults


def try_until_cf_space_done(btpUsecase, command, message, spacename, search_every_x_seconds, timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        p = runShellCommand(btpUsecase, command, "INFO", message)
        result = p.stdout.decode()
        lines = result.splitlines()

        for line in lines:
            if line == "name":
                continue
            if spacename == line:
                return "DONE"

        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds
    return result


def try_until_space_quota_created(btpUsecase, command, message, quotaname, search_every_x_seconds, timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        p = runShellCommand(btpUsecase, command, "INFO", message)
        result = p.stdout.decode()
        lines = result.splitlines()

        for line in lines:
            content = line.split()
            for entry in content:
                if quotaname == entry:
                    return "DONE"

        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds
    return result


def create_cf_service(btpUsecase, service):
    instancename = service.instancename

    plan = service.plan

    if service.planCatalogName is not None:
        plan = service.planCatalogName

    command = "cf create-service '" + service.name + \
        "' '" + plan + "' '" + instancename + "'"

    if service.parameters is not None:
        thisParameter = dictToString(service.parameters)
        command += " -c '" + thisParameter + "'"
    elif service.serviceparameterfile is not None:
        command += f" -c {service.serviceparameterfile}"
    message = "Create instance >" + instancename + \
        "< for service >" + service.name + "< and plan >" + plan + "<"
    runShellCommand(btpUsecase, command, "INFO", message)
    return service


def cf_cup_service_already_exists(btpUsecase, instance_name):
    command = "cf service '" + instance_name + "'"
    p = runShellCommandFlex(btpUsecase, command, "CHECK", None, False, False)
    result = p.stdout.decode()
    if "FAILED" in result:
        return False
    else:
        return True


def create_cf_cup_service(btpUsecase, service):
    instance_name = service.name
    cfCupServiceAlreadyExists = cf_cup_service_already_exists(
        btpUsecase, instance_name)

    if cfCupServiceAlreadyExists is False:
        command = "cf cups '" + instance_name + "' "

        if service.parameters is not None:
            thisParameter = str(service.parameters)
            command += thisParameter
            message = "Create CF cups instance for service >" + instance_name + "<"
            runShellCommandFlex(btpUsecase, command,
                                "INFO", message, True, True)
            log.info("created CF cup service >" + instance_name + "<")
        else:
            message = "missing parameter for the CF cups service >" + \
                instance_name + "<. Won't create the CF cup service."
            log.warning(message)
    else:
        log.info("the user provided service >" + instance_name +
                 "< already exists and won't be created newly.")

    return service


def get_cf_service_status(btpUsecase, service):
    instance_name = service.instancename

    message = "Get creation status for service instance >" + instance_name + "<"
    command = "cf service '" + instance_name + "'"
    p = runShellCommand(btpUsecase, command, "CHECK", message)
    result = p.stdout.decode()

    service_broker = getKeyFromCFOutput(result, "broker")
    status = getKeyFromCFOutput(result, "status")
    return [service_broker, status]


def get_cf_service_deletion_status(btpUsecase, service):
    instance_name = service["instancename"]
    command = "cf service '" + instance_name + "'"
    message = "Get deletion status for service instance >" + instance_name + "<"

    p = runShellCommandFlex(btpUsecase, command,
                            "CHECK", message, False, False)
    result = p.stdout.decode()
    if "delete failed" in result:
        return "delete failed"
    if "FAILED" in result:
        return "deleted"
    else:
        return "not deleted"
