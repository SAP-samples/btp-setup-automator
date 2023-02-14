# Basic setup

## Pre-requisites

To use the btp-setup-automator, this is what you need to do first:

- Get an [SAP BTP trial account](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial), or a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) (recommended) where you can make use of the free tier service plans
- [Install a Docker engine](https://docs.docker.com/desktop/)

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details read [Docker is Updating and Extending Our Product Descriptions](https://www.docker.com/blog/updating-product-subscriptions/).

In case you are new to the containers topic, we **strongly recommend** that you install and setup **MS Visual Studio Code** (VS Code), too:

- [Install VS Code](https://code.visualstudio.com/download) - this will be your development environment.
- Install the VS Code [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for connecting to and using Docker containers.

## Download and Run

Once the pre-requisites above are all met, you can either use one of the pre-built Docker images for the `btp-setup-automator`, or build it yourself.

### Option 1: Start the btpsa via Dev Container (recommended)

We provide two configurations for Dev Containers to start the `btp-setup-automator` based on the two pre-built images we serve on GitHub:

- The **release**/**stable** image: This is a *stable* version of the `btp-setup-automator` and corresponds to the latest release visible on the [release section](https://github.com/SAP-samples/btp-setup-automator/releases) of the repository. The corresponding code is taken from the [`main branch`](https://github.com/SAP-samples/btp-setup-automator/tree/main) of the repository.
- The **dev** image: This is an up-to-date version of the `btp-setup-automator`. It usually contains newer features and fixes but was not yet officially released. The corresponding code is taken from the [`dev branch`](https://github.com/SAP-samples/btp-setup-automator/tree/dev) of the repository.

To start a Dev Container in VS Code the easiest way is to click on the "Open a remote Window" button in the footer of VS Code:

![open in remote window](pics/open-in-remote-window.png)

This opens the command palette. Select `Reopen in Container` in the Dev Container section:

![reopen in container](pics/command-palette-devcontainer.png)

Select the configuration you want to use (*stable* or *dev*):

![devcontainer config options](pics/devcontainer-config-options.png)

VS Code will reopen in the Dev Container and you can start using the  `btp-setup-automator`.

> 📝 Tip - You can also use the VS Code command palette (in the menu "View" select "Command Palette" or press the key combination `Ctrl+Shift+P` for Windows or `Cmd+Shift+P` for Mac) and use the "Dev Container: Reopen in Container" option from there.

#### Alternative GitHub Codespaces

Defining Dev Container configurations opens up the option to use [GitHub Codespaces](https://docs.github.com/en/codespaces) as you execution environment for the `btp-setup-automator`.

To open the btpsa in GitHub Codespaces use the badges provided on the [main page](https://github.com/SAP-samples/btp-setup-automator) of the repository.

> ⚠ NOTE: Cost might occur on your personal or organizational account when using GitHub Codespaces. You find more information on that topic [here](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces).

In case you are using SSO as login option when execution use cases, be aware that there might be issues when it comes to [forwarded ports](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-visibility-of-forwarded-ports) depending on your organizational settings.

### Option 2: Start Docker Container with Pre-Built Images via scripts

As an alternative to Dev Containers you can also directly spin up the `btpsa` container via Docker CLI or via `run` scripts that we provide. This sections guides you through this setup.

To leverage the Docker CLI, open a terminal window on your machine and run the following command to pull the Docker image from the GitHub repository and start a container based upon it.

- For the **release** image:

    ```bash
    docker container run --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:latest"
    ```

- For the **dev** image:

    ```bash
    docker container run --rm -it --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator-dev:dev"
    ```

> ⚠ NOTE: If you are running on an ARM based platform like a Mac M1 or M2 and are facing issues with the image, add the `--platform linux/amd64` option to the `docker container run command`. The image we provide is built for `linux/amd64` and due to some implicit dependencies we cannot perform a built for `linux/arm64` with the alpine linux as base image.

Here is a brief explanation of the options used:

- `--rm` causes the container to be automatically cleaned up (removed) when you're done with it (when it stops)
- `-it` is short for `-i` `-t` and together make the container accessible and interactive (for you to work within)
- `--name` specifies a name for the container (rather than have Docker generate a random one)

> You may need to authenticate with GitHub's container registry at `ghcr.io` (you'll know you need to do this if you get a "denied" error when you run the above command). If this is the case, you'll need to [create a Personal Access Token (PAT)](https://github.com/settings/tokens) with the `read:packages` scope, and then run this command to log in, using the PAT as the password, when prompted:
>
> ```bash
> docker login ghcr.io --username <your GitHub username>
> ```

You'll notice that the prompt in your terminal has changed, because you are now working inside the Docker container that you just started.

You can now run the main script `btpsa` with the following command and you'll be deploying a CAP application on your SAP BTP Trial account (the [default use case](../usecases/released/default.json)).

```bash
./btpsa
```

The tool starts to execute and the only thing you need to type in is your password for your SAP BTP account.

> 📝 Tip - If you are already using VS Code, you should execute this command instead, so that the container runs "detached" (`-d`) from your command line session. Here teh command when using the release image
>
> ```bash
> docker container run --rm -it -d --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:latest"
> ```

You can also use the provided `run` files to pull the image from the registry and start the container via one command. To do so execute the following command (clone this repo to make the commands available to you):

- bash (macOS/Linux)
  - **release** image:

      ```bash
      ./run RunReleaseFromRegistry
      ```

  - **dev** image:

      ```bash
      ./run RunDevFromRegistry
      ```

- Command Prompt (Windows):

  - **release** image:

      ```cmd
      .\run.bat RunReleaseFromRegistry
      ```

  - **dev** image:

      ```cmd
      .\run.bat RunDevFromRegistry
      ```

- PowerShell Core (Cross Platform):
  - **release** image:

      ```powershell
      .\run.ps1 -RunReleaseFromRegistry $True
      ```

  - **dev** image:

      ```powershell
      .\run.ps1 -RunDevFromRegistry $True
      ```

### Option 3: Start Docker Container With Self-Built Image

To create the Docker image yourself you need to execute these steps:

- Clone this GitHub repository to a local folder on your machine.

  > 📝 Tip If you are on Windows you you get an error when cloning the repository stating `Filename too long`, you need to adjust your git settings: `git config --system core.longpaths true`

- Open the local folder in a terminal window on your machine (or in VS Code).
- Build the image with the following command:

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

The script will build a Docker image and create a running container from it, on your machine.

## Get the Docker Container up-and-running

Regardless of which option you chose, you should now see the Docker container up and running. In case you are using VS Code, open the command palette (Windows: `Ctrl+Shift+P` ; Mac: `Cmd+Shift+P`) and select the `Remote Containers: Attach to Running Container...` command:

![command in VS Code to attach it to a running container](./pics/quick-guide-step00.png)

> 📝 Tip - Don't forget to install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in VS Code

Then look for the container by name (`btp-setup-automator`) and selecting it:

![select running container in VS Code](./pics/quick-guide-step01.png)

> You may see a message in VS Code informing you about the installation of some VS Code mechanisms into the container (to support the attachment to the remote container) and may have to wait a minute or two for this to complete.

## What's next?

You have now successfully setup your environment and are good to go and start with executing a sample setup of an SAP BTP account. Now let us get an overview what we can do [here](OVERVIEW.md).
