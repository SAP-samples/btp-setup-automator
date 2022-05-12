from libs.python.helperCommandExecution import runCommandAndGetJsonResult, runShellCommandFlex
# from libs.python.helperGeneric import save_collected_metadata
from libs.python.helperJson import getJsonFromFile
# import re
# import os
# import sys
import logging

log = logging.getLogger(__name__)


def getMembersForRolecollection(btpUsecase, rolecollection):
    users = []
    for usergroup in rolecollection.get("assignedUserGroupsFromParameterFile"):
        members = getMembersOfUserGroup(btpUsecase, usergroup)
        if members:
            for member in members:
                users.append(member)
        else:
            log.warning("Didn't find any members for user group >" + usergroup + '<. Check the section "usergroups" in your parameters file >' + btpUsecase.parameterfile + "<")
    users = list(dict.fromkeys(users))
    return users


def getMembersForRolecollectionTypeAndLevel(btpUsecase, type, level):
    rolecollections = btpUsecase.definedRoleCollections

    checkType = type is not None
    checkLevel = level is not None

    users = []
    for rolecollection in rolecollections:
        thisType = rolecollection.get("type")
        thisLevel = rolecollection.get("level")
        addMembers = False
        if checkLevel is True and thisLevel == level:
            addMembers = True
        if checkType is True and thisType == type:
            addMembers = True
        if checkType is False and checkLevel is False:
            addMembers = True
        if addMembers is True:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            for member in members:
                users.append(member)
    users = list(dict.fromkeys(users))
    return users


def getSubaccountAdmins(btpUsecase):
    result = "["

    users = getMembersForRolecollectionTypeAndLevel(btpUsecase, "account", None)
    for user in users:
        if user == users[-1]:
            result += '"' + user + '"]'
        else:
            result += '"' + user + '" , '
    return result


def getRoleCollectionsOfServices(btpUsecase):
    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if usecase.get("services") is not None:
        for service in usecase.get("services"):
            if service.get("requiredrolecollections") is not None:
                for rolecollection in service.get("requiredrolecollections"):
                    items.append(rolecollection)

    return items


def getMembersOfUserGroup(btpUsecase, usergroup):
    members = None
    usergroupExists = False

    for thisUserGroup in btpUsecase.usergroups:
        if thisUserGroup.get("name") == usergroup:
            usergroupExists = True
            members = thisUserGroup.get("members")
    if usergroupExists is False:
        log.error("you didn't define a usergroup >" + usergroup + "< in your parameters file >" + btpUsecase.parameterfile + "<. Therefore no members where found.")
    return members


def assignUsergroupsToRoleCollection(btpUsecase, rolecollection):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    assignedUserGroupsFromParameterFile = rolecollection.get("assignedUserGroupsFromParameterFile")

    for usergroup in assignedUserGroupsFromParameterFile:
        members = getMembersOfUserGroup(btpUsecase, usergroup)
        if members:
            for userEmail in members:
                rolecollectioname = rolecollection.get("name")
                message = "assign user >" + userEmail + "< the role collection >" + rolecollectioname + "<"
                command = "btp --format json assign security/role-collection '" + rolecollectioname + "' --to-user '" + userEmail + \
                    "' --create-user-if-missing --subaccount '" + subaccountid + "'"
                thisResult = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)
                thisResult = thisResult


def getSelfDefinedRoleCollections(btpUsecase):
    items = []
    for rolecollection in btpUsecase.definedRoleCollections:
        items.append(rolecollection)

    return items


def getRoleCollectionsOfTypeAndLevel(btpUsecase, type, level):
    rolecollections = btpUsecase.definedRoleCollections
    checkType = type is not None
    checkLevel = level is not None

    result = []
    for rolecollection in rolecollections:
        thisType = rolecollection.get("type")
        thisLevel = rolecollection.get("level")
        add = False
        rightLevel = False
        rightType = False
        if checkLevel is True and thisLevel == level:
            rightLevel = True
        if checkType is True and thisType == type:
            rightType = True
        if checkType is True and checkLevel is True:
            add = rightLevel and rightType
        if checkType is True and checkLevel is False:
            add = rightType
        if checkType is False and checkLevel is True:
            add = rightLevel
        if add is True:
            result.append(rolecollection)

    return result


def assignUsersToGlobalAndSubaccount(btpUsecase):
    subaccountid = btpUsecase.subaccountid

    log.header("Set global account administrators")
    rolecollectionsGlobalAccount = getRoleCollectionsOfTypeAndLevel(btpUsecase, "account", "global account")
    for rolecollection in rolecollectionsGlobalAccount:
        members = getMembersForRolecollection(btpUsecase, rolecollection)
        role = rolecollection.get("name")
        log.info("assign users to global account role >" + role + "<")
        for userEmail in members:
            message = " - assign user >" + userEmail + "<"
            command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing -ga"
            runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

    log.header("Set sub account administrators")
    rolecollectionsSubAccount = getRoleCollectionsOfTypeAndLevel(btpUsecase, "account", "sub account")
    for rolecollection in rolecollectionsSubAccount:
        members = getMembersForRolecollection(btpUsecase, rolecollection)
        role = rolecollection.get("name")
        log.info("assign users to sub account role >" + role + "<")
        for userEmail in members:
            message = " - assign user >" + userEmail + "<"
            command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
            runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)


def assignUsersToEnvironments(btpUsecase):
    environments = btpUsecase.definedEnvironments

    for environment in environments:
        if environment.name == "cloudfoundry":
            org = btpUsecase.org
            cfspacename = btpUsecase.cfspacename

            log.header("Set members of Cloudfoundry org")
            rolecollectionsCloudFoundryOrg = getRoleCollectionsOfTypeAndLevel(btpUsecase, "cloudfoundry", "org")
            for rolecollection in rolecollectionsCloudFoundryOrg:
                members = getMembersForRolecollection(btpUsecase, rolecollection)
                orgRole = rolecollection.get("name")
                log.info("assign users to org role >" + orgRole + "<")
                for admin in members:
                    message = " - user >" + admin + "<"
                    command = "cf set-org-role '" + admin + "' '" + org + "' '" + orgRole + "'"
                    p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + orgRole + "<")

            log.header("Set members of Cloudfoundry space")
            rolecollectionsCloudFoundrySpace = getRoleCollectionsOfTypeAndLevel(btpUsecase, "cloudfoundry", "space")

            for rolecollection in rolecollectionsCloudFoundrySpace:
                members = getMembersForRolecollection(btpUsecase, rolecollection)
                spaceRole = rolecollection.get("name")
                log.info("assign users to space role >" + orgRole + "<")
                for admin in members:
                    message = " - user >" + admin + "<"
                    command = "cf set-space-role '" + admin + "' '" + org + "' '" + cfspacename + "' '" + spaceRole + "'"
                    p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + spaceRole + "<")
