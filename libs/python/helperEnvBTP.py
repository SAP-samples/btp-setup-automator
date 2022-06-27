from libs.python.helperCommandExecution import runShellCommand
from libs.python.helperJson import convertStringToJson
import logging

log = logging.getLogger(__name__)


def get_btp_service_status(btpUsecase, service):
    instanceName = service.instancename
    instanceId = service.id

    command = "btp --format json get services/instance --id " + instanceId + " --name " + instanceName + + " --subaccount " + btpUsecase.accountMetadata.get("subaccountid")

    p = runShellCommand(btpUsecase, command, "CHECK", None)
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
