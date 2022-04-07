import json
import os
import sys
import re
import requests
import logging

log = logging.getLogger(__name__)


def getJsonFromFile(self, filename):
    data = None
    foundError = False
    f = None

    if "http://" in filename or "https://" in filename:
        data = None
        try:
            thisRequest = requests.get(filename)
            data = json.loads(thisRequest.text)
        except Exception as e:
            log.error("please check the json file >" + filename + "<: " + str(e))
            sys.exit(os.EX_DATAERR)
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
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
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
    jsonObject = json.loads(string)
    return jsonObject


def convertJsonToString(json):
    string = json.dumps(json)
    return string


def addKeyValuePair(json, key, value):
    json[key] = value
    return json


def saveJsonToFile(filename, jsonData):
    with open(filename, 'w') as outfile:
        json.dump(jsonData, outfile, indent=2)
    return True


def addKeyValuePairToJsonFile(filename, key, value):
    myJson = getJsonFromFile(None, filename)
    myJson = addKeyValuePair(myJson, key, value)
    saveJsonToFile(filename, myJson)


def convertCloudFoundryCommandOutputToJson(lines):
    dict = []
    positions = []
    keys = []
    # Remove the first 2 lines of the output (don't contain neccessary information)
    lines = lines.split('\n', 2)[-1]

    # Detect the columns of the text table
    # Simply look for three whitespaces as separator
    for line in lines.splitlines():
        keys = re.split(r'\s{3,}', line)
        for key in keys:
            pos = line.find(key)
            positions.append(pos)
        break
    # Remove the first line (the one with the keys)
    dataRows = lines.split('\n', 1)[-1]

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
    lines = lines.split('\n', 2)[-1]

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
            for counter in len(columns):
                value += columns[counter + 1]
            value = value.strip()
            if value == "":
                value = None
            key = key.strip()

        if key is not None and key != "":
            dataInRow = addKeyValuePair(dataInRow, key, value)

    json = dictToJson(dataInRow)
    json = convertStringToJson(json)
    return json
