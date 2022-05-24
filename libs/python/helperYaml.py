import yaml
from libs.python.helperJson import getJsonFromFile


def build_service_instance_yaml_from_parameters():

    serviceInstanceTemplate = getJsonFromFile('libs/json/templates/K8s-SERVICE-INSTANCE.json')

    serviceInstanceYaml = yaml.dump(serviceInstanceTemplate, default_flow_style=False)

    return serviceInstanceYaml


def build_service_binding_yaml_from_parameters():

    serviceBindingTemplate = getJsonFromFile('libs/json/templates/K8s-SERVICE-BINDING.json')

    serviceBindingYaml = yaml.dump(serviceBindingTemplate, default_flow_style=False)

    return serviceBindingYaml


def store_yaml_to_disk(yamlFilePath, yamlContent):
    with open(yamlFilePath, 'w') as outfile:
        outfile.write(yamlContent)
