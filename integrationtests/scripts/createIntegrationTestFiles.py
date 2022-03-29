import json
import sys
import os
import glob

myemail = "EMAIL"
globalaccount = "GLOBALACCOUNT"
# myemail = sys.argv[1]
# globalaccount = sys.argv[2]

LOCALFOLDERLOGS = "C:\\Users\\I550309\\Desktop"
INTEGRATIONTESTNAME = "integrationtestExecute.sh"


def getJsonFromFile(filename):
    data = None
    foundError = False

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        print("Can't open json file >" + filename + "<")
        foundError = True
    except ValueError as err:
        print("There is an issue in the json file >" + filename + "<. Issue starts on character position " + str(err.pos) + ": " + err.msg)
        foundError = True
    finally:
        f.close()

    if foundError is True:
        print("Can't run the use case before the error(s) mentioned above are not fixed")
        sys.exit(os.EX_DATAERR)
    return data


def buildStringForDockerBuild(containerName, containerDefinition):
    result = "docker image build  -t \"" + containerName + "\":latest -f \"config/containerdefinitions/" + containerDefinition + "/Dockerfile\"  ."
    return result


def buildStringForDockerRun(containerName, containerDefinition):
    logFolder = "${folderLogFile}/"
    indent = " " * 24

    # result = "docker container run -e BTPSETUPAUTOMATOR_VERSION=\"$(git describe --long --tags  --always)\" --rm  -it -d --name \"" + containerName + "\" \\\n"
    # result += indent + "--mount type=bind,source=\"" + logFolder + "\",target=\"/home/user/log/\" \\\n"
    # result += indent + "\"" + containerName + "\"\n"

    result = "docker container run -e BTPSETUPAUTOMATOR_VERSION=\"$(git describe --long --tags  --always)\" --rm  -it -d --name \"" + containerName + "\" \\\n"
    result += indent + "--mount type=bind,source=\"" + logFolder + "\",target=\"/home/user/log/\" \\\n"
    result += indent + "\"ghcr.io/sap-samples/btp-setup-automator:main\"\n"

    return result


def buildStringForDockerExecute(containerName, commands):
    result = "docker exec --workdir \"/home/user/\" "
    result += "\"" + containerName + "\" " + commands
    return result


def deriveFileNames(paramFile, prefix):
    logFile = None
    metadataFile = None

    filename = os.path.basename(paramFile)
    (filenameWithoutSuffix, suffix) = os.path.splitext(filename)

    dirPrefix = "/home/user/log/"
    logFile = dirPrefix + prefix + ".log"
    metadataFile = dirPrefix + prefix + "_metadata.json"

    return filenameWithoutSuffix, logFile, metadataFile


def writeFile(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()


def makeFileExecutable(file):
    mode = os.stat(file).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(file, mode)

###############################################################################


result = "#!/usr/bin/env bash\n\n"
result += "folderLogFile=\"" + LOCALFOLDERLOGS + "/log/$(date \"+%Y-%m-%d\")/\"\n"
result += "mkdir -p \"${folderLogFile}\"\n"
result += "docker system prune -a -f\n"
result += "\n"

allParameterFiles = glob.glob("integrationtests/parameterfiles/*.json")
allParameterFiles.sort()

i = 0
integrationtestName = "btpsa-integrationtest"


result += buildStringForDockerRun(integrationtestName, "btp-setup-automator") + "\n"
indent = " " * 58

for thisParameterFile in allParameterFiles:
    i = i + 1
    prefix = "integrationtest" + "{:02d}".format(i)
    myIntegrationtestName, logFile, metadataFile = deriveFileNames(thisParameterFile, prefix)

    jsonParameterFile = getJsonFromFile(thisParameterFile)

    result += "#" * (100 + len(integrationtestName)) + "\n"
    result += "# BTPSA integration test for use case file\n"
    result += "# " + jsonParameterFile["usecasefile"] + "<" + "\n"
    result += "#" * (100 + len(integrationtestName)) + "\n"

    commands = "./btpsa -parameterfile 'integrationtests/parameterfiles" + thisParameterFile.replace("../../", "") + "' \\\n"
    commands += indent + " -logfile '" + logFile + "' \\\n"
    commands += indent + " -metadatafile '" + metadataFile + "' \\\n"
    if "loginmethod" in jsonParameterFile and jsonParameterFile["loginmethod"] != "sso":
        commands += indent + " -myemail '" + myemail + "' \\\n"

    if "globalaccount" in jsonParameterFile:
        commands += indent + " -globalaccount '" + jsonParameterFile["globalaccount"] + "' \\\n"
    else:
        commands += indent + " -globalaccount '" + globalaccount + "' \\\n"

    commands += indent + " -mypassword $(cat cred.txt)"

    result += buildStringForDockerExecute(integrationtestName, commands) + "\n"

result += "docker container stop  " + integrationtestName + "\n"
result += "docker container rm -f " + integrationtestName + "\n"
result += "\n"

writeFile(INTEGRATIONTESTNAME, result)
makeFileExecutable(INTEGRATIONTESTNAME)
