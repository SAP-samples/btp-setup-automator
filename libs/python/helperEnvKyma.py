from libs.python.helperJson import convertStringToJson
from libs.python.helperYaml import build_service_binding_yaml_from_parameters, store_yaml_to_disk
from libs.python.helperCommandExecution import runShellCommand


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
    command = "kubectl get ServiceInstance " + service.instanceName + " -n " + btpUsecase.accountMetadata.get("k8snamespace") + " --kubeconfig " + btpUsecase.accountMetadata.get("kubeconfigpath") + " | jq .status.ready"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    if p.stdout.decode() == "TRUE":
        return "create succeeded"
    else:
        return "NotReady"


def create_kyma_service(btpUsecase, service):
    serviceInstanceYaml = build_service_binding_yaml_from_parameters(service)

    filepath = "k8s/service-instance/service-instance-" + btpUsecase.accountMetadata.get("subaccountid") + ".yaml"
    store_yaml_to_disk(filepath, serviceInstanceYaml)

    # Call kubectl to create the service
    command = "kubectl apply -f " + filepath + " -n " + btpUsecase.accountMetadata.get("k8snamespace") + " --kubeconfig " + btpUsecase.accountMetadata.get("kubeconfigpath")
    message = "Create instance >" + service.instanceName + "< for service >" + service.name + "< and plan >" + service.plan + "<" + "in namespace >" + btpUsecase.accountMetadata.get("k8snamespace") + "<"

    runShellCommand(btpUsecase, command, "INFO", message)

    return service


def getStatusResponseFromCreatedKymaInstance(btpUsecase, instanceName):
    command = "kubectl get ServiceInstance " + instanceName + " -n " + btpUsecase.accountMetadata.get("k8snamespace") + " --kubeconfig " + btpUsecase.accountMetadata.get("kubeconfigpath") + " -o json"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    jsonResult = convertStringToJson(p.stdout.decode())

    return jsonResult
