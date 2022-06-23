import argparse
from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperJson import addKeyValuePairToJsonFile, getJsonFromFile
from libs.python.helperFolders import FOLDER_SCHEMA_LIBS

import getpass
import logging
import sys
import os


log = logging.getLogger(__name__)


def setupParams(myArguments):
    parser = argparse.ArgumentParser()
    if myArguments is not None and myArguments != "":

        allJsonParameters = getJsonFromFile(myArguments)
        for key, value in allJsonParameters.get("properties").items():
            argument = key
            type = value.get("type")
            help = value.get("description")
            default = value.get("default")

            typeIsList = isinstance(type, list)

            if typeIsList:
                for thisType in type:
                    if thisType == "string":
                        type = "string"
                        break
                    if thisType == "boolean":
                        type = "boolean"
                        break
                    if thisType == "integer":
                        type = "integer"
                        break

            if type == "string":
                if "acceptedvalues" in value:
                    parser.add_argument('-' + argument, type=str, help=help, choices=value["acceptedvalues"])
                else:
                    parser.add_argument('-' + argument, type=str, help=help)
            if type == "boolean":
                parser.add_argument('-' + argument, type=bool, help=help)
            if type == "integer":
                parser.add_argument('-' + argument, type=int, help=help)
            if type == "object":
                parser.add_argument('-' + argument, type=str, help=help)
            if type == "array":
                parser.add_argument('-' + argument, type=str, help=help)

        args = parser.parse_args()
        parameterfile = None
        if args.parameterfile is not None and args.parameterfile != "":
            parameterfile = args.parameterfile
        else:
            parameterfile = getDefaultValueForParameter(allJsonParameters, "parameterfile")

        if parameterfile is not None and parameterfile != "":
            myParameters = getJsonFromFile(parameterfile)

            for key in myParameters:
                # Get the default values for the keys of the args object
                valueThroughDirectParameter = getattr(args, key)

                # Get the values in the parameters file
                valueInParametersFile = None
                if key in myParameters:
                    valueInParametersFile = myParameters[key]

                valueToSet = None
                valueDefaultFromParamJson = getDefaultValueForParameter(allJsonParameters, key)

                if valueThroughDirectParameter is not None and valueThroughDirectParameter != "":
                    valueToSet = valueThroughDirectParameter
                else:
                    valueToSet = valueInParametersFile

                # in case no value was set, take the default value defined in the json parameters file
                if valueToSet is None:
                    valueToSet = valueDefaultFromParamJson

                setattr(args, key, valueToSet)

            # in case the parameter file does not include all parameter keys, add the missing ones to the args
            btpSetupAutomatorArguments = FOLDER_SCHEMA_LIBS + "btpsa-parameters.json"
            allJsonParameters = getJsonFromFile(btpSetupAutomatorArguments)
            for key, value in allJsonParameters.get("properties").items():
                default = value.get("default")
                if key not in myParameters:
                    valueToSet = getattr(args, key)
                    if valueToSet is None and default is not None:
                        setattr(args, key, default)
                    else:
                        setattr(args, key, valueToSet)
        else:
            log.error("Missing parameterfile. Can't run the script")
            sys.exit(os.EX_PROTOCOL)

        return args
    return None


def getDefaultValueForParameter(allJsonParameters, myArgument):
    result = None
    for key, value in allJsonParameters.get("properties").items():
        if key == myArgument:
            result = value.get("default")

    return result


def validateJson():
    None


def setupParamsBtpsa():
    jsonSchema = FOLDER_SCHEMA_LIBS + "btpsa-parameters.json"
    args = setupParams(jsonSchema)
    return args


def setupParamsServices():
    serviceArguments = FOLDER_SCHEMA_LIBS + "btpsa-usecase.json"
    args = setupParams(serviceArguments)
    return args


