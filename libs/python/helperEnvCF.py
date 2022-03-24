from libs.python.helperCommandExecution import runShellCommand, runCommandAndGetJsonResult, login_cf, runShellCommandFlex
from libs.python.helperGeneric import getServiceByServiceName, createInstanceName, getTimingsForStatusRequest
from libs.python.helperJson import convertStringToJson, convertCloudFoundryCommandOutputToJson, dictToString
from libs.python.helperLog import logtype
import time
import os
import sys


def getKeyFromCFOutput(cfoutput, key):
    result = None

    lines = cfoutput.splitlines()
    for line in lines:
        thisLineSplit = line.split(":")
        if len(thisLineSplit) == 2 and thisLineSplit[0] == key:
            result = thisLineSplit[1].strip()
    return result


def checkIfCFEnvironmentAlreadyExists(btpUsecase):
    accountMetadata = btpUsecase.accountMetadata

    command = "btp --format json list account/environment-instance --subaccount " + \
        accountMetadata["subaccountid"]
    result = runCommandAndGetJsonResult(
        btpUsecase, command, logtype.INFO, None)

    if "orgid" in accountMetadata:
        orgid = accountMetadata["orgid"]
        nameOfEnvInstance = accountMetadata["subdomain"] + "_cloudfoundry"
        org = None

        for instance in result["environmentInstances"]:
            if instance["name"] == nameOfEnvInstance:
                labels = convertStringToJson(instance["labels"])
                org = labels["Org Name:"]
                return instance["platformId"], org
        # If the for loop didn't return any value, the orgid wasn't found
        return orgid, org
    else:
        return None, None


def checkIfCFSpaceAlreadyExists(btpUsecase):
    cfspacename = btpUsecase.cfspacename

    command = "cf spaces"
    p = runShellCommand(btpUsecase, command, logtype.INFO, None)
    result = p.stdout.decode()
    lines = result.splitlines()

    for line in lines:
        if cfspacename == line:
            return True
    return False


def checkIfAllServiceInstancesCreated(btpUsecase):
    log = btpUsecase.log

    command = "cf services"
    p = runShellCommand(btpUsecase, command, logtype.INFO, None)
    result = p.stdout.decode()
    jsonResults = convertCloudFoundryCommandOutputToJson(result)

    allServicesCreated = True
    for thisJson in jsonResults:
        name = thisJson["service"]
        plan = thisJson["plan"]
        instancename = thisJson["name"]
        status = thisJson["last operation"]
        servicebroker = thisJson["broker"]
        for service in btpUsecase.definedServices:
            if service["name"] == name and service["plan"] == plan and service["instancename"] == instancename and service["successInfoShown"] is False:
                if status != "create succeeded":
                    allServicesCreated = False
                    service["status"] = "NOT READY"
                    service["successInfoShown"] = False
                else:
                    log.write(logtype.SUCCESS, "Service instance for service >" + service["name"] + "< (plan " + service["plan"] + ") is now available")
                    service["servicebroker"] = servicebroker
                    service["successInfoShown"] = True
                    service["status"] = "create succeeded"
    return allServicesCreated


