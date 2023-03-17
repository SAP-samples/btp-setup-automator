from libs.python.helperCommandExecution import (
    runCommandAndGetJsonResult,
    runShellCommandFlex,
    runShellCommand,
)
from libs.python.helperCommandExecution import login_cf
from libs.python.helperJson import getJsonFromFile
import logging
import sys
import os

log = logging.getLogger(__name__)


def getMembersForRolecollection(btpUsecase, rolecollection):
    # the one executing the use case is only added to the role collections defined in the use case if explicitly added
    users = []

    if rolecollection:
        for usergroup in rolecollection.get("assignedUserGroupsFromParameterFile"):
            members = getMembersOfUserGroup(btpUsecase, usergroup)
            if members:
                for member in members:
                    users.append(member)
            else:
                log.warning(
                    "Didn't find any members for user group >"
                    + usergroup
                    + '<. Check the section "usergroups" in your parameters file >'
                    + btpUsecase.parameterfile
                    + "<"
                )
        users = list(dict.fromkeys(users))
    return users


def getRoleCollectionsOfServices(btpUsecase):
    # Use case file can be remote, so we need to provide authentication information
    usecase = getJsonFromFile(
        btpUsecase.usecasefile,
        btpUsecase.externalConfigAuthMethod,
        btpUsecase.externalConfigUserName,
        btpUsecase.externalConfigPassword,
        btpUsecase.externalConfigToken,
    )
    items = []
    if usecase.get("services") is not None:
        for service in usecase.get("services"):
            if service.get("requiredrolecollections") is not None:
                for rolecollection in service.get("requiredrolecollections"):
                    items.append(rolecollection)

    return items


def getMembersOfUserGroup(btpUsecase, usergroup):
    # the one executing the use case is only added to the role collections defined in the use case if explicitly added
    members = []
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
                log.error(
                    "you didn't define a usergroup >"
                    + usergroup
                    + "< in your parameters file >"
                    + btpUsecase.parameterfile
                    + "<. Therefore no members where found."
                )
        else:
            log.warning(
                "didn't find user group >"
                + usergroup
                + "< as no usergroups defined in your parameters file >"
                + btpUsecase.parameterfile
                + "<"
            )

    return members


