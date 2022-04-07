# Instructions for running SAP Discovery Center Mission in btp-setup-automator

## Pre-Requisites

To use the tooling you first need to finish the following tasks:

- Get an [SAP BTP trial account](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial) or a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) (recommended) where you can make use of the free tier service plans
- [Install a Docker engine](https://docs.docker.com/desktop/)

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details see this [link](https://www.docker.com/blog/updating-product-subscriptions/).

## Instructions

Open a command line terminal on your machine.

> 📝 Tip - In case you don't know how to do it, here are the instructions for [MS Windows](https://www.wikihow.com/Open-Terminal-in-Windows), [Mac OS](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac) and [Ubuntu Linux](https://www.wikihow.com/Open-a-Terminal-Window-in-Ubuntu).

Enter the following command into the terminal and press the `ENTER` key:

```bash
docker container run --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:main"
```

You'll notice that the prompt in your terminal has changed, because you are now working inside the docker container, that you just started.
Now run the main script `btpsa` with the following command:

```bash
./btpsa -parameterfile 'usecases/other/discoverycenter/3638-kyma-multitenant/parameters.json' \
    -globalaccount '<your global account subdomain as shown in the SAP BTP cockpit>'  \
    -region        '<region for your subaccount e.g. us10>' \
    -myemail       '<your email address>'
```
The btp-setup-automator script will now prepare your SAP BTP account to cover the discovery center mission. You can have a look at the [usecase.json](usecase.json) and [parameters.json](parameters.json) for more details about the used services and configuration parameters (e.g. DB Password for SAP HANA Cloud)

## Changes the configuration

Currently the usecase is designed to use the free tier service plans and requieres a a productive SAP BTP account. Also the name and the name of the subaccount is preconfigured to "EasyFranchise" and US10 as region. In order to change the name of the subaccount or the region you need to adapt the [parameters.json](parameters.json). The easiest way to change either the [usecase.json](usecase.json) or the [parameters.json](parameters.json) is to attach Visual Studio Code directly to your running container. You can have a look at the [Setup Automator for SAP Business Technology Platform documentation](../../../../README.md#option-2-start-docker-container-with-self-built-image) for more details.

### Changing the region

In case you want to change the region for the usecase you can have a look at the [Available Regions here](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/557ec3adc3174ed4914ec9d6d13487cf.html?locale=en-US&version=Cloud). In order to make sure the the usecase is executeable you need to check if the [SAP BTP Kyma Runtime availability](https://discovery-center.cloud.sap/serviceCatalog/kyma-runtime?region=all&tab=service_plan) and the [SAP HANA Cloud availability](https://discovery-center.cloud.sap/serviceCatalog/sap-hana-cloud?region=all&tab=service_plan) is given. 