def try_until_cf_space_done(btpUsecase, command, message, spacename, search_every_x_seconds, timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        p = runShellCommand(btpUsecase, command, logtype.INFO, message)
        result = p.stdout.decode()
        lines = result.splitlines()

        for line in lines:
            if line == "name":
                continue
            if spacename == line:
                return "DONE"

        time.sleep(search_every_x_seconds)
        current_time += search_every_x_seconds
    return result


def create_cf_service(btpUsecase, service):
    instancename = service["instancename"]

    command = "cf create-service \"" + \
        service["name"] + "\" \"" + service["plan"] + \
        "\"  \"" + instancename + "\""

    if "parameters" in service:
        thisParameter = dictToString(service["parameters"])
        command += " -c '" + thisParameter + "'"
    message = "Create instance >" + instancename + "< for service >" + \
        service["name"] + "< and plan >" + service["plan"] + "<"
    runShellCommand(btpUsecase, command, logtype.INFO, message)
    return service


def create_cf_cup_service(btpUsecase, service):
    log = btpUsecase.log

    servicename = service["name"]
    command = "cf cups \"" + servicename + "\" "

    if "parameters" in service:
        thisParameter = str(service["parameters"])
        command += thisParameter
        message = "Create CF cups instance for service >" + servicename + "<"
        runShellCommand(btpUsecase, command, logtype.INFO, message)
        log.write(logtype.INFO, "created CF cup service >" + servicename + "<")
    else:
        message = "missing parameter for the CF cups service >" + servicename + "<. Won't create the CF cup service."
        log.write(logtype.WARNING, message)

    return service


def initiateCreationOfServiceInstances(btpUsecase):
    log = btpUsecase.log

    createServiceInstances = btpUsecase.definedServices is not None and len(btpUsecase.definedServices) > 0

    if createServiceInstances is True:
        login_cf(btpUsecase)
        log.write(logtype.HEADER, "Initiate creation of service instances")

        # First add all instance names to the services
        for service in btpUsecase.definedServices:
            instancename = createInstanceName(btpUsecase, service)
            service["instancename"] = instancename

        # Check whether there are services with the same instance name
        # If there are, it's not safe to create the service instances
        for service in btpUsecase.definedServices:
            instanceName = service["instancename"]
            counter = 0
            for thisService in btpUsecase.definedServices:
                thisInstanceName = thisService["instancename"]
                if thisInstanceName == instanceName:
                    counter += 1
            if counter > 1:
                log.write(logtype.ERROR, "there is more than one service with the instance name >" + instanceName + "<. Please fix that before moving on.")
                sys.exit(os.EX_DATAERR)

        # Now create all the service instances
        for service in btpUsecase.definedServices:
            serviceName = service["name"]
            # servicePlan = service["plan"]
            # Quickly initiate the creation of all service instances (without waiting until they are all created)
            if "requiredServices" in service:
                for requiredService in service["requiredServices"]:
                    thisService = getServiceByServiceName(btpUsecase, requiredService)
                    if thisService is not None:
                        current_time = 0
                        search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(btpUsecase, thisService)
                        # Wait until thisService has been created and is available
                        while usecaseTimeout > current_time:
                            [servicebroker, status] = get_cf_service_status(btpUsecase, thisService)
                            if (status == "create succeeded"):
                                log.write(logtype.SUCCESS, "service >" + requiredService + "< now ready as pre-requisite for service >" + serviceName + "<")
                                if service["category"] == "SERVICE" or service["category"] == "ELASTIC_SERVICE":
                                    service = create_cf_service(btpUsecase, service)
                                else:
                                    log.write(logtype.INFO, "this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                                    service["status"] = "create succeeded"
                                break
                            else:
                                log.write(logtype.CHECK, "waiting for service >" + requiredService + "< (status >" + status +
                                          "<) to finish as pre-requisite for service >" + serviceName + "< (trying again in " + str(search_every_x_seconds) + "s)")

                            time.sleep(search_every_x_seconds)
                            current_time += search_every_x_seconds
                    else:
                        log.write(logtype.ERROR, "did not find the defined required service >" + requiredService +
                                  "<, which is a pre-requisite for the service >" + serviceName + "<. Please check your configuration file!")
            else:
                if service["category"] == "SERVICE" or service["category"] == "ELASTIC_SERVICE":
                    service = create_cf_service(btpUsecase, service)
                else:
                    if service["category"] == "CF_CUP_SERVICE":
                        service = create_cf_cup_service(btpUsecase, service)
                    else:
                        log.write(logtype.INFO, "this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                        service["status"] = "create succeeded"


def get_cf_service_status(btpUsecase, service):
    instance_name = service["instancename"]

    command = "cf service \"" + instance_name + "\""
    p = runShellCommand(btpUsecase, command, logtype.CHECK, None)
    result = p.stdout.decode()

    service_broker = getKeyFromCFOutput(result, "service broker")
    status = getKeyFromCFOutput(result, "status")
    return [service_broker, status]


def get_cf_service_deletion_status(btpUsecase, service):
    instance_name = service["instancename"]
    command = "cf service \"" + instance_name + "\""
    p = runShellCommandFlex(btpUsecase, command, logtype.CHECK, None, False, False)
    result = p.stdout.decode()
    if "FAILED" in result:
        return "deleted"
    else:
        return "not deleted"
