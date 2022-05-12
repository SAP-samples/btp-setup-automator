from libs.python.helperCommandExecution import runCommandAndGetJsonResult, runShellCommandFlex
# from libs.python.helperGeneric import save_collected_metadata
from libs.python.helperJson import getJsonFromFile
# import re
# import os
# import sys
import logging

log = logging.getLogger(__name__)


# def getMembersOfUsergroupType(btpUsecase, type):
#     usergroups = btpUsecase.usergroups
#     userList = []

#     for group in usergroups:
#         if group.get("type") == type:
#             members = group.get("members")
#             for member in members:
#                 userList.append(member)
#     userList = list(dict.fromkeys(userList))

#     return userList


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


# def getUserGroups(btpUsecase):
#     return btpUsecase.usergroups

# def assignRoleToRoleCollection(btpUsecase, role, rolecollectioname):
#     accountMetadata = btpUsecase.accountMetadata
#     subaccountid = accountMetadata["subaccountid"]

#     message = "Assign role " + role["name"] + " to role collection " + rolecollectioname
#     command = "btp add security/role '" + role["name"] + "' --to-role-collection  '" + rolecollectioname + \
#         "' --of-role-template '" + role["roletemplate"] + "' --of-app '" + role["app"] + "' --subaccount '" + subaccountid + "'"
#     runShellCommand(btpUsecase, command, "INFO", message)


# def createRoleCollection(btpUsecase, rolecollectioname):
#     accountMetadata = btpUsecase.accountMetadata
#     subaccountid = accountMetadata["subaccountid"]

#     message = "Create role collection >" + rolecollectioname
#     command = "btp create security/role-collection '" + rolecollectioname + "' --description  '" + rolecollectioname + "' --subaccount '" + subaccountid + "'"
#     runShellCommand(btpUsecase, command, "INFO", message)


# def createRoleCollectionIfNotExisting(btpUsecase, rolecollection):
#     rolecollectioname = rolecollection["name"]
#     # Check the role collection was not created before
#     message = "Check if this role collection does not exist >" + rolecollectioname
#     command = "btp get security/role-collection '" + rolecollectioname + "'"
#     p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
#     result = p.stdout.decode()

#     # If the role collection is not existing so far, create it
#     if not result:
#         result = p.stderr.decode()
#         if "error: No entity found with values" in result:
#             createRoleCollection(btpUsecase, rolecollectioname)

#     for role in rolecollection.get("assignedUserGroupsFromParameterFile"):
#         assignRoleToRoleCollection(btpUsecase, role, rolecollectioname)


# def getAdminsForUseCase(btpUsecase):
#     licenseType = None
#     result = []
#     myUser = btpUsecase.myemail

#     licenseType = btpUsecase.accountMetadata["licenseType"]

#     if licenseType != "TRIAL":
#         for admin in btpUsecase.admins:
#             email = admin
#             result.append(email)

#     result.append(myUser)
#     # remove duplicates in admins list
#     result = list(dict.fromkeys(result))

#     return result


# def build_admins_list(btpUsecase):
#     admins = getAdminsForUseCase(btpUsecase)
#     # Remove duplicates
#     admins = list(dict.fromkeys(admins))
#     result = "["

#     for admin in admins:
#         if admin == admins[-1]:
#             result += '"' + admin + '"]'
#         else:
#             result += '"' + admin + '" , '

#     return result


# def getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase):
#     allEmails = None
#     adminsList = btpUsecase.admins

#     # Create a copy of the usecase, as we might have to remove pieces prior the analysis
#     thisUsecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)

#     # Remove the use case author from the usecase to be analyzed
#     if "aboutThisUseCase" in thisUsecase and "author" in thisUsecase["aboutThisUseCase"]:
#         del thisUsecase["aboutThisUseCase"]["author"]

#     # Convert the usecase dict to a string to detect any other email-adresses added in other parameters of the file
#     usecaseString = dictToString(thisUsecase)
#     allEmails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', usecaseString)

#     # Before checking all other email addresses, remove from the result all the email addresses that already have been covered in the admins section
#     for admin in adminsList:
#         if admin in allEmails:
#             allEmails.remove(admin)

#     return allEmails


# def checkEmailsinUsecaseConfig(btpUsecase):
#     allowedUsers = getListOfUsersOnAccount(btpUsecase)
#     foundError = False

#     adminsList = getAdminsForUseCase(btpUsecase)

