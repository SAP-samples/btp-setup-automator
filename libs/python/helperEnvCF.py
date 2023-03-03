import os
import sys
from libs.python.helperCommandExecution import (
    runShellCommand,
    runCommandAndGetJsonResult,
    runShellCommandFlex,
)
from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperJson import (
    convertCloudFoundryCommandForSingleServiceToJson,
    convertCloudFoundryCommandOutputToJson,
    convertStringToJson,
    dictToString,
)
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
    message = (
        "create service key from XSUAA instance >"
        + instanceName
        + "< for keyname >"
        + keyName
        + "<"
    )
    p = runShellCommand(btpUsecase, command, "INFO", message)
    returnCode = p.returncode

    if returnCode == 0:
        command = "cf service-key '" + instanceName + "' '" + keyName + "'"
        message = (
            "get service key for instance >"
            + instanceName
            + "< and keyname >"
            + keyName
            + "<"
        )
        response = runShellCommand(btpUsecase, command, "CHECK", message)
        # Delete the first 2 lines of the CF result string as they don't contain json data
        result = response.stdout.decode()
        result = result.split("\n", 2)[-1]
        result = convertStringToJson(result)
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)
    return result


def deleteCFServiceKeysAndWait(key, service, btpUsecase):
    delete_cf_service_key(btpUsecase, service["instancename"], key["keyname"])

    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
        btpUsecase, service
    )
    current_time = 0
    while usecaseTimeout > current_time:
        command = "cf service-key '" + service["instancename"] + "' " + key["keyname"]
        # Calling the command with the goal to get back the "FAILED" status, as this means that the service key was not
        # found (because deletion was successful)
        # If the status is not "FAILED", this means that the deletion hasn't been finished so far
        message = (
            "check if service key >"
            + key["keyname"]
            + "< for service instance >"
            + service["instancename"]
            + "< is deleted"
        )
        p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
        result = p.stdout.decode()
        if "FAILED" in result:
            usecaseTimeout = current_time - 1
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds


def delete_cf_service_key(btpUsecase, instanceName, keyName):
    command = "cf delete-service-key '" + instanceName + "' '" + keyName + "' -f"
    message = (
        "delete service key from instance >"
        + instanceName
        + "< for key >"
        + keyName
        + "<"
    )
    runShellCommand(btpUsecase, command, "INFO", message)


