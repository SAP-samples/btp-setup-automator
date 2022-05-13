# Parameters that can be used when calling btp-setup-automator

When calling the '`btp-setup-automator` you can provide additional parameters to the command line of add the parameters in the `parameters.json` file.

These are the available commands:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
| myemail | email address used for your SAP BTP account | str |  | None |
| globalaccount | your SAP BTP global account | str |  | None |
| loginmethod | if set to sso, you'll need to open a link provided in a browser to login. Set to basicAuthentication (default) the script will ask if you want to provide username and password. If set to **envVariables** you need to provide the email address and password by setting the environment variable **BTPSA_PARAM_MYEMAIL** and **BTPSA_PARAM_MYPASSWORD**. In addition you can as well provide the global account through the environment variable **BTPSA_PARAM_GLOBALACCOUNT**. | str |  | basicAuthentication |
| region | region of the subaccount for use case | str |  | us10 |
| subaccountid | subaccount id for use case | str |  | None |
| subaccountname | subaccount name for use case | str |  | None |
| subdomain | subdomain of subaccount | str |  | None |
| org | org name of the CF environment for use case | str |  | None |
| orgid | org id of the CF environment for use case | str |  | None |
| cfspacename | name for the Cloudfoundry space  | str |  | development |
| iashost | IAS host for your SAP BTP sub account | str |  | None |
| suffixinstancename | suffix attached to each service instance created | str |  | None |
| fallbackserviceplan | if defined, the tool will use the defined name as fallback service plan, if the plan defined in the use case is not supported | str |  | None |
| repeatstatusrequest | time in seconds to wait after requesting status info (pulling) | int |  | 4 |
| repeatstatustimeout | timeout in seconds after which requests should be stopped | int |  | 4200 |
| waitForKymaEnvironmentCreation | Should the tool wait for the creation of the Kyma environment | bool |  | True |
| timeoutLimitForKymaCreationInMinutes | Limit in minutes until the tool should wait for the Kyma instance to be created | int |  | 40 |
| pollingIntervalForKymaCreationInMinutes | Polling interval in minutes when tool is waiting for the Kyma instance to be created | int |  | 5 |
| timeoutLimitForKymaDeprovisioningInMinutes | Limit in minutes until the tool should wait for the Kyma instance to be deprovisioned/deleted | int |  | 40 |
| pollingIntervalForKymaDeprovisioningInMinutes | Polling interval in minutes when tool is waiting for the Kyma instance to be deprovisioned/deleted | int |  | 5 |
| usecasefile | file with usecase config | str |  | None |
| parameterfile | file to deliver all parameters within a single json file | str |  | parameters.json |
| logfile | file for log information | str |  | log/script.log |
| metadatafile | file for log information | str |  | log/metadata_log.json |
| logcommands | if set to True, the script will log all commands sent to the SAP BTP account. If set to False it won't | bool |  | True |
| pruneusecase | if set to True: deletes all assets of a usecase based on the collected info in the metadatafile. No confirmation message. USE WITH CARE!!! | bool |  | False |
| prunesubaccount | if set to True: same like -pruneusecase, but on-top deletes the subaccount. USE WITH CARE!!! | bool |  | False |
| mypassword | provide your BTP password via the command line. USE WITH CARE!!! | str |  | None |
| cfcliapihostregion | host region for the Cloud Foundry CLI calls | str |  | None |
| btpcliapihostregion | host region for the BTP CLI calls | str |  | eu10 |
| envvariables | list of environment variables on OS level to be used within commands defined in the `executeBeforeAccountSetup` and `executeAfterAccountSetup`. | str |  | None |
| myusergroups | list of user groups to be used in btpsa | str |  | None |

You can get an overview of those commands as well, by simply typing the following command in your command line terminal:

```bash
./btpsa -h
```