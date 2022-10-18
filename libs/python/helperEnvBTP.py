from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperCommandExecution import runShellCommand, runShellCommandFlex
from libs.python.helperJson import convertStringToJson
import logging
import os
import sys
import time

log = logging.getLogger(__name__)


def get_btp_service_status(btpUsecase, service):
    instanceName = service.instancename
    instanceId = service.id

    message = "Get creation status for service instance >" + instanceName + "<"
    command = "btp --format json get services/instance --id " + instanceId + " --name " + \
        instanceName + + " --subaccount " + \
        btpUsecase.accountMetadata.get("subaccountid")

    p = runShellCommand(btpUsecase, command, "CHECK", message)
    result = p.stdout.decode()

    return result


def create_btp_service(btpUsecase, service):
    command = "btp --format json create services/instance --subaccount " + btpUsecase.accountMetadata.get(
        "subaccountid") + " --offering-name " + service.name + " --plan-name " + service.plan + " --name " + service.instancename

    if service.parameters is not None:
        command = command + " --parameters '" + service.parameters

    message = "Create instance >" + service.instancename + "< for service >" + \
        service.name + "< and plan >" + service.plan + "<" + " via BTP CLI"

    p = runShellCommand(btpUsecase, command, "INFO", message)

    result = convertStringToJson(p.stdout.decode())

    service.id = result.get("id")

    return service


def getStatusResponseFromCreatedBTPInstance(btpUsecase, instancename, service):
    command = "btp --format json get services/instance --id " + service.id + " --subaccount " + \
        btpUsecase.accountMetadata.get("subaccountid")
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    jsonResult = convertStringToJson(result)

    return jsonResult


def createBtpServiceBinding(btpUsecase, instanceId, instanceName, keyName):
    result = None

    command = "btp --format JSON create services/binding --name " + keyName + " --service-instance " + \
        instanceId + " --subaccount " + \
        btpUsecase.accountMetadata.get("subaccountid")
    message = "create service key for service instance >" + \
        instanceName + "< for keyname >" + keyName + "<"

    p = runShellCommand(btpUsecase, command, "INFO", message)
    returnCode = p.returncode

    if returnCode == 0:
        jsonResult = convertStringToJson(p.stdout.decode())

        command = "btp --format JSON get services/binding --id " + \
            jsonResult.get("id") + " --subaccount " + \
            btpUsecase.accountMetadata.get("subaccountid")
        message = "get service key for instance >" + \
            instanceName + "< and keyname >" + keyName + "<"
        response = runShellCommand(btpUsecase, command, "CHECK", message)
        result = convertStringToJson(response.stdout.decode())
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)

    return result


def deleteBtpServiceBindingAndWait(key, service, btpUsecase):
    deleteBtpServiceBinding(
        key["keyname"], service["instancename"], btpUsecase)

    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
        btpUsecase, service)
    current_time = 0
    while usecaseTimeout > current_time:
        message = "check if service binding >" + \
            key["keyname"] + "< for service instance >" + \
            service["instancename"] + "< is deleted"
        command = "btp --format JSON get services/binding --name " + \
            key["keyname"] + " --subaccount " + \
            btpUsecase.accountMetadata.get("subaccountid")
        p = runShellCommandFlex(btpUsecase, command,
                                "CHECK", message, False, False)

        output = p.stdout.decode()
        err = p.stderr.decode()
        if output == "" and "FAILED" in err:
            usecaseTimeout = current_time - 1
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds


def deleteBtpServiceBinding(keyName, instanceName, btpUsecase):
    command = "btp --format JSON delete services/binding -n " + \
        keyName + " -sa " + \
        btpUsecase.accountMetadata.get("subaccountid") + " --confirm"
    message = "Delete BTP service binding >" + keyName + \
        "< for service instance >" + instanceName + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def deleteBtpServiceInstance(service, btpUsecase):
    command = "btp --format JSON delete services/instance " + \
        service["id"] + " -sa " + \
        btpUsecase.accountMetadata.get("subaccountid") + " --confirm"
    message = "Delete BTP service instance >" + \
        service["instancename"] + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def getBtpServiceDeletionStatus(service, btpUsecase):
    command = "btp --format JSON get services/instance " + \
        service["id"] + " -sa " + \
        btpUsecase.accountMetadata.get("subaccountid")

    message = "Get deletion status for service instance >" + \
        service["instancename"] + "<"

    p = runShellCommandFlex(btpUsecase, command,
                            "CHECK", message, False, False)
    output = p.stdout.decode()
    err = p.stderr.decode()
    if output == "" and "FAILED" in err:
        return "deleted"
    else:
        return "not deleted"
