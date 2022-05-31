# Parameters that can be used when calling btp-setup-automator

When calling the '`btp-setup-automator` you can provide additional parameters to the command line of add the parameters in the `parameters.json` file.

If you use VS Code or any other IDE that supports JSON schemas, you can just add the following key/value pair to your parameters file to get auto-fill help, when creating it:

````json
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
````

These are the available parameters:

| Parameter | Description | Type  | Default value |
|---|---|---|---|
| $schema |  | string |  |
| myemail | Email address you use to access your SAP BTP account | ['string', 'null'] | None |
| globalaccount | the 'subdomain id' of your SAP BTP global account (please check it in the SAP BTP cockpit) | ['string', 'null'] | None |
| loginmethod | if set to sso, you'll need to open a link provided in a browser to login. Set to basicAuthentication (default) the script will ask if you want to provide username and password. If set to **envVariables** you need to provide the email address and password by setting the environment variable **BTPSA_PARAM_MYEMAIL** and **BTPSA_PARAM_MYPASSWORD**. In addition you can as well provide the global account through the environment variable **BTPSA_PARAM_GLOBALACCOUNT**. Like this: export BTPSA_PARAM_MYEMAIL=youremail@x.com | string | basicAuthentication |
| region | region for the SAP BTP sub account that should be used for the use case | string | us10 |
| clusterregion | region for the SAP BTP Kyma runtime cluster. This parameter is used as default for Kyma cluster creation. Override via usecase.json possible | string |  |
| subaccountid | id of your sub account that should be used | string | None |
| subaccountname | name of your sub account in case you want to define a specific name for your sub account | ['string', 'null'] | None |
| subdomain | name of the subdomain of your sub account | ['string', 'null'] | None |
| org | org name of the Cloudfroundy environment to be used for your use case | ['string', 'null'] | None |
| orgid | org id of the Cloudfoundry environment to be used for your use case | ['string', 'null'] | None |
| cfspacename | name for the Cloudfoundry space to be used for your use case | ['string', 'null'] | development |
| iashost | IAS host for your SAP BTP sub account in case you want to make use of it in your use case (create a service instance for service 'xsuaa' and plan 'apiaccess') | ['string', 'null'] | None |
| suffixinstancename | suffix attached to each service instance that is created (e.g. hana_yoursuffixinstancename) | ['string', 'null'] | None |
| fallbackserviceplan | if defined, the tool will use the defined name as fallback service plan, if the plan defined in the use case is not supported | ['string', 'null'] | None |
| repeatstatusrequest | time in seconds to wait after requesting status info (pulling) | integer | 4 |
| repeatstatustimeout | timeout in seconds after which requests should be stopped | integer | 4200 |
| waitForKymaEnvironmentCreation | Should the tool wait for the creation of the Kyma environment | boolean | True |
| timeoutLimitForKymaCreationInMinutes | Limit in minutes until the tool should wait for the Kyma instance to be created | integer | 40 |
| pollingIntervalForKymaCreationInMinutes | Polling interval in minutes when tool is waiting for the Kyma instance to be created | integer | 5 |
| timeoutLimitForKymaDeprovisioningInMinutes | Limit in minutes until the tool should wait for the Kyma instance to be deprovisioned/deleted | integer | 40 |
| pollingIntervalForKymaDeprovisioningInMinutes | Polling interval in minutes when tool is waiting for the Kyma instance to be deprovisioned/deleted | integer | 5 |
| usecasefile | file with usecase config | string | None |
| parameterfile | file to deliver all parameters within a single json file | string | parameters.json |
| logfile | file including all logged information | string | log/script.log |
| metadatafile | file for log information | string | log/metadata_log.json |
| logcommands | if set to True, the script will log all commands sent to the SAP BTP account. If set to False it won't | boolean | True |
| pruneusecase | if set to True: deletes all assets of a usecase based on the collected info in the metadatafile. No confirmation message. USE WITH CARE!!! | boolean | False |
| prunesubaccount | if set to True: same like -pruneusecase, but on-top deletes the subaccount. USE WITH CARE!!! | boolean | False |
| mypassword | password for the user of your SAP BTP account (USE WITH CARE!) | string | None |
| cfcliapihostregion | host region for the Cloud Foundry CLI calls | ['string', 'null'] | None |
| btpcliapihostregion | host region for the BTP CLI calls | ['string', 'null'] | eu10 |
| envvariables | list of environment variables on OS level to be used within commands defined in the `executeBeforeAccountSetup` and `executeAfterAccountSetup`. | object | None |
| myusergroups | list of user groups to be used in btpsa | array | None |
| maintain_jsonschemas | if set to true, the json schema files for parameters and usecases will be updated | boolean | False |
| maintain_documentation | if set to true, the the automatically created documentation of btpsa will by updated | boolean | False |

You can get an overview of those commands as well, by simply typing the following command in your command line terminal:

```bash
./btpsa -h
```