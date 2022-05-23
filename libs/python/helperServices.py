from libs.python.helperJson import getJsonFromFile
import sys
import os
from json import JSONEncoder
import logging

log = logging.getLogger(__name__)


class BTPSERVICE:
    def __init__(self, paramDefinitionServices, definedUsecaseService, btpUsecase):
        for key, value in paramDefinitionServices.items():
            argument = key
            default = value.get("default")
            acceptedvalues = None
            if "acceptedvalues" in value:
                acceptedvalues = value.get("acceptedvalues")
            mandatory = value.get("mandatory")
            paramType = value.get("type")

            serviceName = "unknown"
            if "name" in definedUsecaseService:
                serviceName = definedUsecaseService.get("name")

            setattr(self, argument, default)

            if argument in definedUsecaseService.keys():
                value = definedUsecaseService[argument]
                if acceptedvalues is not None and value not in acceptedvalues:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< was set to >" + value + "<, but allowed values are >" + str(acceptedvalues) + "<\nPlease correct the parameter!"
                    log.error(message)
                    sys.exit(os.EX_DATAERR)
                if mandatory is True and value is None:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< is mandatory, but was not set.\nPlease correct the parameter!"
                    log.error(message)
                    sys.exit(os.EX_DATAERR)
                typeParameter = type(value).__name__

                if type(paramType).__name__ == "str":
                    thisType = getPythonClassForJsonSchemaType(paramType)
                    if thisType != typeParameter:
                        message = "parameter >" + argument + "< for service >" + serviceName + "< should be a >" + paramType + "<, but it's >" + typeParameter + "<\nPlease correct the parameter!"
                        log.error(message)
                        sys.exit(os.EX_DATAERR)

                if type(paramType).__name__ == "list":
                    foundType = False
                    for thisParamType in paramType:
                        thisType = getPythonClassForJsonSchemaType(thisParamType)
                        if thisType in typeParameter:
                            foundType = True
                            break
                    if foundType is False:
                        message = "parameter >" + argument + "< for service >" + serviceName + "< is of type >" + typeParameter + "<, but only the following types are allowed >" + str(paramType) + "<\nPlease correct the parameter!"
                        log.error(message)
                        sys.exit(os.EX_DATAERR)

                setattr(self, argument, value)
            else:
                if mandatory is True and default is None:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< is mandatory, but was not set.\nPlease correct the parameter!"
                    log.error(message)
                    sys.exit(os.EX_DATAERR)


def getPythonClassForJsonSchemaType(jsonType):
    # Map the json schema type to the python variable types
    if jsonType:
        if jsonType == "string":
            return "str"
        if jsonType == "integer":
            return "int"
        if jsonType == "object":
            return "dict"
        if jsonType == "array":
            return "list"

    log.warning("not able to map the jsonType >" + jsonType + "< to a python class")
    return None


# subclass JSONEncoder
class BTPSERVICEEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def readAllServicesFromUsecaseFile(btpUsecase):
    # Initiate class with configured parameters
    jsonSchema = "schemas/btpsa-usecase.json"
    paramDefinitionServices = getJsonFromFile(None, jsonSchema)

    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if "services" in usecase:
        for usecaseService in usecase.get("services"):
            serviceParameterDefinition = getServiceParameterDefinition(paramDefinitionServices)
            service = BTPSERVICE(serviceParameterDefinition, usecaseService, btpUsecase)
            items.append(service)
    return items


def getServiceParameterDefinition(paramDefinitionServices):
    result = None
    parametersForServices = paramDefinitionServices.get("properties").get("services")
    for key, value in parametersForServices.items():
        if key == "items":
            result = value.get("properties")
            break
    return result
