from libs.python.helperJson import convertStringToJson


def getKymaEnvironmentInfoByClusterName(environmentData, kymaClusterName):

    for entry in environmentData["environmentInstances"]:
        if entry["environmentType"] == "kyma" and entry["name"] == kymaClusterName:
            return entry


def getKymaEnvironmentStatusFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["state"]


def extractKymaDashboardUrlFromEnvironmentDataEntry(environmentDataEntry):
    return environmentDataEntry["dashboardUrl"]


def extractKymaKubeConfigUrlFromEnvironmentDataEntry(environmentDataEntry):
    labelsFromEntry = convertStringToJson(environmentDataEntry["labels"])
    return labelsFromEntry["KubeconfigURL"]
