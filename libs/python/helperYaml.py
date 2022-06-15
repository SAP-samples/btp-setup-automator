import yaml
from libs.python.helperJson import getJsonFromFile


def build_service_instance_yaml_from_parameters(service):

    serviceInstanceTemplate = getJsonFromFile('libs/json/templates/K8s-SERVICE-INSTANCE.json')

    serviceInstanceTemplate.metadata.name = service.instanceName
    serviceInstanceTemplate.spec.serviceOfferingName = service.name
    serviceInstanceTemplate.spec.servicePlanName = service.plan
    serviceInstanceTemplate.spec.externalName = service.instanceName

    if service.parameters is not None:
        serviceInstanceTemplate.spec.parameters = service.parameters
    elif service.serviceparameterfile is not None:
        serviceInstanceTemplate.spec.parameters = getJsonFromFile(service.serviceparameterfile)       

    serviceInstanceYaml = yaml.dump(serviceInstanceTemplate, default_flow_style=False)

    return serviceInstanceYaml


def build_service_binding_yaml_from_parameters():

    serviceBindingTemplate = getJsonFromFile('libs/json/templates/K8s-SERVICE-BINDING.json')

    serviceBindingYaml = yaml.dump(serviceBindingTemplate, default_flow_style=False)

    return serviceBindingYaml


def store_yaml_to_disk(yamlFilePath, yamlContent):
    with open(yamlFilePath, 'w') as outfile:
        yaml.dump(yamlContent, outfile)
    return True
