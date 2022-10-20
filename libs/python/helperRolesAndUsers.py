from libs.python.helperCommandExecution import runCommandAndGetJsonResult, runShellCommandFlex, runShellCommand
# from libs.python.helperGeneric import save_collected_metadata
from libs.python.helperJson import getJsonFromFile
# import re
# import os
# import sys
import logging

log = logging.getLogger(__name__)


def getMembersForRolecollection(btpUsecase, rolecollection):
    users = []
    users.append(btpUsecase.myemail)
    if rolecollection:
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
    users.append(btpUsecase.myemail)
    if rolecollections:
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
    if users:
        for user in users:
            if user == users[-1]:
                result += '"' + user + '"]'
            else:
                result += '"' + user + '" , '
    else:
        result = "[]"

    return result


def getRoleCollectionsOfServices(btpUsecase):
    usecase = getJsonFromFile(btpUsecase.usecasefile)
    items = []
    if usecase.get("services") is not None:
        for service in usecase.get("services"):
            if service.get("requiredrolecollections") is not None:
                for rolecollection in service.get("requiredrolecollections"):
                    items.append(rolecollection)

    return items


def getMembersOfUserGroup(btpUsecase, usergroup):
    members = []
    members.append(btpUsecase.myemail)
    usergroupExists = False

    if btpUsecase.myusergroups and usergroup:

        if btpUsecase.myusergroups:
            for thisUserGroup in btpUsecase.myusergroups:
                if thisUserGroup.get("name") == usergroup:
                    usergroupExists = True
                    theseMembers = thisUserGroup.get("members")
                    if theseMembers:
                        for thisMember in theseMembers:
                            members.append(thisMember)
                        members = list(dict.fromkeys(members))

            if usergroupExists is False:
                log.error("you didn't define a usergroup >" + usergroup + "< in your parameters file >" + btpUsecase.parameterfile + "<. Therefore no members where found.")
        else:
            log.warning("didn't find user group >" + usergroup + "< as no usergroups defined in your parameters file >" + btpUsecase.parameterfile + "<")

    return members


def assignUsergroupsToRoleCollection(btpUsecase, rolecollection):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    roleCollectionIsString = isinstance(rolecollection, str)
    roleCollectionIsList = isinstance(rolecollection, dict)

    if roleCollectionIsList:
        assignedUserGroupsFromParameterFile = rolecollection.get("assignedUserGroupsFromParameterFile")

        for usergroup in assignedUserGroupsFromParameterFile:
            members = getMembersOfUserGroup(btpUsecase, usergroup)
            if members:
                rolecollectioname = rolecollection.get("name")
                log.info("assign users the role collection >" + rolecollectioname + "<")
                for userEmail in members:
                    message = " - user >" + userEmail + "<"
                    command = "btp --format json assign security/role-collection '" + rolecollectioname + "' --to-user '" + userEmail + \
                        "' --create-user-if-missing --subaccount '" + subaccountid + "'"
                    thisResult = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)
                    thisResult = thisResult
    if roleCollectionIsString:
        log.warning("YOU ARE USING A LEGACY CONFIGURATION FOR ASSIGING USERS TO ROLE COLLECTIONS!")
        log.warning("Please change your parameters file and your usecase file accordingly.")
        log.warning("Checkout the default parameters file and the other released use cases to understand how to do it.")


def getSelfDefinedRoleCollections(btpUsecase):
    items = []
    if btpUsecase.definedRoleCollections:
        for rolecollection in btpUsecase.definedRoleCollections:
            items.append(rolecollection)

    return items


def getRoleCollectionsOfTypeAndLevel(btpUsecase, type, level):
    rolecollections = btpUsecase.definedRoleCollections
    checkType = type is not None
    checkLevel = level is not None

    result = []
    if rolecollections:
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

    log.header("Set administrators for BTP global account")
    rolecollectionsGlobalAccount = getRoleCollectionsOfTypeAndLevel(btpUsecase, "account", "global account")
    if rolecollectionsGlobalAccount:
        for rolecollection in rolecollectionsGlobalAccount:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            role = rolecollection.get("name")
            log.info("assign users to global account role >" + role + "<")
            for userEmail in members:
                message = " - assign user >" + userEmail + "<"
                command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing -ga"
                runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

    log.header("Set administrators for sub account")
    rolecollectionsSubAccount = getRoleCollectionsOfTypeAndLevel(btpUsecase, "account", "sub account")
    if rolecollectionsSubAccount:
        for rolecollection in rolecollectionsSubAccount:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            role = rolecollection.get("name")
            log.info("assign users to sub account role >" + role + "<")
            for userEmail in members:
                message = " - assign user >" + userEmail + "<"
                command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
                runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)