def assignUsergroupsToRoleCollection(btpUsecase, rolecollection):
    accountMetadata = btpUsecase.accountMetadata
    subaccountid = accountMetadata["subaccountid"]

    roleCollectionIsString = isinstance(rolecollection, str)
    roleCollectionIsList = isinstance(rolecollection, dict)

    if roleCollectionIsList:
        assignedUserGroupsFromParameterFile = rolecollection.get(
            "assignedUserGroupsFromParameterFile"
        )

        idp = determineIdpForRoleCollection(btpUsecase, rolecollection)

        for usergroup in assignedUserGroupsFromParameterFile:
            members = getMembersOfUserGroup(btpUsecase, usergroup)
            if members:
                rolecollectioname = rolecollection.get("name")
                log.info("assign users the role collection >" + rolecollectioname + "<")
                for userEmail in members:
                    message = " - user >" + userEmail + "<"
                    command = (
                        "btp --format json assign security/role-collection '"
                        + rolecollectioname
                        + "' --to-user '"
                        + userEmail
                        + "' --create-user-if-missing --subaccount '"
                        + subaccountid
                        + "'"
                    )
                    if idp is not None:
                        command += " --of-idp '" + idp + "'"

                        # Additional mapping for custom IdP only relevant if custom IdP is used
                        (
                            groupForIdp,
                            attributeForIdp,
                            attributeValueForIdp,
                        ) = getCustomIdpMapping(rolecollection)

                        if isMappingForIdpValid(
                            groupForIdp, attributeForIdp, attributeValueForIdp
                        ):

                            if groupForIdp is not None:
                                command += " --to-group '" + groupForIdp + "'"

                            if attributeForIdp is not None:
                                command += " --to-attribute '" + attributeForIdp + "'"
                                command += (
                                    " --attribute-value '" + attributeValueForIdp + "'"
                                )
                        else:
                            log.error(
                                "Custom IdP configuration is not valid. Please check."
                            )
                            sys.exit(os.EX_DATAERR)

                    thisResult = runCommandAndGetJsonResult(
                        btpUsecase, command, "INFO", message
                    )
                    thisResult = thisResult
    if roleCollectionIsString:
        log.warning(
            "YOU ARE USING A LEGACY CONFIGURATION FOR ASSIGING USERS TO ROLE COLLECTIONS!"
        )
        log.warning(
            "Please change your parameters file and your usecase file accordingly."
        )
        log.warning(
            "Checkout the default parameters file and the other released use cases to understand how to do it."
        )


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
    rolecollectionsGlobalAccount = getRoleCollectionsOfTypeAndLevel(
        btpUsecase, "account", "global account"
    )
    if rolecollectionsGlobalAccount:
        for rolecollection in rolecollectionsGlobalAccount:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            role = rolecollection.get("name")
            log.info("assign users to global account role >" + role + "<")

            idp = determineIdpForRoleCollection(btpUsecase, rolecollection)
            for userEmail in members:
                message = " - assign user >" + userEmail + "<"
                command = (
                    "btp --format json assign security/role-collection '"
                    + role
                    + "' --to-user '"
                    + userEmail
                    + "' --create-user-if-missing -ga"
                )
                if idp is not None:
                    command += " --of-idp '" + idp + "'"

                    # Additional mapping for custom IdP only relevant if custom IdP is used
                    (
                        groupForIdp,
                        attributeForIdp,
                        attributeValueForIdp,
                    ) = getCustomIdpMapping(rolecollection)

                    if isMappingForIdpValid(
                        groupForIdp, attributeForIdp, attributeValueForIdp
                    ):

                        if groupForIdp is not None:
                            command += " --to-group '" + groupForIdp + "'"

                        if attributeForIdp is not None:
                            command += " --to-attribute '" + attributeForIdp + "'"
                            command += (
                                " --attribute-value '" + attributeValueForIdp + "'"
                            )
                    else:
                        log.error(
                            "Custom IdP configuration is not valid. Please check."
                        )
                        sys.exit(os.EX_DATAERR)

                runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)

    log.header("Set administrators for sub account")
    rolecollectionsSubAccount = getRoleCollectionsOfTypeAndLevel(
        btpUsecase, "account", "sub account"
    )
    if rolecollectionsSubAccount:
        for rolecollection in rolecollectionsSubAccount:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            role = rolecollection.get("name")
            log.info("assign users to sub account role >" + role + "<")

            idp = determineIdpForRoleCollection(btpUsecase, rolecollection)
            for userEmail in members:
                message = " - assign user >" + userEmail + "<"
                command = (
                    "btp --format json assign security/role-collection '"
                    + role
                    + "' --to-user '"
                    + userEmail
                    + "' --create-user-if-missing --subaccount '"
                    + subaccountid
                    + "'"
                )
                if idp is not None:
                    command += " --of-idp '" + idp + "'"

                    # Additional mapping for custom IdP only relevant if custom IdP is used
                    (
                        groupForIdp,
                        attributeForIdp,
                        attributeValueForIdp,
                    ) = getCustomIdpMapping(rolecollection)

                    if isMappingForIdpValid(
                        groupForIdp, attributeForIdp, attributeValueForIdp
                    ):

                        if groupForIdp is not None:
                            command += " --to-group '" + groupForIdp + "'"

                        if attributeForIdp is not None:
                            command += " --to-attribute '" + attributeForIdp + "'"
                            command += (
                                " --attribute-value '" + attributeValueForIdp + "'"
                            )
                    else:
                        log.error(
                            "Custom IdP configuration is not valid. Please check."
                        )
                        sys.exit(os.EX_DATAERR)

                runCommandAndGetJsonResult(btpUsecase, command, "INFO", message)


