import json
import os
import sys
import re
from requests.auth import HTTPBasicAuth
import requests
import logging
from libs.python.helperDrawio import getUseCaseDataFromDrawIoFile
import os.path

log = logging.getLogger(__name__)


def getJsonFromFile(
    filename,
    externalConfigAuthMethod=None,
    externalConfigUserName=None,
    externalConfigPassword=None,
    externalConfigToken=None,
):
    data = None
    thisRequest = None
    foundError = False
    f = None

    extension = os.path.splitext(filename)[1][1:]
    if extension == "drawio":
        data = getUseCaseDataFromDrawIoFile(filename)
        result = convertStringToJson(data)
        return result

    if "http://" in filename or "https://" in filename:
        if "http://" in filename:
            log.warning(
                "Using http instead of https for url: "
                + filename
                + ". This is not recommended. Support will be removed in next major release!"
            )

        data = None
        try:
            if (
                externalConfigAuthMethod == "basicAuthentication"
                and externalConfigUserName is not None
                and externalConfigPassword is not None
            ):
                basic = HTTPBasicAuth(externalConfigUserName, externalConfigPassword)
                thisRequest = requests.get(filename, auth=basic)
            elif (
                externalConfigAuthMethod == "token" and externalConfigToken is not None
            ):
                thisRequest = requests.get(
                    filename, headers={"Authorization": "Bearer " + externalConfigToken}
                )
            else:
                thisRequest = requests.get(filename)
        except Exception as e:
            log.error("please check the json file >" + filename + "<: " + str(e))
            sys.exit(os.EX_DATAERR)

        data = json.loads(thisRequest.text)
        return data

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    except ValueError as err:
        message = (
            "There is an issue in the json file >"
            + filename
            + "<. Issue starts on character position "
            + str(err.pos)
            + ": "
            + err.msg
        )
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = (
            "Can't run the use case before the error(s) mentioned above are not fixed"
        )
        if log is not None:
            log.error(message)
        else:
            print(message)
        sys.exit(os.EX_DATAERR)
    return data


def dictToString(dict):
    return json.dumps(dict)


def dictToJson(dict):
    return json.dumps(dict, indent=2)


def convertStringToJson(string):
    result = None
    if string is not None and len(string) > 0:
        result = json.loads(string)
    return result


def addKeyValuePair(json, key, value):
    json[key] = value
    return json


def saveJsonToFile(filename, jsonData):
    with open(filename, "w") as outfile:
        json.dump(jsonData, outfile, indent=2)
    return True


def addKeyValuePairToJsonFile(filename, key, value):
    myJson = getJsonFromFile(filename)
    myJson = addKeyValuePair(myJson, key, value)
    saveJsonToFile(filename, myJson)


def convertCloudFoundryCommandOutputToJson(lines, numberOfLinesToRemove: int = 2):
    dict = []
    positions = []
    keys = []
    # Remove the first 2 lines of the output (don't contain necessary information)
    lines = lines.split("\n", numberOfLinesToRemove)[-1]

    # Detect the columns of the text table
    # Simply look for three whitespaces as separator
    for line in lines.splitlines():
        keys = re.split(r"\s{3,}", line)
        for key in keys:
            pos = line.find(key)
            positions.append(pos)
        break
    # Remove the first line (the one with the keys)
    dataRows = lines.split("\n", 1)[-1]

    for row in dataRows.splitlines():
        i = 0
        dataInRow = convertStringToJson("{}")
        for key in keys:
            posStart = positions[i]
            posEnd = len(row)
            if i + 1 < len(positions):
                posEnd = positions[i + 1]
            value = row[posStart:posEnd]
            value = value.strip()
            dataInRow = addKeyValuePair(dataInRow, key, value)
            i = i + 1
        dict.append(dataInRow)

    json = dictToJson(dict)
    json = convertStringToJson(json)
    return json


def convertCloudFoundryCommandForSingleServiceToJson(lines):
    # Remove the first 2 lines of the output (don't contain neccessary information)
    lines = lines.split("\n", 2)[-1]

    # Detect the columns of the text table
    # Simply look for three whitespaces as separator
    dataInRow = convertStringToJson("{}")
    for line in lines.splitlines():
        columns = re.split(": ", line)
        key = None
        value = None
        if len(columns) == 2:
            key = columns[0]
            value = columns[1]
            value = value.strip()
            if value == "":
                value = None
            key = key.strip()
        if len(columns) > 2:
            key = columns[0]
            value = ""
            for counter in columns:
                value += counter
            value = value.strip()
            if value == "":
                value = None
            key = key.strip()

        if key is not None and key != "":
            dataInRow = addKeyValuePair(dataInRow, key, value)

    json = dictToJson(dataInRow)
    json = convertStringToJson(json)
    return json
