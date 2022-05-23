# Setup Automator for SAP Business Technology Platform

[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/btp-setup-automator)](https://api.reuse.software/info/github.com/SAP-samples/btp-setup-automator) [![Build and Push Docker Image](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-build-and-push.yml/badge.svg)](https://github.com/SAP-samples/btp-setup-automator/actions/workflows/docker-build-and-push.yml)

## Description

This repository provides the user with a script to **automate the setup** of an [SAP Business Technology Platform (SAP BTP) account](https://account.hana.ondemand.com/) and to **learn** how this is done with the various command line interfaces and tools.

![architectural overview](docs/pics/overview.png)

This includes:

- Setup of your SAP BTP account
- Entitlement of services
- Subscription of applications and creation of service instances with api keys
- Addition of administrator users to global account and subaccounts
- Setup of roles and role collections, assignment of roles collections to users
- Deployment of complete applications
- Unrolling created setup

In essence it’s all about **making it easier to get developers quickly onboard on SAP BTP** and use services on SAP BTP without having to know too much of the terminology and how to use the SAP BTP Cockpit.

### All in containers

The tooling provided in this repository is supposed to run inside a [docker](https://www.docker.com/) container.

[Why docker](https://www.docker.com/why-docker)? We want to ensure that you can focus on getting your work done on the SAP BTP account without having to worry whether you have the right tools in the right release for the right operating system in place.

### The Use Cases

As a user the only thing you need to focus on is your use case that defines which services or subscriptions you need. The use case is defined within a JSON structure. You can find [use cases in the use cases folder of this repository](usecases/), and - of course - you can create your own use case files, if you want to run the script.

With the built-in json schemas it's fairly simple to create your own use case file as you can see in this video:

![json schema for creating use case files](docs/pics/btpsa-json-schema.gif)

You find more information on the different use cases in the [usecases document](./docs/USECASES.md).


## Requirements

To use the tooling you first need to finish the following tasks:

- Get an [SAP BTP trial account](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial) or a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) (recommended) where you can make use of the free tier service plans
- [Install a Docker engine](https://docs.docker.com/desktop/)

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details see this [link](https://www.docker.com/blog/updating-product-subscriptions/).

In case you are new to the containers topic, it is **highly recommended** to install and setup **MS Visual Studio Code**, too:

- [Install VS Code](https://code.visualstudio.com/download) - this will be your development environment.
- Install the VS Code plugin for [Remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

## Download and Installation

If the pre-requisites above are all met, you can start your work by creating first your container. You can either use the pre-built docker image for the `btp-setup-automator`, or build the docker image yourself.

For starting quickly **it is recommended to use the pre-built Docker image**.

### Option 1: Start Docker Container via Pre-Built Image (recommended)

The fastest way to use the `btp-setup-automator` it, to open a terminal windows on your machine and to enter the following command to pull the docker image from the GitHub repository and run it in a container:

```bash
docker container run --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:main"
```

You'll notice that the prompt in your terminal has changed, because you are now working inside the docker container, that you just started.

You can now run the main script `btpsa` with the following command and you'll be deploying a CAP application on your SAP BTP Trial account (the default [usecase](docs/USECASES.md)):

```bash
./btpsa
```

The tool starts to execute and the only thing you need to type-in is your password for your SAP BTP account.

> 📝 Tip - If you are already using VS Code, you should execute this command instead, so that the container runs "detached" (`-d`) from your command line session:
>
> ```bash
> docker container run --rm -it -d --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:main"
> ```

You can also use the provided `run` files to pull the image from the registry and start the container via one command. To do so execute the following command:

- bash (macOS/Linux)

  ```bash
  ./run RunFromRegistry
  ```

- Command Prompt (Windows):

  ```cmd
  .\run.bat RunFromRegistry
  ```

- PowerShell Core (Cross Platform):

  ```powershell
  .\run.ps1 -RunFromRegistry $True 
  ```

### Option 2: Start Docker Container With Self-Built Image

To create the Docker image yourself you need to execute these steps:

- Clone this GitHub repository to a local folder on your machine.
- Open the local folder in a command terminal on your machine (or in VS Code).
- Build the container with the following command:

  - bash (macOS/Linux)

    ```bash
    ./run
    ```

  - Command Prompt (Windows):

    ```cmd
    .\run.bat
    ```

  - PowerShell Core (Cross Platform):

    ```powershell
    .\run.ps1
    ```

The script  will build a docker image and create a docker container on your machine.

### Option 3: Using the prebuilt Docker image on the command line as one-off

If you're not requiring any changes to the Dockerimage itself and would like to run the tool directly with your local ´usecase.json´ and ´parameters.json´ this is the easiest option. It requires a a shell and docker only and no VSCode Remote Containers or files in the container itself

Pull the image
```bash
docker pull ghcr.io/sap-samples/btp-setup-automator:main
```


Create a alias (mounting the current working directory inside the container)
```bash
alias docker_btpsa='docker container run --rm  -it -v "$PWD:/home/user/data" "btpsa" --entrypoint "/home/user/btpsa"'
```

Execute it with (note - files must be prefixed with ´/data´ from the container POV)
```bash
docker_btpsa -parameterfile data/parameters.json -usecasefile data/usecase.json
```
## Using the Docker Container

Independently whether you've created the docker image yourself, or used the pre-built image, you should now see the Docker container up-and-running. In case you are using VS Code, open the command palette (Windows: `Ctrl+Shift+P` ; Mac: `Cmd+Shift+P`) and select the `Remote Containers: Attach to running Container ...` command:

![command in VS Code to attach it to a running container](docs/pics/quick-guide-step00.png)

> 📝 Tip - Don't forget to install the "Remote-Containers" extension in VS Code)

The select the `btp-setup-automator` container:

![select running container in VS Code](docs/pics/quick-guide-step01.png)

## Using BTP-SETUP-AUTOMATOR

You can run the container directly via the terminal or within VS Code, modify use case file and parameter file or supply externally available use case and parameter file.
  
[Read the detailed instructions](docs/README.md) on how to setup your SAP BTP account for a use case with the `btp-setup-automator`.

## Sample Use-Cases

You find several sample Use cases in the folder [./usecases/released](./usecases/released). They are described in the [USECASES.md](./docs/USECASES.md) file.

## Known Issues

Checkout [the issues section in this repo](https://github.com/SAP-samples/btp-setup-automator/issues) for known and current issues.

## How to obtain Support?

❓ - If you have *question* you may peruse the [Frequently Asked Questions](docs/FAQ.md) document. If you did not find your questions answered there you can [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

🐛 - If you find a bug, feel free to [create an bug report](https://github.com/SAP-samples/btp-setup-automator/issues/new?assignees=&labels=bug&template=bug-report.yml&title=%5BBUG%5D+%3Ctitle%3E).

🚀 - If you have an idea for improvement or a feature request, please open [feature-request](https://github.com/SAP-samples/btp-setup-automator/issues/new?assignees=&labels=enhancement&template=feature-request.yml&title=%5BFEATURE+REQUEST%5D+%3Ctitle%3E).

## Contributions

Checkout the [CONTRIBUTING.md file](CONTRIBUTING.md) for more details on how to contribute to this open source project.

## Code of conduct

Checkout the [CODE_OF_CONDUCT.md file](CODE_OF_CONDUCT.md) for more details on the code of conduct for this open source project.

## License

Copyright (c) 2022 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
