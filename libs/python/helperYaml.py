import yaml
import os
from libs.python.helperJson import getJsonFromFile


def build_and_store_service_instance_yaml_from_parameters(service, yamlFilePath):

    serviceInstanceTemplate = getJsonFromFile('config/jsonschemas/K8s-SERVICE-INSTANCE.json')

    serviceInstanceTemplate["metadata"]["name"] = service.instancename
    serviceInstanceTemplate["spec"]["serviceOfferingName"] = service.name
    serviceInstanceTemplate["spec"]["servicePlanName"] = service.plan
    serviceInstanceTemplate["spec"]["externalName"] = service.instancename

    if service.parameters is not None:
        serviceInstanceTemplate["spec"]["parameters"] = service.parameters
    elif service.serviceparameterfile is not None:
        serviceInstanceTemplate["spec"]["parameters"] = getJsonFromFile(service.serviceparameterfile)       

    os.makedirs(os.path.dirname(yamlFilePath), exist_ok=True)
    with open(yamlFilePath, "w") as outfile:
        yaml.dump(serviceInstanceTemplate, outfile, default_flow_style=False)

   
def build_and_store_service_binding_yaml_from_parameters(keyname, service, yamlFilePath):

    serviceBindingTemplate = getJsonFromFile('config/jsonschemas/K8s-SERVICE-BINDING.json')

    serviceBindingTemplate["metadata"]["name"] = keyname
    serviceBindingTemplate["spec"]["serviceInstanceName"] = service.instancename
    serviceBindingTemplate["spec"]["secretName"] = keyname

    os.makedirs(os.path.dirname(yamlFilePath), exist_ok=True)
    with open(yamlFilePath, "w") as outfile:
        yaml.dump(serviceBindingTemplate, outfile, default_flow_style=False)