def assignUsersToCustomRoleCollections(btpUsecase):

    subaccountid = btpUsecase.subaccountid

    rolecollectionsCustom = getRoleCollectionsOfTypeAndLevel(btpUsecase, "custom", None)
    if rolecollectionsCustom:
        for rolecollection in rolecollectionsCustom:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            rolecollectioname = rolecollection.get("name")
            log.info("assign users to custom role collection >" + rolecollectioname + "<")

            message = "Check if role collection >" + rolecollectioname + "< already exists"
            command = "btp get security/role-collection '" + rolecollectioname + "'"
            p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
            result = p.stdout.decode()
            if not result:
                errormessage = p.stderr.decode()
                if "error: No entity found with values" in errormessage:
                    message = "Assign role collection >" + rolecollectioname
                    command = "btp create security/role-collection '" + rolecollectioname + "' --description  '" + rolecollectioname + "' --subaccount '" + subaccountid + "'"
                    runShellCommand(btpUsecase, command, "INFO", message)

                    if rolecollection["assignedRoles"]:
                        # Get role data from btp for subaccount
                        command = "btp --format json list security/role --subaccount '" + subaccountid + "'"
                        roleSecDataJson = runCommandAndGetJsonResult(btpUsecase, command, "INFO", "Get roles for subaccount")

                    for role in rolecollection["assignedRoles"]:
                        message = "Assign role " + role + " to role collection " + rolecollectioname

                        roleAppId = None
                        roleTemplate = None

                        # Fetch additional role data from roleSecDataJson
                        for roleSecData in roleSecDataJson:
                            if roleSecData["name"] == role:
                                roleAppId = roleSecData["roleTemplateAppId"]
                                roleTemplate = roleSecData["roleTemplateName"]
                                break

                        if roleAppId is None or roleTemplate is None:
                            log.error("Could not find role data for role " + role)
                            break

                        command = "btp add security/role '" + role + "' --to-role-collection  '" + rolecollectioname + \
                            "' --of-role-template '" + roleTemplate + "' --of-app '" + roleAppId + "' --subaccount '" + subaccountid + "'"
                        p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
                        resultErr = p.stderr.decode()
                        resultSuc = p.stdout.decode()
                        if resultErr and "OK" in resultErr:
                            # An OK code is returned via STDERR???
                            log.info(resultErr.strip())
                        else:
                            log.warn(resultErr)  
                        if resultSuc:
                            log.info(resultSuc)

            for userEmail in members:
                message = "assign user >" + userEmail + "< the role collection >" + rolecollectioname + "<"
                command = "btp --format json assign security/role-collection '" + rolecollectioname + "' --to-user '" + userEmail + \
                    "' --create-user-if-missing --subaccount '" + subaccountid + "'"
                runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)


def assignUsersToRoleCollectionsForServices(btpUsecase):
    rolecollections = getRoleCollectionsOfServices(btpUsecase)
    log.header("Assign users to role collections specific to a service")
    if rolecollections:
        for rolecollection in rolecollections:
            assignUsergroupsToRoleCollection(btpUsecase, rolecollection)


def assignUsersToEnvironments(btpUsecase):
    environments = btpUsecase.definedEnvironments

    if environments:
        for environment in environments:
            if environment.name == "cloudfoundry":
                org = btpUsecase.org
                cfspacename = btpUsecase.cfspacename

                rolecollectionsCloudFoundryOrg = getRoleCollectionsOfTypeAndLevel(btpUsecase, "cloudfoundry", "org")
                if rolecollectionsCloudFoundryOrg:
                    log.header("Set members for Cloudfoundry org")
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

                rolecollectionsCloudFoundrySpace = getRoleCollectionsOfTypeAndLevel(btpUsecase, "cloudfoundry", "space")
                if rolecollectionsCloudFoundrySpace:
                    log.header("Set members for Cloudfoundry space")
                    for rolecollection in rolecollectionsCloudFoundrySpace:
                        members = getMembersForRolecollection(btpUsecase, rolecollection)
                        spaceRole = rolecollection.get("name")
                        log.info("assign users to space role >" + spaceRole + "<")
                        for admin in members:
                            message = " - user >" + admin + "<"
                            command = "cf set-space-role '" + admin + "' '" + org + "' '" + cfspacename + "' '" + spaceRole + "'"
                            p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
                            result = p.stdout.decode()
                            if "message: The user could not be found" in result:
                                log.error("the user >" + admin + "< was not found and could not be assigned the role >" + spaceRole + "<")
