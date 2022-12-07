# First Steps

## Configuration

As a developer you configure your use case inside a `usecase.json` file with all services and subscriptions that you need (find some sample [use cases here](./usecases/released) including [their detailed descriptions](./docs/USECASES.md)). The [JSON schema **btpsa-usecase.json**](./libs/btpsa-usecase.json) makes it fairly simple to create your own use case file as you can see in this video:

![json schema for creating use case files](docs/pics/btpsa-json-schema.gif)

You find more information on the sample use cases in the [use cases document](./docs/USECASES.md).

## Using the Setup Automator

You can run the container directly via the terminal or within VS Code, modify use case file and parameter file or supply externally available use case and parameter file.

[Read the detailed instructions](docs/README.md) on how to setup your SAP BTP account for a use case with the `btp-setup-automator`.

### With VS Code

If you want a more detailed walk-through guiding you through the first steps with the btp-setup-automator and VS Code, then this video on YouTube is worth a look:

[![Watch the intro video on the btp-setup-automator](https://img.youtube.com/vi/BHBgQ45fgIk/0.jpg)](https://www.youtube.com/watch?v=BHBgQ45fgIk)

### From a terminal

You can also attach to the running container and execute a shell in there:

```bash
docker exec -it btp-setup-automator bash
```

You'll be placed in a new Bash shell inside the container, with access to all the tools:

```text
; docker exec -it btp-setup-automator bash
bash-5.1$ ls
LICENSE  LICENSES  README.md  btpsa  config  docs  generator  libs  parameters.json  tests  usecases
bash-5.1$ btp
Welcome to the SAP BTP command line interface (client v2.24.0)

Usage: btp [OPTIONS] ACTION GROUP/OBJECT PARAMS

CLI server URL:                    not set
User:                              not set
Configuration:                     /home/user/.config/btp/config.json

You are currently not logged in.

Tips:
    To log in to a global account of SAP BTP, use 'btp login'. For help on login, use 'btp help login'.
    To display general help, use 'btp help'.

bash-5.1$
```
