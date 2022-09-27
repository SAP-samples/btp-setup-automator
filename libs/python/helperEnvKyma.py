from libs.python.helperGeneric import getTimingsForStatusRequest
from libs.python.helperJson import convertStringToJson, saveJsonToFile, isValidJson
from libs.python.helperYaml import build_and_store_service_binding_yaml_from_parameters, build_and_store_service_instance_yaml_from_parameters
from libs.python.helperCommandExecution import runShellCommand, runShellCommandFlex
import os
import sys
import logging
import time
import base64

log = logging.getLogger(__name__)


def create_kyma_service(btpUsecase, service):

    filepath = "logs/k8s/service-instance/service-instance-" + \
        btpUsecase.accountMetadata.get("subaccountid") + "-" + service.instancename + ".yaml"

    build_and_store_service_instance_yaml_from_parameters(service, filepath)

    command = "kubectl apply -f " + filepath + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Create instance >" + service.instancename + "< for service >" + service.name + \
        "< and plan >" + service.plan + "<" + \
        " in namespace >" + btpUsecase.k8snamespace + "<"

    runShellCommandFlex(btpUsecase, command, "INFO", message, True, True)

    return service

    
def createKymaServiceBinding(btpUsecase, service, keyName):
    filepath = "logs/k8s/service-binding/service-binding-" + \
        btpUsecase.accountMetadata.get("subaccountid") + ".yaml"

    build_and_store_service_binding_yaml_from_parameters(
        keyName, service, filepath)

    command = "kubectl apply -f " + filepath + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Create service binding for service instance> " + \
        service.instancename + " <"

    p = runShellCommandFlex(btpUsecase, command, "INFO", message, True, True)

    if p.returncode == 0:
        command = "kubectl get ServiceBinding " + keyName + " -n " + \
            btpUsecase.k8snamespace + " --kubeconfig " + \
            btpUsecase.kubeconfigpath + " -o json"

        p = runShellCommand(btpUsecase, command, "INFO", None)

        result = convertStringToJson(p.stdout.decode())
        if (btpUsecase.enableAPITest):
            getBindingSecret(btpUsecase, keyName)
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)
    return result


def getBindingSecret(btpUsecase, keyName):
    if not os.path.exists("logs/k8s/bindings"):
        os.mkdir("logs/k8s/bindings")
    bindingfilepath = "logs/k8s/bindings/" + keyName + ".json"  
    command = "kubectl get secrets " + keyName + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + \
        btpUsecase.kubeconfigpath + " -o json"
    message = "Get secret details of service key"    
    p = runShellCommand(btpUsecase, command, "INFO", message)
    data = convertStringToJson(p.stdout.decode())
    for servicekey, servicevalue in data['data'].items():
        d = base64.b64decode(servicevalue)
        data['data'][servicekey] = d.decode('utf-8')
        isJson = isValidJson(data['data'][servicekey])
        if isJson:
            data['data'][servicekey] = convertStringToJson(data['data'][servicekey])
    saveJsonToFile(bindingfilepath, data) 


def deleteKymaServiceBindingAndWait(key, service, btpUsecase):
    deleteKymaServiceBinding(
        key["keyname"], service["instancename"], btpUsecase)

    search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
        btpUsecase, service)
    current_time = 0
    while usecaseTimeout > current_time:
        message = "check if service binding >" + \
            key["keyname"] + "< for service instance >" + \
            service["instancename"] + "< is deleted"
        command = "kubectl get ServiceBinding " + \
            key["keyname"] + " -n " + btpUsecase.k8snamespace + \
            " --kubeconfig " + btpUsecase.kubeconfigpath
        p = runShellCommandFlex(btpUsecase, command,
                                "CHECK", message, False, False)

        output = p.stdout.decode()
        err = p.stderr.decode()
        if output == "" and "NotFound" in err:
            usecaseTimeout = current_time - 1
        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds


def deleteKymaServiceBinding(keyName, instanceName, btpUsecase):
    command = "kubectl delete ServiceBinding " + keyName + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Delete Kyma service binding >" + keyName + \
        "< for service instance >" + instanceName + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def deleteKymaServiceInstance(service, btpUsecase):
    command = "kubectl delete ServiceInstance " + \
        service["instancename"] + " -n " + btpUsecase.k8snamespace + \
        " --kubeconfig " + btpUsecase.kubeconfigpath
    message = "Delete Kyma service instance >" + \
        service["instancename"] + "< from subaccount"
    result = runShellCommand(btpUsecase, command, "INFO", message)

    return result


def extractKymaDashboardUrlFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["dashboardUrl"]


def extractKymaKubeConfigUrlFromEnvironmentDataEntry(environmentDataEntry):
    labelsFromEntry = convertStringToJson(environmentDataEntry["labels"])
    return labelsFromEntry["KubeconfigURL"]


def getKymaEnvironmentInfoByClusterName(environmentData, kymaClusterName):
    for entry in environmentData["environmentInstances"]:
        parametersFromEntry = convertStringToJson(entry["parameters"])
        if entry["environmentType"] == "kyma" and parametersFromEntry["name"] == kymaClusterName:
            return entry


def getKymaEnvironmentStatusFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["state"]


def getKymaEnvironmentIdByClusterName(environmentData, kymaClusterName):
    for entry in environmentData["environmentInstances"]:
        parametersFromEntry = convertStringToJson(entry["parameters"])
        if entry["environmentType"] == "kyma" and parametersFromEntry["name"] == kymaClusterName:
            return entry["id"]


def get_kyma_service_status(btpUsecase, service):
    command = "kubectl get ServiceInstance " + service.instanceName + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + \
        btpUsecase.kubeconfigpath + " | jq .status.ready"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    if p.stdout.decode() == "TRUE":
        return "create succeeded"
    else:
        return "NotReady"


def getStatusResponseFromCreatedKymaInstance(btpUsecase, instanceName):
    command = "kubectl get ServiceInstance " + instanceName + " -n " + \
        btpUsecase.k8snamespace + " --kubeconfig " + \
        btpUsecase.kubeconfigpath + " -o json"

    p = runShellCommand(btpUsecase, command, "INFO", None)

    jsonResult = convertStringToJson(p.stdout.decode())

    return jsonResult


def getKymaServiceDeletionStatus(service, btpUsecase):
    command = "kubectl get ServiceInstance " + \
        service["instancename"] + " -n " + btpUsecase.k8snamespace + \
        " --kubeconfig " + btpUsecase.kubeconfigpath
    p = runShellCommandFlex(btpUsecase, command, "CHECK", None, False, False)
    output = p.stdout.decode()
    err = p.stderr.decode()
    if output == "" and "NotFound" in err:
        return "deleted"
    else:
        return "not deleted"
