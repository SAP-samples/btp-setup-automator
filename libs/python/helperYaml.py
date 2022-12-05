import yaml
import os
from libs.python.helperJson import getJsonFromFile
from libs.python.helperFolders import FOLDER_K8S_YAML_TEMPLATES


def build_and_store_service_instance_yaml_from_parameters(service, yamlFilePath):

    templatePath = FOLDER_K8S_YAML_TEMPLATES + 'K8s-SERVICE-INSTANCE.json'
    # local access - no auth needed
    serviceInstanceTemplate = getJsonFromFile(templatePath)

    serviceInstanceTemplate["metadata"]["name"] = service.instancename
    serviceInstanceTemplate["spec"]["serviceOfferingName"] = service.name
    serviceInstanceTemplate["spec"]["servicePlanName"] = service.plan
    serviceInstanceTemplate["spec"]["externalName"] = service.instancename

    if service.labels is not None:
        serviceInstanceTemplate["metadata"]["labels"] = service.labels

    if service.parameters is not None:
        serviceInstanceTemplate["spec"]["parameters"] = service.parameters
    elif service.serviceparameterfile is not None:
        serviceInstanceTemplate["spec"]["parameters"] = getJsonFromFile(
            service.serviceparameterfile)

    os.makedirs(os.path.dirname(yamlFilePath), exist_ok=True)
    with open(yamlFilePath, "w") as outfile:
        yaml.dump(serviceInstanceTemplate, outfile, default_flow_style=False)


def build_and_store_service_binding_yaml_from_parameters(keyname, service, yamlFilePath, keyLabels):

    templatePath = FOLDER_K8S_YAML_TEMPLATES + 'K8s-SERVICE-BINDING.json'
    # local access no auth needed
    serviceBindingTemplate = getJsonFromFile(templatePath)

    serviceBindingTemplate["metadata"]["name"] = keyname
    
    if keyLabels is not None:
        serviceBindingTemplate["metadata"]["labels"] = keyLabels

    serviceBindingTemplate["spec"]["serviceInstanceName"] = service.instancename
    serviceBindingTemplate["spec"]["secretName"] = keyname

    os.makedirs(os.path.dirname(yamlFilePath), exist_ok=True)
    with open(yamlFilePath, "w") as outfile:
        yaml.dump(serviceBindingTemplate, outfile, default_flow_style=False)