def assignUsersToCustomRoleCollections(btpUsecase):
    subaccountid = btpUsecase.subaccountid

    rolecollectionsCustom = getRoleCollectionsOfTypeAndLevel(btpUsecase, "custom", None)
    if rolecollectionsCustom:
        for rolecollection in rolecollectionsCustom:
            members = getMembersForRolecollection(btpUsecase, rolecollection)
            rolecollectioname = rolecollection.get("name")
            log.info(
                "assign users to custom role collection >" + rolecollectioname + "<"
            )

            message = (
                "Check if role collection >" + rolecollectioname + "< already exists"
            )
            command = "btp get security/role-collection '" + rolecollectioname + "'"
            p = runShellCommandFlex(btpUsecase, command, "INFO", message, False, False)
            result = p.stdout.decode()
            if not result:
                errormessage = p.stderr.decode()
                if "error: No entity found with values" in errormessage:
                    message = "Assign role collection >" + rolecollectioname
                    command = (
                        "btp create security/role-collection '"
                        + rolecollectioname
                        + "' --description  '"
                        + rolecollectioname
                        + "' --subaccount '"
                        + subaccountid
                        + "'"
                    )
                    runShellCommand(btpUsecase, command, "INFO", message)

                    if rolecollection["assignedRoles"]:
                        # Get role data from btp for subaccount
                        command = (
                            "btp --format json list security/role --subaccount '"
                            + subaccountid
                            + "'"
                        )
                        roleSecDataJson = runCommandAndGetJsonResult(
                            btpUsecase, command, "INFO", "Get roles for subaccount"
                        )

                    for role in rolecollection["assignedRoles"]:
                        message = (
                            "Assign role "
                            + role
                            + " to role collection "
                            + rolecollectioname
                        )

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

                        command = (
                            "btp add security/role '"
                            + role
                            + "' --to-role-collection  '"
                            + rolecollectioname
                            + "' --of-role-template '"
                            + roleTemplate
                            + "' --of-app '"
                            + roleAppId
                            + "' --subaccount '"
                            + subaccountid
                            + "'"
                        )
                        p = runShellCommandFlex(
                            btpUsecase, command, "INFO", message, False, False
                        )
                        resultErr = p.stderr.decode()
                        resultSuc = p.stdout.decode()
                        if resultErr and "OK" in resultErr:
                            # An OK code is returned via STDERR???
                            log.info(resultErr.strip())
                        else:
                            log.warn(resultErr)
                        if resultSuc:
                            log.info(resultSuc)

            idp = determineIdpForRoleCollection(btpUsecase, rolecollection)

            for userEmail in members:
                message = (
                    "assign user >"
                    + userEmail
                    + "< the role collection >"
                    + rolecollectioname
                    + "<"
                )
                command = (
                    "btp --format json assign security/role-collection '"
                    + rolecollectioname
                    + "' --to-user '"
                    + userEmail
                    + "' --create-user-if-missing --subaccount '"
                    + subaccountid
                    + "'"
                )
                if idp is not None:
                    command += " --of-idp '" + idp + "'"

                    # Additional mapping for custom IdP only relevant if custom IdP is used
                    (
                        groupForIdp,
                        attributeForIdp,
                        attributeValueForIdp,
                    ) = getCustomIdpMapping(rolecollection)

                    if isMappingForIdpValid(
                        groupForIdp, attributeForIdp, attributeValueForIdp
                    ):

                        if groupForIdp is not None:
                            command += " --to-group '" + groupForIdp + "'"

                        if attributeForIdp is not None:
                            command += " --to-attribute '" + attributeForIdp + "'"
                            command += (
                                " --attribute-value '" + attributeValueForIdp + "'"
                            )
                    else:
                        log.error(
                            "Custom IdP configuration is not valid. Please check."
                        )
                        sys.exit(os.EX_DATAERR)

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
                # Make sure that you are logged in to the CF API
                if btpUsecase.skipcfspacecreation is True:
                    login_cf(btpUsecase)

                org = btpUsecase.org
                cfspacename = btpUsecase.cfspacename

                rolecollectionsCloudFoundryOrg = getRoleCollectionsOfTypeAndLevel(
                    btpUsecase, "cloudfoundry", "org"
                )
                if rolecollectionsCloudFoundryOrg:
                    log.header("Set members for Cloudfoundry org")
                    for rolecollection in rolecollectionsCloudFoundryOrg:
                        members = getMembersForRolecollection(
                            btpUsecase, rolecollection
                        )
                        idp = determineIdpForRoleCollection(btpUsecase, rolecollection)
                        orgRole = rolecollection.get("name")
                        log.info("assign users to org role >" + orgRole + "<")
                        for user in members:
                            message = " - user >" + user + "<"
                            command = (
                                "cf set-org-role '"
                                + user
                                + "' '"
                                + org
                                + "' '"
                                + orgRole
                                + "'"
                            )
                            if idp is not None:
                                command += " --origin '" + idp + "'"

                            p = runShellCommandFlex(
                                btpUsecase, command, "INFO", message, False, False
                            )
                            result = "".join(p.stdout.decode().splitlines())
                            if "FAILED" in result:
                                error = "".join(p.stderr.decode().splitlines())
                                log.error(result)
                                log.error(error)

                rolecollectionsCloudFoundrySpace = getRoleCollectionsOfTypeAndLevel(
                    btpUsecase, "cloudfoundry", "space"
                )
                if rolecollectionsCloudFoundrySpace:
                    log.header("Set members for Cloudfoundry space")
                    for rolecollection in rolecollectionsCloudFoundrySpace:
                        members = getMembersForRolecollection(
                            btpUsecase, rolecollection
                        )
                        idp = determineIdpForRoleCollection(btpUsecase, rolecollection)
                        spaceRole = rolecollection.get("name")
                        log.info("assign users to space role >" + spaceRole + "<")
                        for user in members:
                            message = " - user >" + user + "<"
                            command = (
                                "cf set-space-role '"
                                + user
                                + "' '"
                                + org
                                + "' '"
                                + cfspacename
                                + "' '"
                                + spaceRole
                                + "'"
                            )
                            if idp is not None:
                                command += " --origin '" + idp + "'"
                            p = runShellCommandFlex(
                                btpUsecase, command, "INFO", message, False, False
                            )
                            result = "".join(p.stdout.decode().splitlines())
                            if "FAILED" in result:
                                error = "".join(p.stderr.decode().splitlines())
                                log.error(result)
                                log.error(error)


