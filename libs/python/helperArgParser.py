import argparse
from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperJson import addKeyValuePairToJsonFile, getJsonFromFile, saveJsonToFile
import getpass
import logging
import sys
import os

log = logging.getLogger(__name__)


def setupParams(myArguments):
    parser = argparse.ArgumentParser()
    if myArguments is not None and myArguments != "":
        allJsonParameters = getJsonFromFile(None, myArguments)

        for parameter in allJsonParameters:
            argument = parameter["argument"]
            type = parameter["type"]
            help = parameter["help"]
            default = parameter["default"]
            if type == "str":
                if "acceptedvalues" in parameter:
                    parser.add_argument('-' + argument, type=str, help=help, default=default, choices=parameter["acceptedvalues"])
                else:
                    parser.add_argument('-' + argument, type=str, help=help, default=default)
            if type == "bool":
                parser.add_argument('-' + argument, type=bool, help=help, default=default)
            if type == "int":
                parser.add_argument('-' + argument, type=int, help=help, default=default)

        args = parser.parse_args()
        myArgs = assignArgumentsThroughJsonParameterFile(args)
        return myArgs
    return None


def setupParamsBtpsa():
    btpSetupAutomatorArguments = "libs/json/paramBtpSetupAutomator.json"
    args = setupParams(btpSetupAutomatorArguments)
    return args


def setupParamsServices():
    serviceArguments = "libs/json/paramServices.json"
    args = setupParams(serviceArguments)
    return args


def assignArgumentsThroughJsonParameterFile(args):
    if args.parameterfile is not None and args.parameterfile != "":
        myParameters = getJsonFromFile(None, args.parameterfile)

        for key in myParameters:
            # Get the default values for the keys of the args object
            valueThroughDirectParameter = getattr(args, key)

            # Get the values in the parameters file
            valueInParametersFile = None
            if key in myParameters:
                valueInParametersFile = myParameters[key]

            valueToSet = None
            if valueInParametersFile is not None and valueInParametersFile != "":
                valueToSet = valueInParametersFile
            else:
                valueToSet = valueThroughDirectParameter

            setattr(args, key, valueToSet)

        # in case the parameter file does not include all parameter keys, add the missing ones to the args
        btpSetupAutomatorArguments = "libs/json/paramBtpSetupAutomator.json"
        allJsonParameters = getJsonFromFile(None, btpSetupAutomatorArguments)
        for parameter in allJsonParameters:
            key = parameter["argument"]
            if key not in myParameters:
                setattr(args, key, getattr(args, key))

    return args


def createDefaultParametersFile(toolParametersFile):
    if toolParametersFile is not None and toolParametersFile != "":
        allJsonParameters = getJsonFromFile(None, toolParametersFile)
        result = {}

        for parameter in allJsonParameters:
            key = parameter["argument"]
            value = parameter["default"]
            if key != "mypassword":
                result[key] = value

        saveJsonToFile("libs/json/parametersDefault.json", result)


def checkProvidedArguments(btpUsecase):
    usecaseInfo = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
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