#     for admin in adminsList:
#         if admin in allowedUsers:
#             log.success("user >" + admin + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
#         else:
#             log.warning("user >" + admin + "< (defined in admins section of file >" + btpUsecase.usecasefile + "<) has no access to this global account")

#     emailAddresses = getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase)

#     # Now we can run the email check for the other email addresses
#     for emailAddress in emailAddresses:
#         if emailAddress in allowedUsers:
#             log.success("user >" + emailAddress + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
#         else:
#             log.warning("email address >" + emailAddress + "< was found in the usecase definition, but that user has no access to this global account. Please check!")
#     if foundError is True:
#         log.error("Can't move on with the use case, before the errors above are not fixed")
#         sys.exit(os.EX_DATAERR)

#     return None


# def getListOfUsersOnAccount(btpUsecase):
#     result = None

#     command = "btp --format json list security/user"
#     result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

#     return result


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


# # def assignUsersToSubaccount(btpUsecase):
# #     accountMetadata = btpUsecase.accountMetadata

# #     subaccountid = accountMetadata["subaccountid"]

# #     for role in btpUsecase.definedRoleCollections:
# #         usergroups = role.get("assignedUserGroupsFromParameterFile")
# #         for userEmail in

# #     admins = getAdminsForUseCase(btpUsecase)

# #     log.header("Set global account and sub account administrators")
# #     for userEmail in admins:
# #         role = "Subaccount Administrator"
# #         message = "assign user >" + userEmail + "< the role >" + role + "<"
# #         command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
# #         runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

# #         role = "Subaccount Service Administrator"
# #         message = "assign user >" + userEmail + "< the role >" + role + "<"
# #         command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
# #         runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

# #         # Do not add user as global admin for Trial accounts
# #         if btpUsecase.accountMetadata["licenseType"] != "TRIAL":
# #             role = "Global Account Administrator"
# #             message = "assign user >" + userEmail + "< the role >" + role + "<"
# #             # Add user to GA with suffix -ga
# #             command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing -ga"
# #             runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

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


# def set_all_cf_space_roles(btpUsecase):
#     environments = btpUsecase.definedEnvironments

#     for environment in environments:
#         if environment.name == "cloudfoundry":
#             members = []
#             subaccountAdmins = getMembersOfUsergroupType(btpUsecase, "subaccount")
#             for member in subaccountAdmins:
#                 members.append(member)
#             subaccountAdmins = getMembersOfUsergroupType(btpUsecase, "subaccount")

#             members = list(dict.fromkeys(members))

#             accountMetadata = btpUsecase.accountMetadata
#             log.header("Set all CF space roles")

#             org = accountMetadata["org"]
#             cfspacename = btpUsecase.cfspacename
#             accountMetadata = addKeyValuePair(accountMetadata, "cfspacename", cfspacename)

#             spaceRoles = ["SpaceManager", "SpaceDeveloper", "SpaceAuditor"]

#             for spaceRole in spaceRoles:
#                 for admin in members:
#                     message = "Assign space role >" + spaceRole + "< to user >" + admin + "<"
#                     command = "cf set-space-role '" + admin + "' '" + org + "' '" + cfspacename + "' '" + spaceRole + "'"
#                     p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
#                     result = p.stdout.decode()
#                     if "message: The user could not be found" in result:
#                         log.error("the user >" + admin + "< was not found and could not be assigned the role >" + spaceRole + "<")

#             save_collected_metadata(btpUsecase)


# def set_all_cf_org_roles(btpUsecase):
#     environments = btpUsecase.definedEnvironments

#     for environment in environments:
#         if environment.name == "cloudfoundry":
#             admins = getAdminsForUseCase(btpUsecase)

#             accountMetadata = btpUsecase.accountMetadata
#             log.header("Set all CF org roles")

#             org = accountMetadata["org"]

#             orgRoles = ["OrgManager", "OrgAuditor"]

#             for orgRole in orgRoles:
#                 for admin in admins:
#                     message = "Assign org role >" + orgRole + "< to user >" + admin + "<"
#                     command = "cf set-org-role '" + admin + "' '" + org + "' '" + orgRole + "'"
#                     p = runShellCommandFlex(
#                         btpUsecase, command, "INFO", message, False, False)
#                     result = p.stdout.decode()
#                     if "message: The user could not be found" in result:
#                         log.error("the user >" + admin + "< was not found and could not be assigned the role >" + orgRole + "<")

#             save_collected_metadata(btpUsecase)
