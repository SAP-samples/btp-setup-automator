from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperJson import convertStringToJson
from libs.python.helperYaml import build_and_store_service_instance_yaml_from_parameters
from libs.python.helperCommandExecution import runShellCommand, runShellCommandFlex


def getKymaEnvironmentInfoByClusterName(environmentData, kymaClusterName):
    for entry in environmentData["environmentInstances"]:
        parametersFromEntry = convertStringToJson(entry["parameters"])
        if entry["environmentType"] == "kyma" and parametersFromEntry["name"] == kymaClusterName:
            return entry


def getKymaEnvironmentStatusFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["state"]


def extractKymaDashboardUrlFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["dashboardUrl"]


def extractKymaKubeConfigUrlFromEnvironmentDataEntry(environmentDataEntry):
    labelsFromEntry = convertStringToJson(environmentDataEntry["labels"])
    return labelsFromEntry["KubeconfigURL"]


def getKymaEnvironmentIdByClusterName(environmentData, kymaClusterName):
    for entry in environmentData["environmentInstances"]:
        parametersFromEntry = convertStringToJson(entry["parameters"])
        if entry["environmentType"] == "kyma" and parametersFromEntry["name"] == kymaClusterName:
            return entry["id"]


def get_kyma_service_status(btpUsecase, service):
    command = "kubectl get ServiceInstance " + service.instanceName + " -n " + btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath + " | jq .status.ready"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    if p.stdout.decode() == "TRUE":
        return "create succeeded"
    else:
        return "NotReady"


def create_kyma_service(btpUsecase, service):

    filepath = "k8s/service-instance/service-instance-" + btpUsecase.accountMetadata.get("subaccountid") + ".yaml"

    build_and_store_service_instance_yaml_from_parameters(service, filepath)

    command = "kubectl apply -f " + filepath + " -n " + btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Create instance >" + service.instancename + "< for service >" + service.name + "< and plan >" + service.plan + "<" + " in namespace >" + btpUsecase.k8snamespace + "<"

    runShellCommandFlex(btpUsecase, command, "INFO", message, True, True)

    return service


def getStatusResponseFromCreatedKymaInstance(btpUsecase, instanceName):
    command = "kubectl get ServiceInstance " + instanceName + " -n " + btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath + " -o json"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    jsonResult = convertStringToJson(p.stdout.decode())

    return jsonResult


def getKymaServiceBinding(btpUsecase, instanceName, keyName):
    return "to be done"


def deleteKymaServiceBindingAndWait(key, service, btpUsecase):
    deleteKymaServiceBinding(key["keyname"], service["instancename"], btpUsecase)
    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(btpUsecase, service)
    current_time = 0
    #while usecaseTimeout > current_time:
    #    command = "cf service-key '" + service["instancename"] + "' " + key["keyname"]
    #    # Calling the command with the goal to get back the "FAILED" status, as this means that the service key was not found (because deletion was successfull)
    #    # If the status is not "FAILED", this means that the deletion hasn't been finished so far
    #    message = "check if service key >" + key["keyname"] + "< for service instance >" + service["instancename"] + "<"
    #    p = runShellCommandFlex(btpUsecase, command, "CHECK", message, False, False)
    #    result = p.stdout.decode()
    #    if "FAILED" in result:
    #        usecaseTimeout = current_time - 1
    #    time.sleep(search_every_x_seconds)
    #    current_time += search_every_x_seconds
    return "to be done"    


def deleteKymaServiceBinding(keyName, instanceName, btpUsecase):
    return "to be done"


def deleteKymaServiceInstance(service, btpUsecase):
    command = "kubectl delete ServiceInstance " + service["instancename"] + " -n " + btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Delete Kyma service instance >" + service["instancename"] + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result
    

def getKymaServiceDeletionStatus(service, btpUsecase):
    command = "kubectl get ServiceInstance " + service["instancename"] + " -n " + btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    p = runShellCommandFlex(btpUsecase, command, "CHECK", None, False, False)
    output = p.stdout.decode()
    err = p.stderr.decode()
    if output == "" and "NotFound" in err:
        return "deleted"
    else:
        return "not deleted"   