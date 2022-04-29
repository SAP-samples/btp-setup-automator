from libs.python.helperCommandExecution import runShellCommand, runCommandAndGetJsonResult, login_cf, runShellCommandFlex
from libs.python.helperGeneric import getServiceByServiceName, createInstanceName, getTimingsForStatusRequest
from libs.python.helperJson import convertCloudFoundryCommandForSingleServiceToJson, convertStringToJson, convertCloudFoundryCommandOutputToJson, dictToString
import time
import os
import sys
import logging

log = logging.getLogger(__name__)


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
    orgid = None
    org = None

    command = "btp --format json list account/environment-instance --subaccount '" + accountMetadata["subaccountid"] + "'"
    result = runCommandAndGetJsonResult(btpUsecase, command, "INFO", None)

    if "orgid" in accountMetadata:
        orgid = accountMetadata["orgid"]

    # If the for loop didn't return any value, the orgid wasn't found
    for instance in result["environmentInstances"]:
        if instance["subaccountGUID"] == btpUsecase.subaccountid:
            labels = convertStringToJson(instance["labels"])
            org = labels["Org Name:"]
            return instance["platformId"], org

    return orgid, org


def checkIfCFSpaceAlreadyExists(btpUsecase):
    cfspacename = btpUsecase.cfspacename

    command = "cf spaces"
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    lines = result.splitlines()

    for line in lines:
        if cfspacename == line:
            return True
    return False


def getStatusResponseFromCreatedInstance(btpUsecase, instancename):
    command = "cf service '" + instancename + "'"
    p = runShellCommand(btpUsecase, command, "INFO", None)
    result = p.stdout.decode()
    jsonResults = convertCloudFoundryCommandForSingleServiceToJson(result)
    return jsonResults


def checkIfAllServiceInstancesCreated(btpUsecase):
    command = "cf services"
    p = runShellCommand(btpUsecase, command, "INFO", None)
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
            if service.name == name and service.plan == plan and service.instancename == instancename and service.successInfoShown is False:
                if status != "create succeeded" and status != "update succeeded":
                    allServicesCreated = False
                    service.status = "NOT READY"
                    service.successInfoShown = False
                else:
                    log.success("Service instance for service >" + service.name + "< (plan " + service.plan + ") is now available")
                    service.servicebroker = servicebroker
                    service.successInfoShown = True
                    service.status = "create succeeded"
                    service.statusResponse = getStatusResponseFromCreatedInstance(btpUsecase, instancename)
    return allServicesCreated


