# Instructions for running SAP Discovery Center Mission in btp-setup-automator

## Pre-Requisites

To use the tooling you first need to finish the following tasks:

- Get an [SAP BTP trial account](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial) or a [productive SAP BTP account](https://account.hana.ondemand.com/#/home/welcome) (recommended) where you can make use of the free tier service plans
- [Install a Docker engine](https://docs.docker.com/desktop/)
- [Install VS Code](https://code.visualstudio.com/download) - this will be your development environment.
- Install the VS Code plugin for [Remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

> ⚠ NOTE: Be aware of the terms of Docker for usage in enterprises. For details see this [link](https://www.docker.com/blog/updating-product-subscriptions/).

## Instructions

Open VS Code and open a terminal via the menu `Terminal > New terminal`. 

Enter the following command into the terminal and press the `ENTER` key:

```bash
docker container run --rm  -it -d --name "btp-setup-automator" "ghcr.io/sap-samples/btp-setup-automator:main"
```

Now open the Command Palette (in the menu "View" select "Command Palette") or press the key combination `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac). Then enter the command:

```text
Remote-Containers: Attach to Running Container
```

![command in VS Code to attach it to a running container](../../../../docs/pics/quick-guide-step00.png)

Now you should see the running container. Click on it, and a new window will pop-up with the content of the Docker container.

![select running container in VS Code](../../../../docs/pics/quick-guide-step01.png)

You might have to select folder with the content in navigation panel of VS Code via `Open Folder`:

![open folder](../../../../docs/pics/quick-guide-step02.png)

Select the `/home/user` folder:

![select folder](../../../../docs/pics/quick-guide-step03.png)

You can also open a new terminal in the container via the menu `Terminal` - `New Terminal`. This will open an `ash` shell.

![open new terminal](../../../../docs/pics/quick-guide-step04.png)

The last step is to run the main script `btpsa` with the following command:

```bash
./btpsa -parameterfile 'usecases/other/discoverycenter/3774-taskcenter/parameters.json' \
    -globalaccount '<your global account subdomain as shown in the SAP BTP cockpit>'  \
    -region        '<region for your subaccount e.g. us10>' \
    -myemail       '<your email address>'
```

The tool starts to execute and the only thing you need to type-in is your password for your SAP BTP account.
