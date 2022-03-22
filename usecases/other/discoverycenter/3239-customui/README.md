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
./btpsa -parameterfile 'usecases/other/discoverycenter/3239-customui/parameters.json'
 \
    -globalaccount '<your global account subdomain as shown in the SAP BTP cockpit>'  \
    -region        '<region for your subaccount e.g. us10>' \
    -myemail       '<your email address>'
```

The tool starts to execute and the only thing you need to type-in is your password for your SAP BTP account. The btp-setup-automator script will now prepare your SAP BTP account to cover the discovery center mission.