def checkProvidedArguments(btpUsecase):
    usecaseInfo = getJsonFromFile(btpUsecase.usecasefile)
    if "aboutThisUseCase" in usecaseInfo:
        info = usecaseInfo["aboutThisUseCase"]
        log.header("Info about use case to be executed")
        filename = btpUsecase.usecasefile
        if filename is not None:
            log.info("file  : " + filename)
        if "name" in info:
            name = info["name"]
            log.info("name  : " + name)
        if "description" in info:
            description = info["description"]
            log.info("descr.: " + description)

    log.header("Checking provided arguments and files")

    if btpUsecase.loginmethod == "envVariables":

        if btpUsecase.myemail is None or btpUsecase.myemail == "":
            param = "BTPSA_PARAM_MYEMAIL"
            paramValue = getEnvVariableValue(param)
            if paramValue is not None and len(paramValue) > 0:
                btpUsecase.myemail = paramValue
            else:
                log.error("env variable " + param + " for parameter >myemail< was not set. Please set it, or change loginmethod")
                sys.exit(os.EX_DATAERR)

        if btpUsecase.mypassword is None or btpUsecase.mypassword == "":
            param = "BTPSA_PARAM_MYPASSWORD"
            paramValue = getEnvVariableValue(param)
            if paramValue is not None and len(paramValue) > 0:
                btpUsecase.mypassword = paramValue
            else:
                log.error("env variable " + param + " for parameter >mypassword< was not set. Please set it, or change loginmethod")
                sys.exit(os.EX_DATAERR)

        if btpUsecase.globalaccount is None or btpUsecase.globalaccount == "":
            param = "BTPSA_PARAM_GLOBALACCOUNT"
            paramValue = getEnvVariableValue(param)
            if paramValue is not None and len(paramValue) > 0:
                btpUsecase.globalaccount = paramValue
            else:
                log.error("env variable " + param + " for parameter >globalaccount< was not set. Please set it, or change loginmethod")
                sys.exit(os.EX_DATAERR)

    if btpUsecase.loginmethod == "basicAuthentication":
        # Check CREDENTIALS: EMAIL
        while btpUsecase.myemail is None or btpUsecase.myemail == "":
            log.warning("EMAIL ADDRESS MISSING")
            inputMessage = "                      " + "\033[38;5;51m" + \
                "Please enter your email address (hit Enter when done):"
            value = checkUserInput(inputMessage, "text")
            if value is not None:
                btpUsecase.myemail = value
                addKeyValuePairToJsonFile(btpUsecase.parameterfile, "myemail", value)
                log.success("added your email address into your parameters file >" + btpUsecase.parameterfile + "<")
            else:
                btpUsecase.myemail = ""

        # INPUT CREDENTIALS: PASSWORD
        while btpUsecase.mypassword is None or btpUsecase.mypassword == "":
            log.warning("YOU NEED TO PROVIDE YOUR BTP PASSWORD")
            inputMessage = "                      " + "\033[38;5;51m" + \
                "Please enter your BTP password (hit Enter when done):"
            value = checkUserInput(inputMessage, "password")
            if value is not None:
                btpUsecase.mypassword = value
            else:
                btpUsecase.mypassword = ""

    # Check GLOBAL ACCOUNT SUBDOMAIN
    while btpUsecase.globalaccount is None or btpUsecase.globalaccount == "":
        log.warning("GLOBAL ACCOUNT SUBDOMAIN MISSING in your parameter file >" + btpUsecase.parameterfile + "<")
        inputMessage = "                      " + "\033[38;5;51m" + \
            "Please enter your global account subdomain (hit Enter when done):"
        value = checkUserInput(inputMessage, "text")
        if value is not None:
            btpUsecase.globalaccount = value
            addKeyValuePairToJsonFile(btpUsecase.parameterfile, "globalaccount", value)
            log.success("added your global account subdomain into your parameters file >" + btpUsecase.parameterfile + "<")
        else:
            btpUsecase.globalaccount = ""

    return btpUsecase


def checkUserInput(inputMessage, type):
    if type == "password":
        string = getpass.getpass(inputMessage)
    else:
        string = input(inputMessage)

    if string is None:
        return None

    if len(string) == 0:
        return None
    else:
        return string