def try_until_cf_space_done(btpUsecase, command, message, spacename, search_every_x_seconds, timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0

    while timeout_after_x_seconds > current_time:
        number_of_tries += 1
        p = runShellCommand(btpUsecase, command, "INFO", message)
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
    instancename = service.instancename

    plan = service.plan

    if service.planCatalogName is not None:
        plan = service.planCatalogName

    command = "cf create-service '" + service.name + "' '" + plan + "' '" + instancename + "'"

    if service.parameters is not None:
        thisParameter = dictToString(service.parameters)
        command += " -c '" + thisParameter + "'"
    elif service.serviceparameterfile is not None:
        command += f" -c {service.serviceparameterfile}"
    message = "Create instance >" + instancename + "< for service >" + service.name + "< and plan >" + plan + "<"
    runShellCommand(btpUsecase, command, "INFO", message)
    return service


def cf_cup_service_already_exists(btpUsecase, instance_name):
    command = "cf service '" + instance_name + "'"
    p = runShellCommandFlex(btpUsecase, command, "CHECK", None, False, False)
    result = p.stdout.decode()
    if "FAILED" in result:
        return False
    else:
        return True


def create_cf_cup_service(btpUsecase, service):
    instance_name = service.name
    cfCupServiceAlreadyExists = cf_cup_service_already_exists(btpUsecase, instance_name)

    if cfCupServiceAlreadyExists is False:
        command = "cf cups '" + instance_name + "' "

        if service.parameters is not None:
            thisParameter = str(service.parameters)
            command += thisParameter
            message = "Create CF cups instance for service >" + instance_name + "<"
            runShellCommandFlex(btpUsecase, command, "INFO", message, True, True)
            log.info("created CF cup service >" + instance_name + "<")
        else:
            message = "missing parameter for the CF cups service >" + instance_name + "<. Won't create the CF cup service."
            log.warning(message)
    else:
        log.info("the user provided service >" + instance_name + "< already exists and won't be created newly.")

    return service


def initiateCreationOfServiceInstances(btpUsecase):
    createServiceInstances = btpUsecase.definedServices is not None and len(btpUsecase.definedServices) > 0

    if createServiceInstances is True:
        login_cf(btpUsecase)
        log.header("Initiate creation of service instances")

        # First add all instance names to the services
        for service in btpUsecase.definedServices:
            instancename = createInstanceName(btpUsecase, service)
            service.instancename = instancename

        # Check whether there are services with the same instance name
        # If there are, it's not safe to create the service instances
        for service in btpUsecase.definedServices:
            instanceName = service.instancename
            counter = 0
            for thisService in btpUsecase.definedServices:
                thisInstanceName = thisService.instancename
                if thisInstanceName == instanceName:
                    counter += 1
            if counter > 1:
                log.error("there is more than one service with the instance name >" + instanceName + "<. Please fix that before moving on.")
                sys.exit(os.EX_DATAERR)

        serviceInstancesToBeCreated = []
        # Restrict the creation of service instances to those
        # that have been set to entitleOnly to False (default)
        for service in btpUsecase.definedServices:
            if service.entitleonly is False:
                serviceInstancesToBeCreated.append(service)

        # Now create all the service instances
        for service in serviceInstancesToBeCreated:
            serviceName = service.name
            # servicePlan = service.plan
            # Quickly initiate the creation of all service instances (without waiting until they are all created)
            if service.requiredServices is not None and len(service.requiredServices) > 0:
                for requiredService in service.requiredServices:
                    thisService = getServiceByServiceName(btpUsecase, requiredService)
                    if thisService is not None:
                        current_time = 0
                        search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(btpUsecase, thisService)
                        # Wait until thisService has been created and is available
                        while usecaseTimeout > current_time:
                            [servicebroker, status] = get_cf_service_status(btpUsecase, thisService)
                            if (status == "create succeeded" or status == "update succeeded"):
                                log.success("service >" + requiredService + "< now ready as pre-requisite for service >" + serviceName + "<")
                                if service.category == "SERVICE" or service.category == "ELASTIC_SERVICE":
                                    service = create_cf_service(btpUsecase, service)
                                else:
                                    log.info("this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                                    service.status = "create succeeded"
                                break
                            else:
                                log.check("waiting for service >" + requiredService + "< (status >" + status +
                                          "<) to finish as pre-requisite for service >" + serviceName + "< (trying again in " + str(search_every_x_seconds) + "s)")

                            time.sleep(search_every_x_seconds)
                            current_time += search_every_x_seconds
                    else:
                        log.error("did not find the defined required service >" + requiredService +
                                  "<, which is a pre-requisite for the service >" + serviceName + "<. Please check your configuration file!")
            else:
                if service.category == "SERVICE" or service.category == "ELASTIC_SERVICE":
                    service = create_cf_service(btpUsecase, service)
                else:
                    if service.category == "CF_CUP_SERVICE":
                        service = create_cf_cup_service(btpUsecase, service)
                    else:
                        log.info("this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                        service.status = "create succeeded"


def get_cf_service_status(btpUsecase, service):
    instance_name = service.instancename

    command = "cf service '" + instance_name + "'"
    p = runShellCommand(btpUsecase, command, "CHECK", None)
    result = p.stdout.decode()

    service_broker = getKeyFromCFOutput(result, "service broker")
    status = getKeyFromCFOutput(result, "status")
    return [service_broker, status]


def get_cf_service_deletion_status(btpUsecase, service):
    instance_name = service["instancename"]
    command = "cf service '" + instance_name + "'"
    p = runShellCommandFlex(btpUsecase, command, "CHECK", None, False, False)
    result = p.stdout.decode()
    if "FAILED" in result:
        return "deleted"
    else:
        return "not deleted"
