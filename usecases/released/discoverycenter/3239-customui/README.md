# Instructions for running SAP Discovery Center Mission in btp-setup-automator

The setup of this [mission](https://discovery-center.cloud.sap/protected/index.html#/missiondetail/3239/) can be executed by the [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator).

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) is an open source project to help developers setting-up their SAP BTP accounts quickly via various command line interfaces.

## Pre-Requisites

To use the [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) you first need to finish the following tasks:

- Get an [SAP BTP trial account](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial) or a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) (recommended) where you can make use of the free tier service plans
- [Install a Docker engine](https://docs.docker.com/desktop/)

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details see this [link](https://www.docker.com/blog/updating-product-subscriptions/).

## Instructions

Open a command line terminal on your machine.

> 📝 Tip - In case you don't know how to do it, here are the instructions for [MS Windows](https://www.wikihow.com/Open-Terminal-in-Windows), [Mac OS](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac) and [Ubuntu Linux](https://www.wikihow.com/Open-a-Terminal-Window-in-Ubuntu).

Enter the following command into the terminal and press the `ENTER` key:

```bash
docker container run --platform linux/amd64 --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:latest"
```

You'll notice that the prompt in your terminal has changed, because you are now working inside the docker container, that you just started.
Now run the main script `btpsa` with the following command:

```bash
./btpsa -parameterfile 'usecases/released/discoverycenter/3239-customui/parameters.json' \
    -globalaccount 'your_global_account_subdomain_as_shown_in_the_SAP_BTP_cockpit'  \
    -region        'region_for_your_subaccount_eg_us10' \
    -myemail       'your_email_address'
```

The tool starts to execute and the only thing you need to type-in is your password for your SAP BTP account. The btp-setup-automator script will now prepare your SAP BTP account to cover the discovery center mission.

> ⚠ NOTE: In case you don't have the rights to create your own sub account, you should add the sub account id as a parameter to the command. That should look like this:

```bash
./btpsa -parameterfile 'usecases/released/discoverycenter/3239-customui/parameters.json' \
    -globalaccount 'your_global_account_subdomain_as_shown_in_the_SAP_BTP_cockpit'  \
    -subaccountid  'your_sub_account_id_as_shown_in_the_SAP_BTP_cockpit'
    -region        'region_for_your_subaccount_eg_us10' \
    -myemail       'your_email_address'
```

If you want to understand other possible parameters, give the following command:

```bash
./btpsa --help
```

> Note: In case that the basic authentication fails due to some special character issues in your password, use the option 'SSO' as follows:

```bash
./btpsa -parameterfile 'usecases/other/discoverycenter/3774-taskcenter/parameters.json' \
    -globalaccount 'your_global_account_subdomain_as_shown_in_the_SAP_BTP_cockpit'  \
    -subaccountid  'your_sub_account_id_as_shown_in_the_SAP_BTP_cockpit'
    -region        'region_for_your_subaccount_eg_us10' \
    -myemail       'your_email_address' \
    -loginmethod   sso
```
