from libs.python.helperCommandExecution import runShellCommand
from libs.python.helperGeneric import getServiceByServiceName, createInstanceName, getTimingsForStatusRequest
from libs.python.helperJson import convertCloudFoundryCommandOutputToJson, convertStringToJson
from libs.python.helperEnvCF import deleteCFServiceInstance, deleteCFServiceKeysAndWait, get_cf_service_deletion_status, get_cf_service_key, get_cf_service_status, create_cf_service, create_cf_cup_service, getStatusResponseFromCreatedInstance
from libs.python.helperEnvBTP import get_btp_service_status, create_btp_service, getStatusResponseFromCreatedBTPInstance, createBtpServiceBinding, deleteBtpServiceBindingAndWait, deleteBtpServiceInstance, getBtpServiceDeletionStatus
from libs.python.helperEnvKyma import createKymaServiceBinding, deleteKymaServiceBindingAndWait, deleteKymaServiceInstance, get_kyma_service_status, create_kyma_service, getKymaServiceDeletionStatus, getStatusResponseFromCreatedKymaInstance
import time
import os
import sys
import logging

log = logging.getLogger(__name__)


def checkIfAllServiceInstancesCreated(btpUsecase):

    cloudfoundryServices = []
    kubernetesServices = []
    otherServices = []

    allServicesCreated = True

    # Check the service Categories of all services ... do we have a CF, Kubernetes and/or BTP CLI Service
    for service in btpUsecase.definedServices:
        if service.entitleonly is False:
            if service.targetenvironment == "cloudfoundry":
                cloudfoundryServices.append(service)

            elif service.targetenvironment == "kymaruntime":
                kubernetesServices.append(service)

            else:
                otherServices.append(service)

    if cloudfoundryServices:

        command = "cf services"
        p = runShellCommand(btpUsecase, command, "INFO", None)
        result = p.stdout.decode()
        jsonResultsCF = convertCloudFoundryCommandOutputToJson(result)

        for thisJson in jsonResultsCF:
            name = thisJson.get("service")
            if name is None:
                name = thisJson.get("offering")

            plan = thisJson.get("plan")
            instancename = thisJson.get("name")
            status = thisJson.get("last operation")
            servicebroker = thisJson.get("broker")
            for service in btpUsecase.definedServices:
                if service.name == name and service.plan == plan and service.instancename == instancename and service.successInfoShown is False:
                    if status != "create succeeded" and status != "update succeeded":
                        allServicesCreated = False
                        service.status = "NOT READY"
                        service.successInfoShown = False
                    else:
                        log.success("Service instance for service >" + service.name +
                                    "< (plan " + service.plan + ") is now available")
                        service.servicebroker = servicebroker
                        service.successInfoShown = True
                        service.status = "create succeeded"
                        service.statusResponse = getStatusResponseFromCreatedInstanceGen(
                            btpUsecase, instancename, service)

    if kubernetesServices:

        command = "kubectl get ServiceInstance -n " + btpUsecase.k8snamespace + \
            " --kubeconfig " + btpUsecase.kubeconfigpath + " --output json"
        p = runShellCommand(btpUsecase, command, "INFO", None)

        jsonResultsK8s = convertStringToJson(p.stdout.decode())

        jsonResultsK8sServiceInstances = jsonResultsK8s.get("items")

        for thisJson in jsonResultsK8sServiceInstances:
            name = thisJson.get("spec").get("serviceOfferingName")

            plan = thisJson.get("spec").get("servicePlanName")
            instancename = thisJson.get("metadata").get("name")
            status = thisJson.get("status").get("ready")
            for service in btpUsecase.definedServices:
                if service.name == name and service.plan == plan and service.instancename == instancename and service.successInfoShown is False:
                    if status != "True":
                        allServicesCreated = False
                        service.status = "NOT READY"
                        service.successInfoShown = False
                    else:
                        log.success("Service instance for service >" + service.name +
                                    "< (plan " + service.plan + ") is now available")
                        service.successInfoShown = True
                        service.status = "create succeeded"
                        service.statusResponse = getStatusResponseFromCreatedInstanceGen(
                            btpUsecase, instancename, service)

    if otherServices:
        command = "btp --format json list services/instance --subaccount " + \
            btpUsecase.accountMetadata.get("subaccountid")
        p = runShellCommand(btpUsecase, command, "INFO", None)

        jsonResultsBTP = convertStringToJson(p.stdout.decode())

        for thisJson in jsonResultsBTP:

            if thisJson.get("context").get("origin") == "sapcp":
                serviceId = thisJson.get("id")
                instancename = thisJson.get("context").get("instance_name")
                status = str(thisJson.get("ready"))
                subaccountId = thisJson.get("context").get("subaccount_id")
                serviceplanId = thisJson.get("service_plan_id")

                command = "btp --format json get services/plan --id " + \
                    serviceplanId + " --subaccount " + subaccountId

                q = runShellCommand(btpUsecase, command, "INFO", None)

                jsonResultServicePlan = convertStringToJson(q.stdout.decode())

                servicePlanName = jsonResultServicePlan.get("name")

                for service in btpUsecase.definedServices:
                    if service.id == serviceId and service.plan == servicePlanName and service.instancename == instancename and service.successInfoShown is False:
                        if status != "True":
                            allServicesCreated = False
                            service.status = "NOT READY"
                            service.successInfoShown = False
                        else:
                            log.success("Service instance for service >" + service.name +
                                        "< (plan " + service.plan + ") is now available")
                            service.successInfoShown = True
                            service.status = "create succeeded"
                            service.statusResponse = getStatusResponseFromCreatedInstanceGen(
                                btpUsecase, instancename, service)

    return allServicesCreated