def determineIdpForRoleCollection(btpUsecase, rolecollection):
    # If no IdP is configured we use the default one and do not provide an IdP
    idp = None

    if btpUsecase.defaultIdp:
        # A explicit default IdP is configured
        idp = btpUsecase.defaultIdp
    if rolecollection.get("idp"):
        # A role collection specific IdP is configured - overrules the default IdP
        idp = rolecollection.get("idp")

    return idp


def getCustomIdpMapping(rolecollection):
    groupForIdp = None
    attributeForIdp = None
    attributeValueForIdp = None

    if rolecollection.get("group"):
        groupForIdp = rolecollection.get("group")

    if rolecollection.get("attribute"):
        attributeForIdp = rolecollection.get("attribute")

    if rolecollection.get("attributeValue"):
        attributeValueForIdp = rolecollection.get("attributeValue")

    return groupForIdp, attributeForIdp, attributeValueForIdp


def isMappingForIdpValid(groupForIdp, attributeForIdp, attributeValueForIdp):
    if groupForIdp is not None and attributeForIdp is not None:
        log.error(
            "A group and an attribute is configured for the IdP mapping. Only one is allowed."
        )
        return False
    if (attributeForIdp is None and attributeValueForIdp is not None) or (
        attributeForIdp is not None and attributeValueForIdp is None
    ):
        log.error(
            "Attribute and attributeValue are both required for the IdP mapping. One is missing."
        )
        return False
    return True
