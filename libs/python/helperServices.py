from libs.python.helperJson import getJsonFromFile
from libs.python.helperLog import logtype
import sys
import os
from json import JSONEncoder


class BTPSERVICE:
    def __init__(self, paramDefinitionServices, definedUsecaseService, btpUsecase):
        log = btpUsecase.log
        for parameter in paramDefinitionServices:
            argument = parameter["argument"]
            default = parameter["default"]
            acceptedvalues = None
            if "acceptedvalues" in parameter:
                acceptedvalues = parameter["acceptedvalues"]
            mandatory = parameter["mandatory"]
            paramType = parameter["type"]

            serviceName = "unknown"
            if "name" in definedUsecaseService:
                serviceName = definedUsecaseService["name"]

            setattr(self, argument, default)

            if argument in definedUsecaseService.keys():
                value = definedUsecaseService[argument]
                if acceptedvalues is not None and value not in acceptedvalues:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< was set to >" + value + "<, but allowed values are >" + str(acceptedvalues) + "<\nPlease correct the parameter!"
                    log.write(logtype.ERROR, message)
                    sys.exit(os.EX_DATAERR)
                if mandatory is True and value is None:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< is mandatory, but was not set.\nPlease correct the parameter!"
                    log.write(logtype.ERROR, message)
                    sys.exit(os.EX_DATAERR)
                typeParameter = type(value).__name__
                if paramType != typeParameter:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< should be a >" + paramType + "<, but it's >" + typeParameter + "<\nPlease correct the parameter!"
                    log.write(logtype.ERROR, message)
                    sys.exit(os.EX_DATAERR)
                setattr(self, argument, value)
            else:
                if mandatory is True and default is None:
                    message = "parameter >" + argument + "< for service >" + serviceName + "< is mandatory, but was not set.\nPlease correct the parameter!"
                    log.write(logtype.ERROR, message)
                    sys.exit(os.EX_DATAERR)


# subclass JSONEncoder
class BTPSERVICEEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def readAllServicesFromUsecaseFile(btpUsecase):
    # Initiate class with configured parameters
    paramServicesFile = "libs/json/paramServices.json"
    paramDefinitionServices = getJsonFromFile(None, paramServicesFile)

    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if "services" in usecase:
        for usecaseService in usecase["services"]:
            service = BTPSERVICE(paramDefinitionServices, usecaseService, btpUsecase)
            items.append(service)
    return items
