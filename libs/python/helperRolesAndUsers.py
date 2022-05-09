from libs.python.helperCommandExecution import runShellCommand, runShellCommandFlex, runCommandAndGetJsonResult
from libs.python.helperGeneric import save_collected_metadata
from libs.python.helperJson import addKeyValuePair, dictToString, getJsonFromFile
import re
import os
import sys
import logging

log = logging.getLogger(__name__)


def getUserGroups(btpUsecase):
    return btpUsecase.usergroups


def getMembersOfUserGroup(btpUsecase, usergroup):

    for thisUserGroup in btpUsecase.usergroups:
        if thisUserGroup.get("name") == usergroup:
            members = thisUserGroup.get("members")
    return members


def assignRoleToRoleCollection(btpUsecase, role, rolecollectioname):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    message = "Assign role " + role["name"] + " to role collection " + rolecollectioname
    command = "btp add security/role '" + role["name"] + "' --to-role-collection  '" + rolecollectioname + \
        "' --of-role-template '" + role["roletemplate"] + "' --of-app '" + role["app"] + "' --subaccount '" + subaccountid + "'"
    runShellCommand(btpUsecase, command, "INFO", message)


def assignUsergroupsToRoleCollection(btpUsecase, rolecollection):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    assignedUserGroupsFromParameterFile = rolecollection.get("assignedUserGroupsFromParameterFile")

    for usergroup in assignedUserGroupsFromParameterFile:
        members = getMembersOfUserGroup(btpUsecase, usergroup)
        for userEmail in members:
            rolecollectioname = rolecollection.get("name")
            message = "assign user >" + userEmail + "< the role collection >" + rolecollectioname + "<"
            command = "btp --format json assign security/role-collection '" + rolecollectioname + "' --to-user '" + userEmail + \
                "' --create-user-if-missing --subaccount '" + subaccountid + "'"
            thisResult = runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)
            thisResult = thisResult


def createRoleCollection(btpUsecase, rolecollectioname):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    message = "Create role collection >" + rolecollectioname
    command = "btp create security/role-collection '" + rolecollectioname + "' --description  '" + rolecollectioname + "' --subaccount '" + subaccountid + "'"
    runShellCommand(btpUsecase, command, "INFO", message)


def createRoleCollectionIfNotExisting(btpUsecase, rolecollection):
    rolecollectioname = rolecollection["name"]
    # Check the role collection was not created before
    message = "Check if this role collection does not exist >" + rolecollectioname
    command = "btp get security/role-collection '" + rolecollectioname + "'"
    p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
    result = p.stdout.decode()

    # If the role collection is not existing so far, create it
    if not result:
        result = p.stderr.decode()
        if "error: No entity found with values" in result:
            createRoleCollection(btpUsecase, rolecollectioname)
            for role in rolecollection["roles"]:
                assignRoleToRoleCollection(btpUsecase, role, rolecollectioname)


def getRoleCollectionsOfServices(btpUsecase):
    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if usecase.get("services") is not None:
        for service in usecase.get("services"):
            if service.get("requiredrolecollections") is not None:
                for rolecollection in service.get("requiredrolecollections"):
                    items.append(rolecollection)

    return items


def getSelfDefinedRoleCollections(btpUsecase):
    usecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)
    items = []
    if "requiredrolecollections" in usecase:
        for rolecollection in usecase["requiredrolecollections"]:
            items.append(rolecollection)
    else:
        log.info("no role collections defined in your use case configuration file")

    return items


def getAdminsForUseCase(btpUsecase):
    licenseType = None
    result = []
    myUser = btpUsecase.myemail

    licenseType = btpUsecase.accountMetadata["licenseType"]

    if licenseType != "TRIAL":
        for admin in btpUsecase.admins:
            email = admin
            result.append(email)

    result.append(myUser)
    # remove duplicates in admins list
    result = list(dict.fromkeys(result))

    return result


def build_admins_list(btpUsecase):
    admins = getAdminsForUseCase(btpUsecase)
    # Remove duplicates
    admins = list(dict.fromkeys(admins))
    result = "["

    for admin in admins:
        if admin == admins[-1]:
            result += '"' + admin + '"]'
        else:
            result += '"' + admin + '" , '

    return result


def getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase):
    allEmails = None
    adminsList = btpUsecase.admins

    # Create a copy of the usecase, as we might have to remove pieces prior the analysis
    thisUsecase = getJsonFromFile(btpUsecase, btpUsecase.usecasefile)

    # Remove the use case author from the usecase to be analyzed
    if "aboutThisUseCase" in thisUsecase and "author" in thisUsecase["aboutThisUseCase"]:
        del thisUsecase["aboutThisUseCase"]["author"]

    # Convert the usecase dict to a string to detect any other email-adresses added in other parameters of the file
    usecaseString = dictToString(thisUsecase)
    allEmails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', usecaseString)

    # Before checking all other email addresses, remove from the result all the email addresses that already have been covered in the admins section
    for admin in adminsList:
        if admin in allEmails:
            allEmails.remove(admin)

    return allEmails


def checkEmailsinUsecaseConfig(btpUsecase):
    allowedUsers = getListOfUsersOnAccount(btpUsecase)
    foundError = False

    adminsList = getAdminsForUseCase(btpUsecase)

    for admin in adminsList:
        if admin in allowedUsers:
            log.success("user >" + admin + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
        else:
            log.warning("user >" + admin + "< (defined in admins section of file >" + btpUsecase.usecasefile + "<) has no access to this global account")

    emailAddresses = getListOfAdditionalEmailAdressesInUsecaseFile(btpUsecase)

    # Now we can run the email check for the other email addresses
    for emailAddress in emailAddresses:
        if emailAddress in allowedUsers:
            log.success("user >" + emailAddress + "< will be able to access use case in global account >" + btpUsecase.globalaccount + "<")
        else:
            log.warning("email address >" + emailAddress + "< was found in the usecase definition, but that user has no access to this global account. Please check!")
    if foundError is True:
        log.error("Can't move on with the use case, before the errors above are not fixed")
        sys.exit(os.EX_DATAERR)

    return None


def getListOfUsersOnAccount(btpUsecase):
    result = None

    command = "btp --format json list security/user"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    return result


def assignUsersToSubaccount(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata

    subaccountid = accountMetadata["subaccountid"]
    admins = getAdminsForUseCase(btpUsecase)

    log.header("Set global account and sub account administrators")
    for userEmail in admins:
        role = "Subaccount Administrator"
        message = "assign user >" + userEmail + "< the role >" + role + "<"
        command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
        runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

        role = "Subaccount Service Administrator"
        message = "assign user >" + userEmail + "< the role >" + role + "<"
        command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + \
            userEmail + "' --create-user-if-missing --subaccount '" + subaccountid + "'"
        runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

        # Do not add user as global admin for Trial accounts
        if btpUsecase.accountMetadata["licenseType"] != "TRIAL":
            role = "Global Account Administrator"
            message = "assign user >" + userEmail + "< the role >" + role + "<"
            # Add user to GA with suffix -ga
            command = "btp --format json assign security/role-collection '" + role + "' --to-user '" + userEmail + "' --create-user-if-missing -ga"
            runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)


def set_all_cf_space_roles(btpUsecase):
    environments = btpUsecase.definedEnvironments

    for environment in environments:
        if environment.name == "cloudfoundry":
            admins = getAdminsForUseCase(btpUsecase)

            accountMetadata = btpUsecase.accountMetadata
            log.header("Set all CF space roles")

            org = accountMetadata["org"]
            cfspacename = btpUsecase.cfspacename
            accountMetadata = addKeyValuePair(accountMetadata, "cfspacename", cfspacename)

            spaceRoles = ["SpaceManager", "SpaceDeveloper", "SpaceAuditor"]

            for spaceRole in spaceRoles:
                for admin in admins:
                    message = "Assign space role >" + spaceRole + "< to user >" + admin + "<"
                    command = "cf set-space-role '" + admin + "' '" + org + "' '" + cfspacename + "' '" + spaceRole + "'"
                    p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + spaceRole + "<")

            save_collected_metadata(btpUsecase)


def set_all_cf_org_roles(btpUsecase):
    environments = btpUsecase.definedEnvironments

    for environment in environments:
        if environment.name == "cloudfoundry":
            admins = getAdminsForUseCase(btpUsecase)

            accountMetadata = btpUsecase.accountMetadata
            log.header("Set all CF org roles")

            org = accountMetadata["org"]

            orgRoles = ["OrgManager", "OrgAuditor"]

            for orgRole in orgRoles:
                for admin in admins:
                    message = "Assign org role >" + orgRole + "< to user >" + admin + "<"
                    command = "cf set-org-role '" + admin + "' '" + org + "' '" + orgRole + "'"
                    p = runShellCommandFlex(
                        btpUsecase, command, "INFO", message, False, False)
                    result = p.stdout.decode()
                    if "message: The user could not be found" in result:
                        log.error("the user >" + admin + "< was not found and could not be assigned the role >" + orgRole + "<")

            save_collected_metadata(btpUsecase)