def deleteCFServiceInstance(service, btpUsecase):
    command = "cf delete-service '" + service["instancename"] + "' -f"
    message = (
        "Delete CF service instance >" + service["instancename"] + "< from subaccount"
    )
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def checkIfCFEnvironmentAlreadyExists(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata
    orgid = None
    org = None

    command = (
        "btp --format json list account/environment-instance --subaccount '"
        + accountMetadata["subaccountid"]
        + "'"
    )
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    if "orgid" in accountMetadata:
        orgid = accountMetadata["orgid"]

    # If the for loop didn't return any value, the orgid wasn't found
    for instance in result["environmentInstances"]:
        if (
            instance["subaccountGUID"] == btpUsecase.subaccountid
            and instance["environmentType"] == "cloudfoundry"
        ):
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

    command = (
        "btp --format json list account/environment-instance --subaccount '"
        + accountMetadata["subaccountid"]
        + "'"
    )
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    for instance in result["environmentInstances"]:
        if (
            instance["subaccountGUID"] == btpUsecase.subaccountid
            and instance["environmentType"] == "cloudfoundry"
        ):
            labels = convertStringToJson(instance["labels"])

            if labels.get("API Endpoint"):
                cf_api_endpoint = labels.get("API Endpoint")
                break
            elif labels.get("API Endpoint:"):
                cf_api_endpoint = labels.get("API Endpoint:")
                break

    return cf_api_endpoint


def getCfApiEndpointFromLabels(labelsAsJson):
    cf_api_endpoint = None

    if labelsAsJson.get("API Endpoint"):
        cf_api_endpoint = labelsAsJson.get("API Endpoint")
    elif labelsAsJson.get("API Endpoint:"):
        cf_api_endpoint = labelsAsJson.get("API Endpoint:")

    return cf_api_endpoint


def getStatusResponseFromCreatedInstance(btpUsecase, instancename):
    command = "cf service '" + instancename + "'"
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    jsonResults = convertCloudFoundryCommandForSingleServiceToJson(result)
    return jsonResults


def try_until_cf_space_done(
    btpUsecase,
    command,
    message,
    spacename,
    search_every_x_seconds,
    timeout_after_x_seconds,
):
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


def try_until_space_quota_created(
    btpUsecase,
    command,
    message,
    quotaname,
    search_every_x_seconds,
    timeout_after_x_seconds,
):
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


def check_if_service_plan_supported_in_cf(btpUsecase, service):
    # Defines how often we should ask CF whether the plan is
    # available or not
    MAX_TRIES = 6
    # Seconds after which we should try again
    SEARCH_EVERY_X_SECONDS = 10

    result = False

    plan = service.plan
    if service.planCatalogName is not None:
        plan = service.planCatalogName

    message = (
        "Check if service >"
        + service.name
        + "< and plan >"
        + plan
        + "<"
        + " is supported in this sub account for the environment >cloudfoundry<"
    )

    command = (
        "cf marketplace -e " + service.name
    )

    for x in range(1, MAX_TRIES):
        p = runShellCommand(btpUsecase, command, "INFO", message)
        shellResult = p.stdout.decode()
        jsonResult = convertCloudFoundryCommandOutputToJson(shellResult, numberOfLinesToRemove=3)

        for entry in jsonResult:
            if entry.get("plan") == plan:
                return True
        log.info(shellResult)
        # In case the search was not successful, sleep a few seconds before trying again
        log.info("Plan not found, yet. Trying again (" + str(x) + "/" + str(MAX_TRIES) + ") in " + str(SEARCH_EVERY_X_SECONDS) + "seconds.")
        time.sleep(SEARCH_EVERY_X_SECONDS)

    return result


def create_cf_service(btpUsecase, service):
    instancename = service.instancename

    plan = service.plan
    if service.planCatalogName is not None:
        plan = service.planCatalogName

    if check_if_service_plan_supported_in_cf(btpUsecase, service) is False:
        log.error(
            "Plan not found in CF marketplace for service >" + service.name
            + "< and plan >" + plan + "< in this sub account."
        )
        sys.exit(os.EX_DATAERR)

    command = (
        "cf create-service '" + service.name + "' '" + plan + "' '" + instancename + "'"
    )

    if service.parameters is not None:
        thisParameter = dictToString(service.parameters)
        command += " -c '" + thisParameter + "'"
    elif service.serviceparameterfile is not None:
        command += f" -c {service.serviceparameterfile}"
    message = (
        "Create instance >"
        + instancename
        + "< for service >"
        + service.name
        + "< and plan >"
        + plan
        + "<"
    )
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
    cfCupServiceAlreadyExists = cf_cup_service_already_exists(btpUsecase, instance_name)

    if cfCupServiceAlreadyExists is False:
        command = "cf cups '" + instance_name + "' "

        if service.parameters is not None:
            thisParameter = str(service.parameters)
            command += thisParameter
            message = "Create CF cups instance for service >" + instance_name + "<"
            runShellCommandFlex(btpUsecase, command, "INFO", message, True, True)
            log.info("created CF cup service >" + instance_name + "<")
        else:
            message = (
                "missing parameter for the CF cups service >"
                + instance_name
                + "<. Won't create the CF cup service."
            )
            log.warning(message)
    else:
        log.info(
            "the user provided service >"
            + instance_name
            + "< already exists and won't be created newly."
        )

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

    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
    result = p.stdout.decode()
    if "delete failed" in result:
        return "delete failed"
    if "FAILED" in result:
        return "deleted"
    else:
        return "not deleted"


def handleLabelsForCF(btpUsecase):
    # if labels are defined for CF services the need to be attached after service/service key creation
    # see https://cli.cloudfoundry.org/en-US/v8/set-label.html

    for serviceInstance in btpUsecase.accountMetadata.get("createdServiceInstances"):
        if (
            serviceInstance.get("entitleonly") is not False
            or serviceInstance.get("category") != "SERVICE"
            or serviceInstance.get("targetenvironment") != "cloudfoundry"
        ):
            # Basic check if service is in scope of attaching labels => Only CF services
            continue

        if serviceInstance.get("labels") is None:
            # Check for labels to put on service
            continue

        labelString = transformLabelJsonToCFString(serviceInstance.get("labels"))

        command = (
            "cf set-label service-instance "
            + serviceInstance.get("instancename")
            + " "
            + labelString
        )
        message = (
            "Set labels for CF service instance >"
            + serviceInstance.get("instancename")
            + "<"
        )
        runShellCommand(btpUsecase, command, "INFO", message)

        # !!! SERVICE KEYS ARE NOT SUPPORTED BY CF API V8!!!
        # if serviceInstance.get("serviceKeyLabels") is None:
        #    # Check for label that s should be put on service key
        #    continue

        # for serviceKeyLabelEntry in serviceInstance.get("serviceKeyLabels"):
        #    labelString = transformLabelJsonToCFString(serviceKeyLabelEntry.get("labels"))

        #    command = "cf set-label service-key " + serviceKeyLabelEntry.get("name") + " " + labelString
        #    message = "Set labels for CF service key >" + serviceKeyLabelEntry.get("name") + "<"
        #    runShellCommand(btpUsecase, command, "INFO", message)


def transformLabelJsonToCFString(labelJson):
    labelString = ""
    for key in labelJson:
        value = " ,".join(labelJson[key])
        labelString += key + "='" + value + "' "
    return labelString.strip()
