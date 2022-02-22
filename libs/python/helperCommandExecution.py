from subprocess import run, PIPE
from libs.python.helperLog import LOGFILE, logtype
from libs.python.helperJson import convertStringToJson, getJsonFromFile
import sys, time

def runShellCommand(btpUsecase, command, format, info):
    return runShellCommandFlex(btpUsecase, command, format, info, True)


def login_cf(btpUsecase):
    accountMetadata= btpUsecase.accountMetadata

    org = accountMetadata["org"]
    usecaseRegion = btpUsecase.region
    myemail = btpUsecase.myemail
    password = btpUsecase.mypassword

    command = "cf login -a \"https://api.cf." + usecaseRegion + ".hana.ondemand.com\" -o \"" + org + "\" -u \"" + myemail + "\" -p \"" + password + "\"" 
    ## If a space is already there, attach the space name to the login to target the space
    if "cfspacename" in accountMetadata and accountMetadata["cfspacename"] != None and accountMetadata["cfspacename"] != "":
        command = "cf login -a \"https://api.cf." + usecaseRegion + ".hana.ondemand.com\" -o \"" + org + "\" -s \"" + accountMetadata["cfspacename"] + "\" -u \"" + myemail + "\" -p \"" + password + "\"" 
    p = runShellCommand(btpUsecase, command, logtype.INFO, "Logging-in to your CF environment in the org >" + org + "< for your user >" + myemail + "<")

def login_btp(btpUsecase):

    myemail = btpUsecase.myemail
    password = btpUsecase.mypassword
    globalaccount = btpUsecase.globalaccount

    command = "btp login --url \"https://cpcli.cf.eu10.hana.ondemand.com\" --subdomain \"" + globalaccount + "\" --user \"" + myemail + "\" --password \"" + password + "\""
    p = runShellCommand(btpUsecase, command, logtype.INFO, "Logging-in to your global account with subdomain ID >" + globalaccount + "< for your user >" + myemail + "<")


def runShellCommandFlex(btpUsecase, command, format, info, exitIfError):
    log = btpUsecase.log
    if info != None:
        log.write( format, info)
    
    # Check whether we are calling a btp or cf command
    # If yes, we should initiate first a re-login, if necessary
    checkIfReLoginNecessary(btpUsecase, command)

    foundPassword = False
    if btpUsecase.logcommands == True:
        #Avoid to show any passwords in the log
        passwordStrings = ["password " , " -p " , " --p "]
        for passwordString in passwordStrings:
            if passwordString in command :
                commandToBeLogged = command[0:command.index(passwordString) + len(passwordString) + 1] + "xxxxxxxxxxxxxxxxx"
                log.write( logtype.COMMAND, commandToBeLogged)
                foundPassword = True
                break
        if foundPassword == False:
            log.write( logtype.COMMAND, command)
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    output = p.stdout.decode()
    error = p.stderr.decode()
    returnCode = p.returncode

    if (returnCode == 0 or exitIfError == False):
        return p
    else:
        output = p.stdout.decode()
        error = p.stderr.decode()
        log.write( logtype.ERROR, output)
        log.write( logtype.ERROR, error)
        sys.exit(returnCode)

def checkIfReLoginNecessary(btpUsecase,command):
    log = btpUsecase.log
    # time in seconds for re-login
    ELAPSEDTIMEFORRELOGIN = 30 * 60

    reLogin = False
    elapsedTime = 0
    currentTime = time.time()

    if command[0:9] == "btp login":
        btpUsecase.timeLastCliLogin = currentTime
        return None

    if command[0:8] == "cf login":
        btpUsecase.timeLastCliLogin = currentTime
        return None

    if btpUsecase.timeLastCliLogin == None:
       btpUsecase.timeLastCliLogin = currentTime

    elapsedTime = currentTime - btpUsecase.timeLastCliLogin

    if elapsedTime > ELAPSEDTIMEFORRELOGIN:
        reLogin = True
    else:
        reLogin = False

    if command[0:4] == "btp " and command[0:9] != "btp login" and reLogin == True:
        minutesPassed = "{:.2f}".format(elapsedTime/60)
        log.write( logtype.WARNING, "executing a re-login in BTP CLI and CF CLI as the last login happened more than >" + minutesPassed + "< minutes ago")
        login_btp(btpUsecase)
        login_cf(btpUsecase)
        btpUsecase.timeLastCliLogin = currentTime

    if command[0:3] == "cf " and command[0:8] != "cf login"and reLogin == True:
        minutesPassed = "{:.2f}".format(elapsedTime/60)
        log.write( logtype.WARNING, "executing a re-login in BTP CLI and CF CLI as the last login happened more than >" + minutesPassed + "< minutes ago")
        login_btp(btpUsecase)
        login_cf(btpUsecase)
        btpUsecase.timeLastCliLogin = currentTime


def runCommandAndGetJsonResult(btpUsecase, command, format, message):
    p = runShellCommand(btpUsecase, command, format, message)
    list = p.stdout.decode()
    list = convertStringToJson(list)
    return list

def executeCommandsFromUsecaseFile(btpUsecase, message, jsonSection):
    log = btpUsecase.log
    usecaseDefinition  = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)


    if jsonSection in usecaseDefinition and len(usecaseDefinition[jsonSection]) > 0 :
        commands = usecaseDefinition[jsonSection]
        log.write( logtype.HEADER, message)
    
        for command in commands:
            message = command["description"]
            thisCommand = command["command"]
            log.write(logtype.HEADER, "COMMAND EXECUTION: " + message)
            p = runShellCommand(btpUsecase, thisCommand, logtype.INFO, "Executing the following commands:\n" + thisCommand + "\n")
            result = p.stdout.decode()
            log.write( logtype.SUCCESS, result)
