# Detailed configuration

This page provides you a detailed description of the `btp-setup-automator` to facilitate own setups and configurations.

## The Structure and Flow

The CLI of the `btp-setup-automator` displays all its available options via:

```bash
./btpsa -h
```

The most convenient way to interact with the CLI is to provide a *parameter file* (option `-parameterfile <filename>`). This file provides the basic setup information needed by the CLI to be able to work. We describe the details in the section ["The Parameter File"](#the-parameter-file). You find all available parameters in the file [`libs/btpsa-parameters.json`](../libs/btpsa-parameters.json).

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

Let us take a closer look into the files needed for the setup.

## The Parameter File

The main file for the setup is the `parameter file` written in JSON format. It provides the basic information for the `btp-setup-automator` to run.

All available parameters are described in the file [`libs/btpsa-parameters.json`](../libs/btpsa-parameters.json). As there are quite some we will focus on the main cases.

### Basics

The basic setup in the `parameter file` typically contains the following information:

```json
"usecasefile": "path/to/usecase/file.json",
"email": "some.email@somedomain.com"
"region": "eu10",
"subaccountname": "My own subacccount name",
```

The main information is the link to the `usecasefile` that contains the detailed information of the setup and is discussed in the section ["The Parameter File"](#the-parameter-file). This is also the place to specify further generic information like your `email`, the `region` where the deployment should take place and how you want to name you subaccount via `subaccountname`.

You can also provide further information like the name of your Cloud Foundry sapce (via `cfspacename`):

```json
"cfspacename": "development",
```

Think about the basics of this file as the very basic information needed to setup resources in SAP BTP. Some of them are defaulted (see [`libs/btpsa-parameters.json`](../libs/btpsa-parameters.json) for the default values).

### Authentication

The parameter to specify how the login is executed is the `loginmethod` needed to access the SAP BTP. You have two options:

- `basicAuthentication`
- `sso`

If you choose `basicAuthentication` you need to provide username and password. You can do that interactively when executing the CLI.

If you choose `sso` you need to execute the login flow via a link in the browser. This is then necessary for login via SAP btp CLI as well as for the Cloud Foundry CLI.

> 📝 Tip - This parameter has no influence on the logon flow when you login to Kyma (implicitly when executing `kubectl` commands). Here you will have an OIDC flow that always redirects you to the browser.

### Sometimes You Need to Wait ☕

Some provisioning actions on BTP take time and in some cases the `btp-setup-automator` needs to wait for them to be finished. However, we want to have some safeguarding aka *circuit breakers* in place. You can therefore specify the *maximum waiting time* as well as the *polling interval* i.e., in which time intervals shall the `btp-setup-automator` check if the provisioning is finished.

This is reflected by the following parameters:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `repeatstatustimeout` | int | seconds | 4200 | This parameter defines the timeout in seconds after which requests to check if the service etc. is available should be stopped.
| `repeatstatusrequest` | int | seconds | 4 | This parameter defines the interval in seconds that requests are sent to check if the service etc. is available.

> 📝 Tip - You can specify these parameters globally or per service definition. In the later case you need to place them in the `usecase file`.

The Kyma environment is a special snowflake as the provisioning takes quite some time. That is why you have dedicated parameters for the timeout settings:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `waitForKymaEnvironmentCreation` | boolean | na | true | This parameter defines if you want to wait for the Kyma environment to be created. If it is set to `false` the `btp-setup-automator` will **not** be able to download the `kubeconfig` file.
| `timeoutLimitForKymaCreationInMinutes` | int | minutes | 40 | This parameter defines the timeout in **minutes** after which requests to check if the Kyma environment is available should be stopped.
| `pollingIntervalForKymaCreationInMinutes` | int | minutes | 5 | This parameter defines the interval in **minutes** that requests are sent to check if the Kyma environment is available.

The same goes for pruning the Kyma environment:

| Parameter | Type | Unit |Default Value | Description
| --- | --- | --- | --- | ---
| `timeoutLimitForKymaDeprovisioningInMinutes` | int | minutes | 40 | This parameter defines the timeout in **minutes** after which requests to check if the Kyma environment is deleted should be stopped.
| `pollingIntervalForKymaDeprovisioningInMinutes` | int | minutes | 5 | This parameter defines the interval in **minutes** that requests are sent to check if the Kyma environment is available.

### Pruning - Handle with Care

After setting up everything you have the option to tear everything down again. One scenario might be to use the  `btp-setup-automator` as a tool to enable a integration or end2end scenario for your app, namely setting things up, checking if it works (via `executeAfterAccountSetup` commands) and then remove everything again.

You specify the behavior via two parameters:

| Parameter | Type | Default Value | Description
| --- | --- | --- | ---
| `pruneusecase`    | boolean | false | If this parameter is set to true the use case setup will be removed. The subaccount will **not** be deleted.
| `prunesubaccount` | boolean | false | If this parameter is set to true the subaccount setup will be removed. This also comprises the removal of the artifacts defined in the usecase. The usecase deletion wil be triggered implicitly independent of the `pruneusecase` parameter.  

> ⚠ NOTE: Be aware that all setups done via commands must be reversed. This must be done via commands provided in the `executeToPruneUseCase` section.  

### Parameter Examples

You find several examples for parameter files in the folder `integrationtests/parameterfiles`.

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

The technical data in this file depends on your services. To make things a bit more tangible, Let us take a look at two samples in the following sections to showcase the fundamentals.

### Sample 1 - Plain XSUAA Service

Let us assume that you want to provision an instance of the XSUAA service. For that we need to specify the service like this:

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
  "assignrolecollections": [
    {
      "name": "Global Account Administrator",
      "type": "account",
      "level": "global account",
      "assignedUserGroupsFromParameterFile": [
        "admins"
      ]
    },
    ....
  ]
}
```

You specify all the artifacts in the `services` section as a JSON array. For XSUAA we have an artifact of the `category` `SERVICE` and specify the relevant input for the creation like the name of the service aka "which service do you want to create" (`"name": "xsuaa"`), the plan that should be used (`"plan": "apiaccess"`) the name of the service instance (`"instancename": "xsuaa_api"`) and so on.

This example also shows the service specific definition of the parameters `repeatstatusrequest` and `repeatstatustimeout` mentioned above.

You also see a `assignrolecollections` attribute that assigns BTP role collections to usergroups that are defined in the `parameter file` (`assignedUserGroupsFromParameterFile`). The usergroups are defined in the parameter file attribute `myusergroups`. Check out the default [parameters.json](../parameters.json) file

### Sample 2 - Plain Kyma Provisioning

Let us assume that you want to provision a Kyma environment in your subaccount. For that we need to specify the service like this:

```json
{
  "aboutThisUseCase": {
    "name": "Setup a Kyma environment on your productive BTP account (GCP)",
    "description": "This usecase contains the necessary configuration to setup a Kyma environment in your SAP BTP account (GCP).",
    ...
 },
  "services": [
    {
      "category": "ENVIRONMENT",
      "name": "kymaruntime",
      "plan": "gcp",
      "amount": 1,
      "parameters": {
        "name": "btp-auto-setup",
        "region": "europe-west3",
        "autoScalerMin": 2,
        "autoScalerMax": 3,
        "machineType": "n2-standard-8"
      }
    }
  ]
}
```

As we create a environment the `category` is set to the value `ENVIRONMENT`. The `name` of the environment is `kymaruntime`. As for every scenario we need to specify the `plan`. In addition we need to provide a value for the `amount` of environments.

Besides this basic setup information we can also specify additional parameters like the `name` we want to give our instance, the `region` where it should be deployed or the `machineType` that should be used.

> 📝 Tip - In case you struggle with the available parameters and the possible values you can either check the SAP BTP cockpit UI (JSON view when creating a service) and the help.sap.com documentation of the service.

### Environment variables available for custom commands

btpsa will expose account metadata as environment variables to allow you to reference it when using `executeAfterAccountSetup`. The available variables are:

- `$GLOBAL_ACCOUNT_ID`: Global account UUID
- `$GLOBALACCOUNT`: Global account subdomain
- `$SUBACCOUNTID`: Subaccount ID
- `$SUBDOMAIN`: Subaccount subdomain
- `$SUBACCOUNT`: Subaccount name

If the usecase involves Kyma, `$KYMAKUBECONFIGURL` is also available (e.g.: `https://kyma-env-broker.cp.kyma.cloud.sap/kubeconfig/<UUID>`).

And for Cloud Foundry:

- `$CFAPIENDPOINT`: e.g.: `https://api.cf.us10-001.hana.ondemand.com`
- `$ORG`: Org name
- `$ORGID`: Org ID

The only environment variable available for `executeBeforeAccountSetup` is `$GLOBAL_ACCOUNT_ID`.

### Usecase Examples

You find several examples for parameter files in the folder `usecases/released`.

## Further Information

As the `btp-setup-automator` is leveraging the capabilities of the SAP btp CLI we recommend to have a look into the documentation of the CLI when it comes to the detailed parameters for single services. You find the information in [help.sap.com](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/7c6df2db6332419ea7a862191525377c.html).

You find a detailed overview and description of the parameters [here](PARAMETERS_OVERVIEW.md).

## What's next?

In case you want to learn more about the available parameters and the corresponding options of your SAP BTP setup via the btp-setup-automator, then this [page](PARAMETERS_OVERVIEW.md) got you covered.

In case you want to dive into the preconfigured use cases, then this [page](USECASES.md) is what you are looking for.
