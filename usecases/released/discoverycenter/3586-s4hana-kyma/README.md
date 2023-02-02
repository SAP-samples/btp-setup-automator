# Instructions for running SAP Discovery Center Mission in btp-setup-automator

The setup of this [mission](https://discovery-center.cloud.sap/protected/index.html#/missiondetail/3586/) can be executed by the [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator).

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) is an open source project to help developers setting-up their SAP BTP accounts quickly via various command line interfaces.
The current script was designed to setup the account and create subscriptions used by the mission, [SAP S/4HANA Extend Business Process Scenario in SAP BTP, Kyma Runtime](https://discovery-center.cloud.sap/missiondetail/3586/).

The script will create a subaccount with the necessary entitlements and also creates the necessary subscriptions used by the SAP S/4HANA Extend Business Process Scenario in SAP BTP, Kyma Runtime. The following service entitlements and subscriptions are created:

* Subaccount s4hanakyma
* Kyma Runtime
* SAP HANA Cloud Tools Subscriptions
* SAP Launchpad Service Subscription
* SAP HANA Schemas and DI Containers
* SAP HAAN Cloud
* Event Mesh
* Connectivity Service

## Pre-Requisites

To use the tooling you first need to finish the following tasks:

* Get a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) where you can make use of the free tier service plans.
* [Install a Docker engine](https://docs.docker.com/desktop/)

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details see this [link](https://www.docker.com/blog/updating-product-subscriptions/).

## Changes the configuration

Currently the use case requires a productive SAP BTP account. Also the name and the name of the subaccount is preconfigured to "s4hanakyma" and US10 as region. In case you need to adapt some of the parameters you can parse them via commandline parameters when you call the script, for example to change the region it would look like this:

```bash
./btpsa -parameterfile 'usecases/released/discoverycenter/3586-s4hana-kyma/parameters.json' -globalaccount '<your global account subdomain as shown in the SAP BTP cockpit>' -myemail '<your email address>' -region 'region for your subaccount'
```

If you want to make changes to the actual [usecase.json](usecase.json) you can either attach Visual Studio Code directly to your running container. Then you can perform the changes (it works as well with the parameters.json) and run the script as described above. You should be aware that the changes are not persisted if you terminate the docker container. In case you need to perform permanent changes to either the usecase.json or the parameter json you need to create your own docker image containing the changes as described [in the documentation](../../../../README.md#option-2-start-docker-container-with-self-built-image) for more details.

**Region Change**

Be aware in case you change the region for the use case you need to have a look at the [Available Regions here](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/557ec3adc3174ed4914ec9d6d13487cf.html?locale=en-US&version=Cloud). In order to make sure the the use case is executable you need to check if the [SAP BTP Kyma Runtime availability](https://discovery-center.cloud.sap/serviceCatalog/kyma-runtime?region=all&tab=service_plan) and the [SAP HANA Cloud availability](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-cloud?region=all&tab=service_plan) is given.

## Instructions

Open a command line terminal on your machine.

> 📝 Tip - In case you don't know how to do it, here are the instructions for [MS Windows](https://www.wikihow.com/Open-Terminal-in-Windows), [Mac OS](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac) and [Ubuntu Linux](https://www.wikihow.com/Open-a-Terminal-Window-in-Ubuntu).

Enter the following command into the terminal and press the `ENTER` key:

```bash
docker container run --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:latest"
```

> ⚠ NOTE: If you are running on an ARM based platform like a Mac M1 or M2 and are facing issues with the image, add the `--platform linux/amd64` option to the `docker container run command`. The image we provide is built for `linux/amd64` and due to some implicit dependencies we cannot perform a built for `linux/arm64` with the alpine linux as base image.

You'll notice that the prompt in your terminal has changed, because you are now working inside the docker container, that you just started.
Now run the main script `btpsa` with the following command:

```bash
./btpsa -parameterfile 'usecases/released/discoverycenter/3586-s4hana-kyma/parameters.json' -globalaccount '<your global account subdomain as shown in the SAP BTP cockpit>' -myemail '<your email address>'
```

The btp-setup-automator script will now prepare your SAP BTP account to cover the discovery center mission. You can have a look at the [usecase.json](usecase.json) and [parameters.json](parameters.json) for more details about the used services and configuration parameters (e.g. DB Password for SAP HANA Cloud)
