# Frequently Asked Questions (FAQ)

This is a set of questions and answers relating to the btp-setup-automator.

If you have other questions you can [ask a question in SAP Community](https://answers.sap.com/questions/ask.html) or [raise an issue](https://github.com/SAP-samples/btp-setup-automator/issues/new) as a feature request.

## Generic Topics

### How does this relate to the Boosters on SAP BTP?

According to [the Boosters documentation](https://help.sap.com/products/BTP/65de2977205c403bbc107264b8eccf4b/fb1b56148f834749a2bf51127421610b.html), boosters "are a set of guided interactive steps that enable you to select, configure, and consume services on SAP BTP to achieve a specific technical goal".

So they do share a similar purpose to the `btp-setup-automator`, but there are some fundamental differences:

* First, while guided interactive steps have their place, so do processes that can be automated and executed in an unattended fashion. The `btp-setup-automator` is designed to be usable in such automated environments, in continuous integration / continuous delivery (CI/CD) pipelines, in platform-wide setup scripts, and beyond.

* Then, there's the open source nature. A deliberate side-effect of making the `btp-setup-automator` available in this project is to demonstrate how to use the various command line interface (CLI) tools that work with SAP BTP, because that's how the actual setup work is achieved. Moreover, we want you to be able to create your own automation mechanisms using the project contents, to be inspired by it and to configure those mechanisms as much or as little as you want.

* Finally, because it's open source, and you're in control, you don't have to request a new booster from SAP or wait for one to be created for you.

### Why containers?

Containers are a great way to encapsulate independent sets of tools and configuration. What's more, that encapsulation can be made available to everyone regardless of their underlying platform. One of the biggest challenges of managing platforms, running development operations (DevOps) processes, and interacting with environments, is the setup and configuration required to do so at an individual level.

A container based approach levels the field and allows you to start working immediately without having to work through a boot load of prerequisites to get the basic tools in place.

> 📝 Tip - For more on how containers enable a better developer experience, but from a slightly different angle, you may be interested in the 3-part blog post series [Boosting tutorial UX with dev containers](https://blogs.sap.com/2022/01/27/boosting-tutorial-ux-with-dev-containers-part-1-challenge-and-base-solution/).

### Why is the btp-setup-automator not written in NodeJS/Java/C/go/...?

The purpose of the `btp-setup-automator` is to show how you can automate the setup of an SAP BTP account. It's meant to be an inspiration for you to think of other ways to integrate SAP BTP into your development landscape or to simply use the tool as is.

Feel free to create your own/better version of `btp-setup-automator` in a programming language that you prefer, or contribute to this tool with a pull request.

### Can I connect the created account to an IAS by setting up the trust configuration?

Yes, you can. The file [setup_task_center.json](../usecases/released/setup_task_center.json) contains the setup of services for the SAP Task Center including establishing the trust with your custom IAS tenant.

### Where can I find a good UI to configure the tool?

The `btp-setup-automator` was started as a script to be integrated into CI/CD pipelines or other command-line setups. But of course you can create your own/better version of `btp-setup-automator` in a programming language that you prefer, or contribute to this tool with a pull request.

## Getting Started

### What do I need to get started?

See the [Requirements section of the main README](https://github.com/SAP-samples/btp-setup-automator#requirements) for details on what you need.

### How to login via SSO?

If you prefer you can set the parameter **loginmethod** to **sso** in the **parameters.json** file and the script will ask you to click on a URL when a login is needed (you have to open a browser with the link). This happens for logging-in via the SAP BPT CLI as well as for the Cloud Foundry CLI.

### Starting the `btpsa` script shows the error: `env: ‘python\r’: No such file or directory`

If you are using a windows machine there might be a default setup for the end of line sequence that is not compatible with Linux namely the `\r\n` as line breaks. To get rid of the error you have two options:

* Switch the end of line sequence setting in the VS Code window you opened via the shortcut the lower right corner of VS Code (you need to have the `btpsa`file open to see the option):

    ![select CLRF in VSCode footer](pics/faq01.png)

    This opens the command palette where you must choose `LF`

    ![select LF in command palette](pics/faq02.png)

* Set the end of line sequence fixed to `\n` via `File` - `Preferences`- `Settings` - `Files:EOL`

    ![change end of line in VSCode settings](pics/faq03.png)

### I've seen a new feature XYZ, but when running the container I don't see it. Why?

You might be using the container image that is in your computers' cache. Execute the following steps to delete the cache:

* Identify the container via:

  ```bash
  docker ps
  ```

* Stop the `btp-setup-automator` container using the container ID from the previous step:

  ```bash
  docker stop container_id
  ```

* Delete the image and run the following command to delete the cache:

  ```bash
  docker system prune -a -f
  ```

Now get the most current `btp-setup-automator` image (as stated in the `Download and Installation` section of the [main README.md](../README.md)) and start the container.

### How do I realize a DEV, TEST, PROD setup in my SAP BTP account with btp-setup-automator?

Just script the script :-). You can create 3 different parameter files, which only differ in the `subaccountname` parameter, like this:

`parameterDEV.json` file:

```bash
{
  "usecasefile": "usecases/released/cap_app_launchpad.json",
  "region": "us10",
  "globalaccount": "youraccount-ga",
  "myemail": "your.email@address.com",
  "loginmethod": "basicAuthentication",
  "subaccountname": "DEV",
}
```

`parameterTEST.json` file:

```bash
{
  "usecasefile": "usecases/released/cap_app_launchpad.json",
  "region": "us10",
  "globalaccount": "youraccount-ga",
  "myemail": "your.email@address.com",
  "loginmethod": "basicAuthentication",
  "subaccountname": "TEST",
}
```

`parameterPROD.json` file:

```bash
{
  "usecasefile": "usecases/released/cap_app_launchpad.json",
  "region": "us10",
  "globalaccount": "youraccount-ga",
  "myemail": "your.email@address.com",
  "loginmethod": "basicAuthentication",
  "subaccountname": "PROD",
}
```

### Where can I find more information about the available parameters?

You find all available parameters for the `btpsa` CLI tool in the file [`libs/btpsa-parameters.json`](../libs/btpsa-parameters.json). All parameters including their data types and default values are defined in there. The CLI is using this definition during runtime.

As an alternative you can also use the CLI directly and key in:

```bash
./btpsa -h
```

A detailed description of the parameters for the `parameters.json` is available here: [link](./generated/btpsa-parameters.md)
A detailed description of the parameters for the `usecase.json` is available here: [link](./generated/btpsa-usecase.md)

### I'm missing the tool XYZ in the container image. Can you please add it?

We want to keep the size of the docker image as small as possible and to contain the essential tool set within that image.

At the same time you can add any additional packages inside the `executeBeforeAccountSetup` section of your usecase file as we have installed the `sudo` Alpine package in the image. Just add something like this to your usecase file:

```json
..
  "executeBeforeAccountSetup": [
    {
      "description": "install the `uuidgen` and the `nano` package",
      "command": "sudo apk add uuidgen nano"
    }
  ]
..
```

### How can I subscribe to a deployed SaaS application?

SaaS applications are deployed in a global account and if registered available in all subaccounts. They have to be handled differently when creating an app subscription. You have to provide the following values in your btpsa files:

* In the `parameters.json` file you must provide a value for the `"customAppProviderSubaccountId"`. This subaccount must be a subaccount where the application is available e. g. the provider subaccount. This is needed to execute the validation of the use case file.
* In the `usecase.json` file when you specify the values for the `APPLICATION` that you want to subscribe to, make sure that you set the value of `"customerDeveloped"` to `true` as this will distinguish it from a regular application available on SAP BTP.

> 📝 Tip - When deploying the app to SAP BTP into the provider subaccount make sure that the value for the plan is available via the BTP CLI. You can check that via `btp --format json list accounts/subscription --subaccount <YOUR SUBACCOUNT ID>`.

## Docker Specifics

### Suddenly I'm getting an "docker: Error response from daemon: Head "../ghcr.io/v2/sap-samples/btp-setup-automator/manifests/main": denied: denied.". What's going on here?

One possibility: your docker login is trying to connect with GitHub via an expired GitHub token (that you have previously connected with docker). To fix this issue run this command in the command line:

```bash
docker logout ghcr.io
```

## Cloud Foundry Setup Specifics

> 🚧 No FAQ yet 🚧

## Kyma Setup Specifics

### I cannot execute `kubectl` commands after the Kyma runtime got provisioned. Is this a bug?

As the SAP BTP. Kyma runtime is using open-source Kyma the flow to access Kyma is based on an OIDC flow using the [kubelogin](https://github.com/int128/kubelogin) plugin to execute the flow. This flows need access to a browser and does not support the native execution from a Docker image (see ["Known Limitations"](https://github.com/int128/kubelogin/blob/237e53313d07a6eb90314c0880eb49605289afb1/docs/usage.md#run-in-docker) of the kubelogin plugin). The BTP setup automator cannot remove this limitation.

There are some workarounds that can help you to bypass the limitation:

* You can execute the BTP setup automator from within VS Code using the "Remote Containers: Attach to running container ..." functionality to access the running container via VS Code. This will enable the OIDC flow as the necessary opening of the browser can be executed by the plugin in this setup.
* Use a [service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) to access the Kyma cluster. This also means that you need to split the use case into two parts, part one that sets up the Kyma cluster and part two that executes the desired steps in the cluster. The flow looks like this
  
  1. Define and execute a use case to provision the Kyma cluster.
  2. Create the service account manually and store the `kubeconfig` of the service account in the container
  3. Define and execute a use case that contains the setup *in* the Kyma cluster using the service account to log on in a **non-interactive** way bypassing kubelogin.

* Execute the non-interactive authentication flow via a "technical" user in the IAS tenant. You must create your own tenant in IAS and define the necessary user, then use a custom OIDC provider when provisioning the Kyma clusters (assigning the user as admin) and and generate the tokens that you can insert in the `kubeconfig` and avoid kubelogin. OIDC provider besides IAS usually have a similar flow for these scenarios. This is probably the procedure with the biggest effort. It comes with the some downside as the scenario mentioned before as you must split your use case file into two parts.

### How can I create a service account?

To make your life easier we provided some scripts to make the creation and fetching of the Kubernetes configuration aka `kubeconfig` easier. You find the following files in the folder **config/kubernetes**:

* `service-account.yaml`: file containing the definition of the service account and the cluster role.
* `cluster-role-binding.yaml`: file containing the cluster role binding, connecting the service account with the corresponding cluster role
* `kubeconfig-sa-mac.sh`/`kubeconfig-sa-windows.ps1`: scripts to fetch the relevant data for the `kubeconfig.yaml`

Execute the following steps:

1. Create a namespace for the `ClusterRoleBinding`

2. Set the namespace as a variable:

    * MacOS

        ```shell
        export ns=<your_namespace>
        ```

    * Windows

        ```powershell
         $ns = "<your_namespace>"
        ```

3. Replace `<YOUR NAMESPACE>` with your value of the namespace in the file `cluster-role-binding.yaml`.

4. Apply the file `service-account.yaml` via `kubectl`:

    ```shell
    kubectl apply -f config/kubernetes/service-account.yaml -n $ns
    ```

5. Apply the file `cluster-role-binding.yaml` via `kubectl`:

    ```shell
    kubectl apply -f config/kubernetes/cluster-role-binding.yaml -n $ns
    ```

You can now download the `kubeconfig`file either via the Kyma dashboard or via the scripts provided in this repository:

* From the Kyma Dashboard:

  * Navigate to your namespace.
  * Access **Configurations** --> **Service Accounts**
  * Open the Service Account created by you in the previous step.
  * Download kubeconfig and store it
  
* Via the script 

  * If using Mac set the execute permission on the file `templates/kubeconfig-sa-mac.sh` and run it:
  
    ```shell
    chmod +x templates/kubeconfig-sa-mac.sh
    ./config/kubernetes/kubeconfig-sa-mac.sh
    ```

  * If using Windows set `Set-ExecutionPolicy Unrestricted` to change the execution policy if needed and run it:
  
    ```shell
    .\config\kubernetes\kubeconfig-sa-windows.ps1
    ```

> 📝 Tip - Do not execute the script multiple times. It will append the config data over and over, which will end up in an invalid config file.

You can then use this file to create services in the Kyma runtime via `kubectl` specifying the path using the paramter `"kubeconfigpath"` in your `parameters.json` file.

> 📝 Tip -  When you copy your configuration into the container, be aware that the btp-setup-automator will store the OIDC-based kubeconfig of Kyma as `.kube/config`. Make sure that you either copy your service account configuration at a different place or name it differently e.g. `config-sa`
