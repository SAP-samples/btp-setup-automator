import logging
import os
import sys
import time

from libs.python.helperCommandExecution import runShellCommand, runShellCommandFlex
from libs.python.helperEnvironments import (
    check_if_service_plan_supported_in_environment,
)
from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperJson import convertStringToJson, dictToString

log = logging.getLogger(__name__)


def get_btp_service_status(btpUsecase, service):
    instanceName = service.instancename

    message = "Get creation status for service instance >" + instanceName + "<"
    command = (
        "btp --format json get services/instance "
        + " --name "
        + instanceName
        + +" --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
    )

    p = runShellCommand(btpUsecase, command, "CHECK", message)
    result = p.stdout.decode()

    return result


def check_if_service_plan_supported_in_sapbtp(btpUsecase, service):
    result = check_if_service_plan_supported_in_environment(
        btpUsecase, service, "sapbtp"
    )
    return result


def create_btp_service(btpUsecase, service):
    if is_service_instance_already_existing(btpUsecase, service) is True:
        log.info(
            "The service >"
            + service.instancename
            + "< already exists and won't be created newly."
        )
        return

    if check_if_service_plan_supported_in_sapbtp(btpUsecase, service) is False:
        log.error(
            "Plan not supported in environment >sapbtp<: service >"
            + service.name
            + "< and plan >"
            + service.plan
            + "<."
        )
        sys.exit(os.EX_DATAERR)

    command = (
        "btp --format json create services/instance --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
        + " --offering-name "
        + service.name
        + " --plan-name "
        + service.plan
        + " --name "
        + service.instancename
    )

    if service.parameters is not None:
        command = command + " --parameters '" + dictToString(service.parameters) + "'"

    if service.labels is not None:
        command = command + " --labels '" + dictToString(service.labels) + "'"

    message = (
        "Create instance >"
        + service.instancename
        + "< for service >"
        + service.name
        + "< and plan >"
        + service.plan
        + "<"
        + " via BTP CLI"
    )

    runShellCommand(btpUsecase, command, "INFO", message)

    return service


def getStatusResponseFromCreatedBTPInstance(btpUsecase, instancename, service):
    command = (
        "btp --format json get services/instance --name "
        + instancename
        + " --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
    )
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    jsonResult = convertStringToJson(result)

    return jsonResult


def createBtpServiceBinding(btpUsecase, instanceName, keyName, keyLabels):
    result = None

    if is_service_key_already_existing(btpUsecase, keyName) is True:
        log.info(
            "The service key>"
            + keyName
            + "< already exists and won't be created newly."
        )
        return

    command = (
        "btp --format JSON create services/binding --name "
        + keyName
        + " --instance-name "
        + instanceName
        + " --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
    )

    if keyLabels is not None:
        command = command + " --labels '" + dictToString(keyLabels) + "'"

    message = (
        "create service key for service instance >"
        + instanceName
        + "< for keyname >"
        + keyName
        + "<"
    )

    p = runShellCommand(btpUsecase, command, "INFO", message)
    returnCode = p.returncode

    if returnCode == 0:
        jsonResult = convertStringToJson(p.stdout.decode())

        command = (
            "btp --format JSON get services/binding --id "
            + jsonResult.get("id")
            + " --subaccount "
            + btpUsecase.accountMetadata.get("subaccountid")
        )
        message = (
            "get service key for instance >"
            + instanceName
            + "< and keyname >"
            + keyName
            + "<"
        )
        response = runShellCommand(btpUsecase, command, "CHECK", message)
        result = convertStringToJson(response.stdout.decode())
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)

    return result


def deleteBtpServiceBindingAndWait(key, service, btpUsecase):
    deleteBtpServiceBinding(key["keyname"], service["instancename"], btpUsecase)

    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
        btpUsecase, service
    )
    current_time = 0
    while usecaseTimeout > current_time:
        message = (
            "check if service binding >"
            + key["keyname"]
            + "< for service instance >"
            + service["instancename"]
            + "< is deleted"
        )
        command = (
            "btp --format JSON get services/binding --name "
            + key["keyname"]
            + " --subaccount "
            + btpUsecase.accountMetadata.get("subaccountid")
        )
        p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)

        output = p.stdout.decode()
        err = p.stderr.decode()
        if output == "" and "FAILED" in err:
            usecaseTimeout = current_time - 1
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds


def deleteBtpServiceBinding(keyName, instanceName, btpUsecase):
    command = (
        "btp --format JSON delete services/binding -n "
        + keyName
        + " -sa "
        + btpUsecase.accountMetadata.get("subaccountid")
        + " --confirm"
    )
    message = (
        "Delete BTP service binding >"
        + keyName
        + "< for service instance >"
        + instanceName
        + "< from subaccount"
    )
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def deleteBtpServiceInstance(service, btpUsecase):
    command = (
        "btp --format JSON delete services/instance "
        + "--name "
        + service["instancename"]
        + " -sa "
        + btpUsecase.accountMetadata.get("subaccountid")
        + " --confirm"
    )
    message = (
        "Delete BTP service instance >" + service["instancename"] + "< from subaccount"
    )
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def getBtpServiceDeletionStatus(service, btpUsecase):
    command = (
        "btp --format JSON get services/instance "
        + "--name "
        + service["instancename"]
        + " -sa "
        + btpUsecase.accountMetadata.get("subaccountid")
    )

    message = (
        "Get deletion status for service instance >" + service["instancename"] + "<"
    )

    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
    output = p.stdout.decode()
    err = p.stderr.decode()
    if output == "" and "FAILED" in err:
        return "deleted"
    else:
        return "not deleted"


def is_service_instance_already_existing(btpUsecase, service):
    instanceName = service.instancename

    message = "Check if service instance >" + instanceName + "< already exists"
    command = (
        "btp --format json get services/instance "
        + " --name "
        + instanceName
        + " --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
    )

    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
    err = p.stderr.decode()

    if err != "" and "FAILED" in err:
        return False
    else:
        return True


def is_service_key_already_existing(btpUsecase, keyName):
    message = "Check if service key >" + keyName + "< already exists"
    command = (
        "btp --format json get services/binding "
        + " --name "
        + keyName
        + " --subaccount "
        + btpUsecase.accountMetadata.get("subaccountid")
    )

    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
    err = p.stderr.decode()

    if err != "" and "FAILED" in err:
        return False
    else:
        return True
