# Running in the terminal

The main instructions in this repo are for using the Docker image based development containers within VS Code. If you want to use them simply in a command line context, these instructions are for you.

> In the procedure that follows, the directory into which this repo is to be cloned is `~/work/`, i.e. the `work/` directory within your user's home directory. Also, the procedure shows the use of the "cap-app-prod" development container, but this would work in a similar way for the other usecases too.

## Clone this repo and move into it

Clone this repo, and change directory into it:

```bash
git clone https://github.tools.sap/btp-dev-automation/main \
  && cd main
```

## Build the image

Now you're in the root of the repo (`~/work/main/`), build the image:

```bash
docker build \
  -t btp-script \
  -f containerdefinitions/btp-script/Dockerfile \
   .
```

This starts the build of the image, as follows:

* the image should be named "btp-script" (and tagged "latest" by default)
* the build instructions (the `Dockerfile`) is to be found in the `containerdefinitions/btp-script/` directory
* the build context (which is used, for example, to resolve [relative paths like these](https://github.tools.sap/btp-dev-automation/main/blob/27b25305ebc917ab4900fd41826af0419ffd6a61/dockerfiles/trial-deploy-cap-app/Dockerfile#L92-L93)) is the current directory (`.`)


## Run a container based on the image

Once the image has been built, you can run an instance of it (a container) like this, giving it the name "mytrialdevcontainer":

```bash
docker run \
  --publish 4004:4004 \
  --rm \
  --interactive \
  --tty \
  --name mytrialdevcontainer \
  btp-script
```

This starts a container based on the options given, as follows:

* where the port 4004 within the container is exposed on the Docker host (your machine) also as 4004
* the container should be immediately removed once you're done with it
* interactive, so you can type in it from your command line
* where a pseudo TTY (terminal) is attached to it
* the container should be named "mytrialdevcontainer"
* and the container is to be based on the `trial` image

> The `--interactive` and `--tty` are commonly contracted in `docker run` commands to be `-it`.

## Operate within the container

Once your container is started, you'll see a Bash prompt, and you'll be able to carry out the [tutorial steps](https://github.tools.sap/btp-dev-automation/main/tree/27b25305ebc917ab4900fd41826af0419ffd6a61/dockerfiles/trial-deploy-cap-app/resources) as described.

## Exit the container

Once you're done, you can exit the container (by exiting the Bash shell, via `exit` or `Ctrl-D`) and it will automatically be removed.
