import json
from os import EX_DATAERR
from urllib.request import urlopen
import xmltodict
from subprocess import run, PIPE
from libs.python.helperLog import logtype
import sys

def getJsonFromFile(self, filename):
    log = None 
    if self != None:
        log = self.log

    data = None
    foundError = False
    f = None

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        if log != None:
            log.write( logtype.ERROR, message)
        else:
            print(message)
        foundError = True
    except ValueError as err:
        message ="There is an issue in the json file >" + filename + "<. Issue starts on character position " + str(err.pos) + ": " + err.msg
        if log != None:
            log.write( logtype.ERROR, message)
        else:
            print(message)
        foundError = True
    finally:
        if f != None:
            f.close()
    
    if foundError == True:
        message ="Can't run the use case before the error(s) mentioned above are not fixed"
        if log != None:
            log.write( logtype.ERROR, message)
        else:
            print(message)
        sys.exit(EX_DATAERR)
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

def addKeyValuePair(json,key,value):
    json[key] = value
    return json
    
def saveJsonToFile(filename,jsonData):
    with open(filename, 'w') as outfile:
        json.dump(jsonData, outfile, indent=2) 
    return True

def addKeyValuePairToJsonFile(filename, key, value):
    myJson = getJsonFromFile(None,filename)
    myJson = addKeyValuePair(myJson, key, value)
    saveJsonToFile(filename, myJson)