def initiateCreationOfServiceInstances(btpUsecase):
    createServiceInstances = btpUsecase.definedServices is not None and len(
        btpUsecase.definedServices) > 0

    if createServiceInstances is True:
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
                log.error("there is more than one service with the instance name >" +
                          instanceName + "<. Please fix that before moving on.")
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
            # Quickly initiate the creation of all service instances (without waiting until they are all created)
            if service.requiredServices is not None and len(service.requiredServices) > 0:
                for requiredService in service.requiredServices:
                    thisService = getServiceByServiceName(
                        btpUsecase, requiredService)
                    if thisService is not None:
                        current_time = 0
                        search_every_x_seconds, usecaseTimeout = getTimingsForStatusRequest(
                            btpUsecase, thisService)
                        # Wait until thisService has been created and is available
                        while usecaseTimeout > current_time:
                            status = get_service_status(
                                btpUsecase, thisService, service.targetenvironment)
                            if (status == "create succeeded" or status == "update succeeded"):
                                log.success(
                                    "service >" + requiredService + "< now ready as pre-requisite for service >" + serviceName + "<")
                                if service.category == "SERVICE" or service.category == "ELASTIC_SERVICE":
                                    service = createServiceInstance(
                                        btpUsecase, service, service.targetenvironment, service.category)
                                else:
                                    log.info(
                                        "this service >" + serviceName + "< is not of type SERVICE or ELASTIC_SERVICE and a service instance won't be created")
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
                service = createServiceInstance(
                    btpUsecase, service, service.targetenvironment, service.category)


def get_service_status(btpUsecase, service, targetEnvironment):
    status = None

    if targetEnvironment == "cloudfoundry":
        [servicebroker, status] = get_cf_service_status(btpUsecase, service)
    elif targetEnvironment == "kymaruntime":
        status = get_kyma_service_status(btpUsecase, service)
    elif targetEnvironment == "sapbtp":
        status = get_btp_service_status(btpUsecase, service)
    else:
        log.error(
            "The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return status


def createServiceInstance(btpUsecase, service, targetEnvironment, serviceCategory):
    if targetEnvironment == "cloudfoundry":
        if serviceCategory == "SERVICE" or service.category == "ELASTIC_SERVICE":
            service = create_cf_service(btpUsecase, service)
        elif serviceCategory == "CF_CUP_SERVICE":
            service = create_cf_cup_service(btpUsecase, service)
    elif targetEnvironment == "kymaruntime":
        service = create_kyma_service(btpUsecase, service)
    elif targetEnvironment == "sapbtp":
        service = create_btp_service(btpUsecase, service)
    else:
        log.error(
            "The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return service


def getStatusResponseFromCreatedInstanceGen(btpUsecase, instancename, service):
    statusResponse = None

    if service.targetenvironment == "cloudfoundry":
        statusResponse = getStatusResponseFromCreatedInstance(
            btpUsecase, instancename)
    elif service.targetenvironment == "kymaruntime":
        statusResponse = getStatusResponseFromCreatedKymaInstance(
            btpUsecase, instancename)
    elif service.targetenvironment == "sapbtp":
        statusResponse = getStatusResponseFromCreatedBTPInstance(
            btpUsecase, instancename, service)
    else:
        log.error("The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return statusResponse


def deleteServiceKeysAndWait(key, service, btpUsecase):
    targetenvironment = service.get("targetenvironment")
    if targetenvironment == "cloudfoundry":
        deleteCFServiceKeysAndWait(key, service, btpUsecase)
    elif targetenvironment == "kymaruntime":
        deleteKymaServiceBindingAndWait(key, service, btpUsecase)
    elif targetenvironment == "sapbtp":
        deleteBtpServiceBindingAndWait(key, service, btpUsecase)
    else:
        log.error("The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)


def deleteServiceInstance(service, btpUsecase):
    targetenvironment = service.get("targetenvironment")
    statusResponse = None

    if targetenvironment == "cloudfoundry":
        statusResponse = deleteCFServiceInstance(service, btpUsecase)
    elif targetenvironment == "kymaruntime":
        statusResponse = deleteKymaServiceInstance(service, btpUsecase)
    elif targetenvironment == "sapbtp":
        deleteBtpServiceInstance(service, btpUsecase)
    else:
        log.error("The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return statusResponse


def getServiceDeletionStatus(service, btpUsecase):
    targetenvironment = service.get("targetenvironment")
    statusResponse = None

    if targetenvironment == "cloudfoundry":
        statusResponse = get_cf_service_deletion_status(btpUsecase, service)
    elif targetenvironment == "kymaruntime":
        statusResponse = getKymaServiceDeletionStatus(service, btpUsecase)
    elif targetenvironment == "sapbtp":
        statusResponse = getBtpServiceDeletionStatus(service, btpUsecase)
    else:
        log.error("The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return statusResponse


def createServiceKey(serviceKey, service, btpUsecase):
    targetenvironment = service.targetenvironment
    statusResponse = None

    if targetenvironment == "cloudfoundry":
        statusResponse = get_cf_service_key(
            btpUsecase, service.instancename, serviceKey)
    elif targetenvironment == "kymaruntime":
        statusResponse = createKymaServiceBinding(
            btpUsecase, service, serviceKey)
    elif targetenvironment == "sapbtp":
        statusResponse = createBtpServiceBinding(btpUsecase, service.id, service.instancename, serviceKey)
    else:
        log.error("The targetenvironment is not supported ")
        sys.exit(os.EX_DATAERR)

    return statusResponse
