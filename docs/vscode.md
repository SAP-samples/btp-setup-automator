# Using the Dockerfiles in MS Visual Studio Code (VSCode)

In case you are using MS VS Code, you can press the key combination command, shift, P and enter the command:

```text
Remote-Containers: Attach to Running Container
```

![command in VS Code to attach it to a running container](pics/quick-guide-step06.png)

Now you should see the running container. Click on it, and a new window will pop-up with the content of the docker container.

![select running container in VS Code](pics/quick-guide-step07.png)

You might have to select the right folder in the left hand navigtion of VS Code. Simply select the /home/user folder.

![open folder](pics/quick-guide-step08.png)

![select folder](pics/quick-guide-step09.png)

![open new terminal](pics/quick-guide-step10.png)

Now the last step is to simply run the script with the following command:

```bash
python run.py
```

The tooling will take the default use case **usecase.json** in the **usecase** folder to start with. But of course you can use other use case files or even create your own use case file.

## Available parameters

The python script allows you to use parameters to configure it to your needs and make it better usable within other scripts and/or ci-cd pipelines. Just run the following command to get a list of the available commands:

```bash
python run.py -h
```

To avoid lengthy commands you can assign all the parameters as well in the **parameters.json** file that can be found in the **usecases** folder.
Ideally, you'd directly add your email address and your global account subdomain to the **parameters.json** file.

![open new terminal](pics/quick-guide-step11.png)

## Using different use cases

The folder **usecases** has several sample use case configurations that you can use with the script. By using the parameter **-usecase** you can tell the script to use another file than the default use case **usecases/usecase.json**. Simply type the following command:



```bash
python run.py -usecase "usecases/usecase_cap-app-launchpad.json"
```

If you want you can as well use your own use case files that you can copy into the corresponding **usecases** folder BEFORE creating the docker image.
