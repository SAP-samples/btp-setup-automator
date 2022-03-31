from libs.python.helperCommandExecution import runShellCommand
from libs.python.helperJson import addKeyValuePair, convertStringToJson, saveJsonToFile, dictToJson

import os
import sys
import requests
import base64
import inquirer
import logging

log = logging.getLogger(__name__)


def runTrustFlow(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata

    if "createdServiceInstances" in accountMetadata:
        for service in accountMetadata["createdServiceInstances"]:
            if service["name"] == "xsuaa" and service["plan"] == "apiaccess":
                log.info("SETTING UP TRUST")
                log.header("SETTING UP TRUST")
                if "instancename" in service and "createdServiceKeys" in service:
                    accountMetadata = addKeyValuePair(
                        accountMetadata, "trustSetupXSUAA", [])
                    for key in service["createdServiceKeys"]:
                        log.info("using XSUAA service key >" + key["keyname"] + "<")
                        if "payload" in key:
                            payload = key["payload"]

                            authClientId = payload["clientid"]
                            authClientSecret = payload["clientsecret"]

                            log.info("get access token for XSUAA")
                            resultApiAccessToken = get_api_access_token_for_xsuaa(btpUsecase, payload["url"] + "/oauth/token", authClientId, authClientSecret)
                            accessToken = resultApiAccessToken["access_token"]

                            log.info("get list of IAS tenants that the subaccount has access to")
                            resultIasTenants = get_list_of_ias_tenants(btpUsecase, payload["apiurl"] + "/sap/rest/identity-providers/ias", accessToken)

                            log.info("create own IDP")
                            resultOwnIDP = createOwnIDP(
                                btpUsecase, payload["apiurl"] + "/sap/rest/identity-providers", accessToken, resultIasTenants)

                            # if "usersToCreateOnIDP" in usecase:
                            #     for user in usecase["usersToCreateOnIDP"]:
                            #         email = user["email"]
                            #         log.info("create user >" + email + "< on IDP")
                            #         password = "initial123456"
                            #         resultUserCreation = registerUserOnIDP(btpUsecase, payload["url"] + "/oauth/token", authClientId, authClientSecret, email, password)

                            item = {"service_key": key["keyname"], "tokenDetails": resultApiAccessToken,
                                    "availableIasTenants": resultIasTenants, "ownIDP": resultOwnIDP}
                            accountMetadata["trustSetupXSUAA"].append(item)

                    filename = btpUsecase.metadatafile
                    saveJsonToFile(filename, accountMetadata)

                else:
                    log.warning("couldn't execute trust flow, as instance name and/or service key for the XSUAA service was not found!")


def get_cf_service_key(btpUsecase, instanceName, keyName):
    result = None

    command = "cf create-service-key \"" + instanceName + "\" \"" + keyName + "\""
    message = "create service key from XSUAA instance >" + instanceName + "< for keyname >" + keyName + "<"
    p = runShellCommand(btpUsecase, command, "INFO", message)
    returnCode = p.returncode

    if returnCode == 0:
        command = "cf service-key \"" + instanceName + "\" \"" + keyName + "\""
        message = "get service key for instance >" + \
            instanceName + "< and keyname >" + keyName + "<"
        response = runShellCommand(btpUsecase, command, "CHECK", message)
        # Delete the first 2 lines of the CF result string as they don't contain json data
        result = response.stdout.decode()
        result = result.split('\n', 2)[-1]
        result = convertStringToJson(result)
    else:
        log.error("can't create service key!")
        sys.exit(os.EX_DATAERR)
    return result


def delete_cf_service_key(btpUsecase, instanceName, keyName):
    command = "cf delete-service-key  \"" + \
        instanceName + "\" \"" + keyName + "\" -f"
    message = "delete service key from instance >" + \
        instanceName + "< for key >" + keyName + "<"
    runShellCommand(btpUsecase, command, "INFO", message)


def get_api_access_token_for_xsuaa(btpUsecase, authClientUrl, authClientId, authClientSecret):
    result = None
    myData = {'grant_type': 'client_credentials', 'client_id': authClientId, 'client_secret': authClientSecret}

    try:
        log.info("sending a POST request to url >" + authClientUrl + "< with the data >" + str(myData) + "<")
        p = requests.post(authClientUrl, data=myData, headers={"content-type": "application/x-www-form-urlencoded"})
        log.success("fetched API access token for XSUAA")
        result = p.json()
    except:
        result = None
    return result


def get_list_of_ias_tenants(btpUsecase, url, accessToken):
    result = None

    try:
        log.info("sending a GET request to url >" + url + "< with the access token")
        p = requests.get(url, headers={"Authorization": "bearer " + accessToken})
        result = p.json()
        log.success("fetched list of ias tenants assigned to this subaccount")
    except:
        result = None
    return result


def createOwnIDP(btpUsecase, url, accessToken, resultIasTenants):
    result = None
    host = None

    host = None
    if btpUsecase.iashost is None or btpUsecase.iashost == "":
        message = "Did not find parameter >iashost< in the parameters file. Will ask you which one to take."
        log.warning(message)

        myChoices = []
        for tenant in resultIasTenants:
            myChoices.append(tenant["host"])
        questions = [inquirer.List('iashost', message="Which IAS host do you want to use? Select with the arrow keys and hit enter", choices=myChoices)]
        answers = inquirer.prompt(questions)
        host = answers["iashost"]
        log.info("you've selected the IAS tenant >" + host + "<")

    if btpUsecase.iashost is not None and btpUsecase.iashost != "":
        iasHostInUsecaseConfig = btpUsecase.iashost
        for thisHost in resultIasTenants:
            myHost = thisHost["host"]
            if myHost == iasHostInUsecaseConfig:
                host = myHost
                break

    if host is not None and host != "":
        log.info("will establish trust with IAS tenant >" + host + "<")
        myData = {"type": "oidc1.0", "config": {"iasTenant": {"host": host}}}
        headers = {'Content-Type': 'application/json', 'Authorization': 'bearer ' + accessToken, 'Content-Type': 'application/json'}
        myData = dictToJson(myData)
        try:
            log.info("sending a POST request to url >" + url + "< with the data >" + str(myData) + "<")
            p = requests.post(url, data=myData, headers=headers)
            result = p.json()
            log.success("created own IDP")
            return result
        except:
            result = None
    else:
        log.warning( "could not establish trust to IAS")
    return result


def registerUserOnIDP(btpUsecase, url, clientId, clientSecret, idpUserName, password):
    result = None

    clientIdSecret = clientId + ":" + clientSecret

    clientIdSecretEncoded = base64.b64encode(clientIdSecret.encode('ascii'))
    clientIdSecretDecoded = clientIdSecretEncoded.decode('ascii')

    log.info("clientIdSecret       : >" + clientIdSecret + "<")
    log.info("clientIdSecretDecoded: >" + str(clientIdSecretEncoded) + "<")

    myData = "username=" + idpUserName + "&password=" + password + \
        "&grant_type=password&login_hint=%7B%22origin%22%3A%22sap.custom%22%7D"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Accept": "application/json", "Authorization": "Basic " + clientIdSecretDecoded}
    log.info("myData: >" + myData + "<")

    try:
        log.info("sending a POST request to url >" + url + "< to create a user on the IDP")
        p1 = requests.post(url, data=myData, headers=headers)
        log.success("added user >" + idpUserName + "< to your IDP")
        result = p1.json()
    except:
        result = None
    return result
