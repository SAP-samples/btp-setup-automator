# Configuration of the BTP-SETUP-AUTOMATOR

This page provides you a detailed description of the `btp-setup-automator` to facilitate own setups and configurations.

## The Structure and Flow

The CLI of the `btp-setup-automator` displays all its available options via:

```bash
./btpsa -h
```

The most convenient way to interact with the CLI is to provide a *parameter file* (option `-parameterfile <filename>`). This file provides the basic setup information needed by the CLI to be able to work. We describe the details in the section ["The Parameter File"](#the-parameter-file). You find all available parameters in the file [`libs\json\paramBtpSetupAutomator.json`](libs/json/paramBtpSetupAutomator.json)

The specifics of the setup are provided via the *usecase file* that is referenced in the parameter file. Here you find the parameterization of the different environments and services you want to provision. We describe the details in the section ["The Usecase File"](#the-usecase-file).

The `btp-setup-automator` takes these files and executes the necessary actions to provide the requested resources and executes the provides commands. It executes the following steps:

1. It checks if the global account is capable of providing the requested resources. It checks if all configured services and app subscriptions are available.
2. It executes all commands provided in the section `executeBeforeAccountSetup` of your usecase file.
3. It creates the subaccount for the resources if it is not already existing.This comprises adding the subaccount admin(s).
4. It assigns the entitlements for the environments, services and app subscriptions.
5. It creates the environments i.e. Cloud Foundry or Kyma.
6. It triggers the creation of app subscriptions and service instances. The corresponding role collections are assigned to the subaccount admins.
7. It creates the role collections specified in the usecase file.
8. It assigns the role collections to the subaccount admins
9. It executes actions necessary after the environment is setup e.g., downloading the `kubeconfig` file for a Kyma environment.
10. It executes all commands provided in the section `executeAfterAccountSetup` of your usecase file.
11. In case pruning is activated, the corresponding steps to prune the usecase and/or subaccount setup are executed.

The flow makes it clear that this tool provides everything for the setup *per se* that can be parameterized and even offers further degrees of freedom via the steps for command execution and this way easily setting up complete applications in one go.

Let us now take a closer look into the files needed for the setup.

## The Parameter File

The main file for the setup is the `parameter file`. It is written in JSON format. It provides the basic information for the `btp-setup-automator` to run.

All available parameters are described in the file [`libs\json\paramBtpSetupAutomator.json`](libs/json/paramBtpSetupAutomator.json). As there are quite some we will focus on the main cases.

### Basics

### Authentication

### Sometimes You Need to Wait ☕

Some provisioning actions on BTP take time. In some cases the `btp-setup-automator` needs to wait for them to be finished. However, we want to have some safeguarding aka circuit breakers in place. To achieve this you can specify the maximum waiting time as well as the polling interval i.e., in which time intervals shall the `btp-setup-automator` check if the provisioning is finished.

In general you achieve this via the following parameters:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `repeatstatustimeout` | int | seconds | 4200 | This value defines the timeout in seconds after which requests to check if the service etc. is available should be stopped.
| `repeatstatusrequest` | int | seconds | 4 | This value defines the interval in seconds that requests are sent to check if the service etc. is available.

> 📝 Tip - You can specify these parameters globally or per service definition. In the later case you ned to add them to the `usecase file`

The Kyma is a special snowflake as the provisioning takes quite some time. That is why you have dedicated parameters for the timeout settings:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `waitForKymaEnvironmentCreation` | boolean | na | true | This parameters defines if you want to wait for the Kyma environment to be created. If it is set to `false` the `btp-setup-automator` will **not** be able to download the `kubeconfig` file.
| `timeoutLimitForKymaCreationInMinutes` | int | minutes | 40 | This value defines the timeout in **minutes** after which requests to check if the Kyma environment is available should be stopped.
| `pollingIntervalForKymaCreationInMinutes` | int | minutes | 5 | This value defines the interval in **minutes** that requests are sent to check if the Kyma environment is available.

The same goes for pruning the Kyma environment:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `timeoutLimitForKymaDeprovisioningInMinutes` | int | minutes | 40 | This value defines the timeout in **minutes** after which requests to check if the Kyma environment is deleted should be stopped.
| `pollingIntervalForKymaDeprovisioningInMinutes` | int | minutes | 5 | This value defines the interval in **minutes** that requests are sent to check if the Kyma environment is available.

### Pruning - Handle with Care

After setting up everything you have the option to tear everything down again. One scenario might be to use the  `btp-setup-automator` as a tool to enable a integration or end2end scenario for your app, namely setting things up, checking if the work (via `executeAfterAccountSetup` commands) and then remove everything again.

You specify the behavior via two parameters:

| Parameter | Type | Default Value | Description
| --- | --- | --- | ---
| `pruneusecase`    | boolean | false | If this parameter is set to true the use case setup will be removed. The subaccount will **not** be deleted.
| `prunesubaccount` | boolean | false | If this parameter is set to true the subaccount setup will be removed. This also comprises the removal of the artifacts defined in the usecase. The usecase deletion wil be triggered implicitly independent of the `pruneusecase` parameter.  

> ⚠ NOTE: Be aware that all setups done via commands must be reversed again. This can be done via commands provided in the `executeToPruneUseCase` section.  

### Parameter Examples

You find several examples for parameter files in the folder `usecases/other/unittests/parameterfiles`

## The Usecase File

The `usecase file` contains all the detail information and parameterization of the setup of environments, services etc. It is written in JSON format. While the `parameter file` defines the flow and generic setup parameters, this file contains the specification of the scenario you want to setup on SAP BTP.

Every usecase file start with some generic metadata that specifies the content named `aboutThisUseCase` that contains the details like name, author, description, status and alike. Here an example:

```json
{
  "aboutThisUseCase": {
    "name": "Deploy full-stack CAP application running in SAP Launchpad (on BTP TRIAL account)",
    "description": "This usecase provides all necessary information to create the necessary service instances and app subscription for a CAP application and to deploy that application on a SAP BTP account.",
    "author": "rui.nogueira@sap.com",
    "testStatus": "tested successfully",
    "usageStatus": "READY TO BE USED",
    "relatedLinks": [
      "https://developers.sap.com/tutorials/btp-app-launchpad-service.html"
    ]
  }
}  
```

The technical data in this file is dependent on your services. To make things a bit more tangible, Let us take a look at two samples in the following sections to showcase the fundamentals.

### Sample 1 - Plain XSUAA Service

Let us assume that you want to provision a XSUAA instance via the tool. This means that we need to specify the service like that:

```json
{
  "aboutThisUseCase": {
    "name": "Setup IAS",
    "description": "This usecase provides the configuration of services to create trust between the subaccount and a customer IAS tenant",
    ...
  },
  "services": [
    {
      "category": "SERVICE",
      "name": "xsuaa",
      "plan": "apiaccess",
      "instancename": "xsuaa_api",
      "repeatstatusrequest": "5",
      "repeatstatustimeout": "200",
      "createServiceKeys": [
        "myServiceKey1"
      ]
    }
  ],
  "admins": []
}
```

You specify all the artifacts in the `services` section as a JSON array. For XSUAA we have an artifact of the `category` `SERVICE` and specify the relevant input for the creation like the name of the service aka "which service do you want to create" (`"name": "xsuaa"`), the plan that should be used (`"plan": "apiaccess"`) the name of the service instance (`"instancename": "xsuaa_api"`) and so on.

This example also shows the service specific definition of the parameters `repeatstatusrequest` and `repeatstatustimeout` mentioned above.

You also see a `admins` attribute that points to an empty array. This allows you to specifiy further administrators. The email specified in the `parameter file` will automatically be added to the administrators and does not need to be added explicitly.

### Sample 2 - Plain Kyma Provisioning

### Usecase Examples

You find several examples for parameter files in the folder `usecases/released`.

## Further Information

As the `btp-setup-automator` is leveraging the capabilities of the SAP btp CLI we recommend to have a look into the documentation of the CLI when it comes to the detailed parameters for single services. You fin the information in [help.sap.com](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/7c6df2db6332419ea7a862191525377c.html)