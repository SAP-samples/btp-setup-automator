from libs.python.helperCommandExecution import *
from libs.python.helperGeneric import *
from libs.python.helperJson import *

import time

def getKeyFromCFOutput(cfoutput, key):
    result = None

    lines = cfoutput.splitlines()
    for line in lines:
        thisLineSplit = line.split(":")
        if len(thisLineSplit) == 2 and thisLineSplit[0] == key:
            result = thisLineSplit[1].strip()
    return result

def checkIfCFEnvironmentAlreadyExists(btpUsecase):
    accountMetadata= btpUsecase.accountMetadata

    command="btp --format json list account/environment-instance --subaccount " + accountMetadata["subaccountid"]
    result = runCommandAndGetJsonResult(btpUsecase, command,logtype.INFO, None)

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

    command="cf spaces"
    p = runShellCommand(btpUsecase, command, logtype.INFO, None)
    result = p.stdout.decode()
    lines = result.splitlines()
    
    for line in lines:
        if cfspacename == line:
            return True
    return False

def checkIfAllServiceInstancesCreated(btpUsecase):
    log = btpUsecase.log

    command="cf services"
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
            if service["name"] == name and service["plan"] == plan and service["instancename"] == instancename and service["successInfoShown"] == False:
                if status != "create succeeded":
                    allServicesCreated = False
                    service["status"] = "NOT READY"          
                    service["successInfoShown"]  = False
                else:
                    log.write( logtype.SUCCESS, "Service instance for service >" + service["name"] + "< (plan " + service["plan"] + ") is now available")
                    service["servicebroker"] = servicebroker
                    service["successInfoShown"]  = True          
                    service["status"] = "create succeeded"
    return allServicesCreated


def try_until_cf_space_done(btpUsecase, command,message, spacename, search_every_x_seconds,timeout_after_x_seconds):
    result = "ERROR"

    current_time = 0
    number_of_tries = 0
    
    while timeout_after_x_seconds > current_time:
        number_of_tries+=1
        checkMessage =  message + " (try " + str(number_of_tries) + " - trying again in " + str(search_every_x_seconds) + "s)"
        p = runShellCommand(btpUsecase, command, logtype.INFO, message)
        result = p.stdout.decode()
        lines = result.splitlines()
        
        for line in lines:
            if line == "name":
                continue
            if spacename == line:
                return "DONE"

        time.sleep(search_every_x_seconds)
        current_time+=search_every_x_seconds
    
    return result

def create_cf_service(btpUsecase, service):
    instancename = createInstanceName(btpUsecase, service)
    service["instancename"] = instancename

    command = "cf create-service \"" + service["name"] + "\" \"" + service["plan"] + "\"  \"" + instancename + "\"" 
    
    if "parameters" in service:
        thisParameter = dictToString(service["parameters"])
        command += " -c '" + thisParameter + "'"
    message = "Create instance >" + instancename + "< for service >" + service["name"] + "< and plan >" + service["plan"] +"<"
    p = runShellCommand(btpUsecase, command, logtype.INFO, message)
    return service

def initiateCreationOfServiceInstances(btpUsecase):
    log = btpUsecase.log

    if btpUsecase.definedServices != None and len(btpUsecase.definedServices) > 0:
        login_cf(btpUsecase)
        log.write( logtype.HEADER, "Initiate creation of service instances")

        # Now create all the service instances
        for service in btpUsecase.definedServices:
            serviceName = service["name"]
            servicePlan = service["plan"]
            # Quickly initiate the creation of all service instances (without waiting until they are all created)
            if "requiredServices" in service:
                for requiredService in service["requiredServices"]:
                    thisService = getServiceByServiceName(btpUsecase, requiredService)
                    if thisService != None:
                        current_time = 0
                        search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(btpUsecase, thisService)
                        ## Wait until thisService has been created and is available
                        while usecaseTimeout > current_time:                
                            [servicebroker, status] = get_cf_service_status(btpUsecase, thisService)
                            if (status == "create succeeded"):
                                log.write( logtype.SUCCESS, "service >" + requiredService + "< now ready as pre-requisite for service >" + serviceName + "<")
                                if service["category"] == "SERVICE" or service["category"] == "ELASTIC_SERVICE":
                                    service = create_cf_service(btpUsecase, service)
                                else:
                                    log.write(logtype.INFO, "this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                                    service["status"] = "create succeeded"
                                break
                            else:
                                log.write( logtype.CHECK, "waiting for service >" + requiredService + "< (status >" + status + "<) to finish as pre-requisite for service >" + serviceName + "< (trying again in " + str(search_every_x_seconds) + "s)")

                            time.sleep(search_every_x_seconds)
                            current_time+= search_every_x_seconds
                    else:
                        log.write( logtype.ERROR, "did not find the defined required service >" + requiredService + "<, which is a pre-requisite for the service >" + serviceName + "<. Please check your configuration file!")
            else:
                if service["category"] == "SERVICE" or service["category"] == "ELASTIC_SERVICE":
                    service = create_cf_service(btpUsecase, service)
                else:
                    log.write(logtype.INFO, "this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
                    service["status"] = "create succeeded"


def get_cf_service_status(btpUsecase, service):
    service_name  = service["name"]
    instance_name = service["instancename"]

    command= "cf service \"" + instance_name + "\""
    message = "creation status of service instance >" + instance_name + "< for service >" + service_name + "<"
    p = runShellCommand(btpUsecase, command, logtype.CHECK, None)
    result = p.stdout.decode()
    
    service_broker = getKeyFromCFOutput(result , "service broker")
    status = getKeyFromCFOutput(result , "status")
    return [service_broker, status]

def get_cf_service_deletion_status(btpUsecase, service):
    service_name  = service["name"]
    instance_name = service["instancename"]

    command= "cf service \"" + instance_name + "\""
    message = "check deletion status of service instance >" + instance_name + "< for service >" + service_name + "<"
    p = runShellCommandFlex(btpUsecase, command, logtype.CHECK, None, False, False)
    result = p.stdout.decode()
    if "FAILED" in result:
        return "deleted"
    else:
        return "not deleted"
