from libs.python.helperCommandExecution import runShellCommand


def get_btp_service_status(btpUsecase, service):
    return "status"


def create_btp_service(btpUsecase, service):

    command = "btp create services/instance --subaccount " + btpUsecase.accountMetadata.get("subaccountid") + " --service " + service.instancename + " --plan " + service.plan + " --offering-name " + service.name

    if service.parameters is not None:
        command = command + " --parameters '" + service.parameters

    message = "Create instance >" + service.instancename + "< for service >" + service.name + "< and plan >" + service.plan + "<" + " via BTP CLI"

    runShellCommand(btpUsecase, command, "INFO", message)

    return service


def getStatusResponseFromCreatedBTPInstance(btpUsecase, instancename):
    return "status"
