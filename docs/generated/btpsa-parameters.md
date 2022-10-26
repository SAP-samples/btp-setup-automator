## JSON Schema for service parameters used in BTPSA Type

`object` ([JSON Schema for service parameters used in BTPSA](btpsa-parameters.md))

all of

*   [Untitled undefined type in JSON Schema for service parameters used in BTPSA](btpsa-parameters-allof-0.md "check type definition")

*   [Untitled undefined type in JSON Schema for service parameters used in BTPSA](btpsa-parameters-allof-1.md "check type definition")

*   [Untitled undefined type in JSON Schema for service parameters used in BTPSA](btpsa-parameters-allof-2.md "check type definition")

# JSON Schema for service parameters used in BTPSA Properties

| Property                                                                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                         |
| :---------------------------------------------------------------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [$schema](#schema)                                                                              | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-schema.md "undefined#/properties/$schema")                                                                                                                                          |
| [btpcliapihostregion](#btpcliapihostregion)                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-host-region-for-the-btp-cli-calls.md "undefined#/properties/btpcliapihostregion")                                                                                                   |
| [cfcliapihostregion](#cfcliapihostregion)                                                       | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-host-region-for-the-cloud-foundry-cli-calls.md "undefined#/properties/cfcliapihostregion")                                                                                          |
| [cfLandscape](#cflandscape)                                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-landscape-of-the-cf-environment-for-use-case.md "undefined#/properties/cfLandscape")                                                                                                |
| [cfspacename](#cfspacename)                                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-name-for-the-cf-space.md "undefined#/properties/cfspacename")                                                                                                                       |
| [cfspacequota](#cfspacequota)                                                                   | `object`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota.md "undefined#/properties/cfspacequota")                                                                                                                             |
| [clusterregion](#clusterregion)                                                                 | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-region-for-sap-btp-kyma-runtime-cluster.md "undefined#/properties/clusterregion")                                                                                                   |
| [customAppProviderSubaccountId](#customappprovidersubaccountid)                                 | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-provider-subaccount-id-of-custom-app-on-sap-btp.md "undefined#/properties/customAppProviderSubaccountId")                                                                           |
| [directoryid](#directoryid)                                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-directory-id-in-sap-btp-global-account.md "undefined#/properties/directoryid")                                                                                                      |
| [directoryname](#directoryname)                                                                 | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-directory-name-for-use-case.md "undefined#/properties/directoryname")                                                                                                               |
| [envvariables](#envvariables)                                                                   | `object`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-list-of-environment-variables-on-os-level-to-be-used-within-commands-defined-in-the-executebeforeaccountsetup-and-executeafteraccountsetup.md "undefined#/properties/envvariables") |
| [fallbackserviceplan](#fallbackserviceplan)                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-fallback-service-plan-if-the-plan-defined-in-the-use-case-is-not-supported.md "undefined#/properties/fallbackserviceplan")                                                          |
| [globalaccount](#globalaccount)                                                                 | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-your-sap-btp-global-account.md "undefined#/properties/globalaccount")                                                                                                               |
| [iashost](#iashost)                                                                             | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-ias-host-for-your-sap-btp-sub-account.md "undefined#/properties/iashost")                                                                                                           |
| [k8snamespace](#k8snamespace)                                                                   | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-name-for-the-kubernetes-namespace.md "undefined#/properties/k8snamespace")                                                                                                          |
| [kubeconfigpath](#kubeconfigpath)                                                               | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-path-to-kubeconfig-file.md "undefined#/properties/kubeconfigpath")                                                                                                                  |
| [logcommands](#logcommands)                                                                     | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-log-all-commands-sent-to-your-sap-btp-account.md "undefined#/properties/logcommands")                                                                                               |
| [logfile](#logfile)                                                                             | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-log-file.md "undefined#/properties/logfile")                                                                                                                                        |
| [loginmethod](#loginmethod)                                                                     | `string`  | Required | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-login-method-to-sap-btp.md "undefined#/properties/loginmethod")                                                                                                                     |
| [metadatafile](#metadatafile)                                                                   | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-file-for-log-information.md "undefined#/properties/metadatafile")                                                                                                                   |
| [myemail](#myemail)                                                                             | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-your-email-address.md "undefined#/properties/myemail")                                                                                                                              |
| [mypassword](#mypassword)                                                                       | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-password-for-the-user-of-your-sap-btp-account-use-with-care.md "undefined#/properties/mypassword")                                                                                  |
| [myusergroups](#myusergroups)                                                                   | `array`   | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-list-of-user-groups-to-be-used-in-btpsa.md "undefined#/properties/myusergroups")                                                                                                    |
| [org](#org)                                                                                     | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-org-name-of-the-cf-environment-for-use-case.md "undefined#/properties/org")                                                                                                         |
| [orgid](#orgid)                                                                                 | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-org-id-of-the-cf-environment-for-use-case.md "undefined#/properties/orgid")                                                                                                         |
| [parameterfile](#parameterfile)                                                                 | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-parameters-file-for-btp-setup-automator.md "undefined#/properties/parameterfile")                                                                                                   |
| [pollingIntervalForKymaCreationInMinutes](#pollingintervalforkymacreationinminutes)             | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-created.md "undefined#/properties/pollingIntervalForKymaCreationInMinutes")                            |
| [pollingIntervalForKymaDeprovisioningInMinutes](#pollingintervalforkymadeprovisioninginminutes) | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-deprovisioneddeleted.md "undefined#/properties/pollingIntervalForKymaDeprovisioningInMinutes")         |
| [prunesubaccount](#prunesubaccount)                                                             | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-same-like-parameter-pruneusecase-but-on-top-deletes-the-subaccount.md "undefined#/properties/prunesubaccount")                                                                      |
| [pruneusecase](#pruneusecase)                                                                   | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-delete-all-assets-of-a-usecase-based-on-the-collected-info-in-the-metadatafile.md "undefined#/properties/pruneusecase")                                                             |
| [region](#region)                                                                               | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-region-for-sap-btp-subaccount.md "undefined#/properties/region")                                                                                                                    |
| [repeatstatusrequest](#repeatstatusrequest)                                                     | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-time-in-seconds-to-wait-after-requesting-status-info-pulling.md "undefined#/properties/repeatstatusrequest")                                                                        |
| [repeatstatustimeout](#repeatstatustimeout)                                                     | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-timeout-in-seconds-after-which-requests-should-be-stopped.md "undefined#/properties/repeatstatustimeout")                                                                           |
| [rundefaulttests](#rundefaulttests)                                                             | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-switch-to-run-default-tests-at-the-beginning-of-the-script.md "undefined#/properties/rundefaulttests")                                                                              |
| [subaccountid](#subaccountid)                                                                   | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-subaccount-id-of-sap-btp-sub-account.md "undefined#/properties/subaccountid")                                                                                                       |
| [subaccountname](#subaccountname)                                                               | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-sub-account-name-for-use-case.md "undefined#/properties/subaccountname")                                                                                                            |
| [subdomain](#subdomain)                                                                         | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-subdomain-of-sub-account.md "undefined#/properties/subdomain")                                                                                                                      |
| [suffixinstancename](#suffixinstancename)                                                       | `string`  | Optional | can be null    | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-suffix-attached-to-each-service-instance-created.md "undefined#/properties/suffixinstancename")                                                                                     |
| [timeoutLimitForKymaCreationInMinutes](#timeoutlimitforkymacreationinminutes)                   | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-created.md "undefined#/properties/timeoutLimitForKymaCreationInMinutes")                                    |
| [timeoutLimitForKymaDeprovisioningInMinutes](#timeoutlimitforkymadeprovisioninginminutes)       | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-deprovisioneddeleted.md "undefined#/properties/timeoutLimitForKymaDeprovisioningInMinutes")                 |
| [usecasefile](#usecasefile)                                                                     | `string`  | Required | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-file-with-usecase-config.md "undefined#/properties/usecasefile")                                                                                                                    |
| [usedirectory](#usedirectory)                                                                   | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-trigger-creationusage-of-a-directory-for-the-subaccount.md "undefined#/properties/usedirectory")                                                                                    |
| [waitForKymaEnvironmentCreation](#waitforkymaenvironmentcreation)                               | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-should-the-tool-wait-for-the-creation-of-the-kyma-environment.md "undefined#/properties/waitForKymaEnvironmentCreation")                                                            |

## $schema



`$schema`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-schema.md "undefined#/properties/$schema")

### $schema Type

`string`

## btpcliapihostregion

host region for the BTP CLI calls

`btpcliapihostregion`

*   is optional

*   Type: `string` ([host region for the BTP CLI calls](btpsa-parameters-properties-host-region-for-the-btp-cli-calls.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-host-region-for-the-btp-cli-calls.md "undefined#/properties/btpcliapihostregion")

### btpcliapihostregion Type

`string` ([host region for the BTP CLI calls](btpsa-parameters-properties-host-region-for-the-btp-cli-calls.md))

### btpcliapihostregion Default Value

The default value is:

```json
"eu10"
```

## cfcliapihostregion

host region for the Cloud Foundry CLI (normally the same as 'region'). In case of errors you might have to set this to e.g. 'eu10-004' (check CF API in your SAP BTP cockpit in the sub account and CF environment).

`cfcliapihostregion`

*   is optional

*   Type: `string` ([host region for the Cloud Foundry CLI calls](btpsa-parameters-properties-host-region-for-the-cloud-foundry-cli-calls.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-host-region-for-the-cloud-foundry-cli-calls.md "undefined#/properties/cfcliapihostregion")

### cfcliapihostregion Type

`string` ([host region for the Cloud Foundry CLI calls](btpsa-parameters-properties-host-region-for-the-cloud-foundry-cli-calls.md))

## cfLandscape

landscape of the Cloud Foundry environment to be used for your use case (e.g. cf-eu10-004)

`cfLandscape`

*   is optional

*   Type: `string` ([landscape of the CF environment for use case](btpsa-parameters-properties-landscape-of-the-cf-environment-for-use-case.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-landscape-of-the-cf-environment-for-use-case.md "undefined#/properties/cfLandscape")

### cfLandscape Type

`string` ([landscape of the CF environment for use case](btpsa-parameters-properties-landscape-of-the-cf-environment-for-use-case.md))

## cfspacename

name for the Cloudfoundry space to be used for your use case

`cfspacename`

*   is optional

*   Type: `string` ([name for the CF space](btpsa-parameters-properties-name-for-the-cf-space.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-name-for-the-cf-space.md "undefined#/properties/cfspacename")

### cfspacename Type

`string` ([name for the CF space](btpsa-parameters-properties-name-for-the-cf-space.md))

### cfspacename Default Value

The default value is:

```json
"development"
```

## cfspacequota

space quota definition for the cf space

`cfspacequota`

*   is optional

*   Type: `object` ([CF space quota](btpsa-parameters-properties-cf-space-quota.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota.md "undefined#/properties/cfspacequota")

### cfspacequota Type

`object` ([CF space quota](btpsa-parameters-properties-cf-space-quota.md))

## clusterregion

region for the SAP BTP Kyma runtime cluster. This parameter is used as default for Kyma cluster creation. Override via usecase.json possible

`clusterregion`

*   is optional

*   Type: `string` ([region for SAP BTP Kyma runtime cluster](btpsa-parameters-properties-region-for-sap-btp-kyma-runtime-cluster.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-region-for-sap-btp-kyma-runtime-cluster.md "undefined#/properties/clusterregion")

### clusterregion Type

`string` ([region for SAP BTP Kyma runtime cluster](btpsa-parameters-properties-region-for-sap-btp-kyma-runtime-cluster.md))

## customAppProviderSubaccountId

id of provider sub account of custom app

`customAppProviderSubaccountId`

*   is optional

*   Type: `string` ([provider subaccount id of custom app on SAP BTP](btpsa-parameters-properties-provider-subaccount-id-of-custom-app-on-sap-btp.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-provider-subaccount-id-of-custom-app-on-sap-btp.md "undefined#/properties/customAppProviderSubaccountId")

### customAppProviderSubaccountId Type

`string` ([provider subaccount id of custom app on SAP BTP](btpsa-parameters-properties-provider-subaccount-id-of-custom-app-on-sap-btp.md))

## directoryid

id of the directory that should be used

`directoryid`

*   is optional

*   Type: `string` ([directory id in SAP BTP global account](btpsa-parameters-properties-directory-id-in-sap-btp-global-account.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-directory-id-in-sap-btp-global-account.md "undefined#/properties/directoryid")

### directoryid Type

`string` ([directory id in SAP BTP global account](btpsa-parameters-properties-directory-id-in-sap-btp-global-account.md))

## directoryname

name of your directory in case you want to define a specific name for it

`directoryname`

*   is optional

*   Type: `string` ([directory name for use case](btpsa-parameters-properties-directory-name-for-use-case.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-directory-name-for-use-case.md "undefined#/properties/directoryname")

### directoryname Type

`string` ([directory name for use case](btpsa-parameters-properties-directory-name-for-use-case.md))

## envvariables

list of environment variables on OS level to be used within commands defined in the `executeBeforeAccountSetup` and `executeAfterAccountSetup`.

`envvariables`

*   is optional

*   Type: `object` ([list of environment variables on OS level to be used within commands defined in the \`executeBeforeAccountSetup\` and \`executeAfterAccountSetup\`.](btpsa-parameters-properties-list-of-environment-variables-on-os-level-to-be-used-within-commands-defined-in-the-executebeforeaccountsetup-and-executeafteraccountsetup.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-list-of-environment-variables-on-os-level-to-be-used-within-commands-defined-in-the-executebeforeaccountsetup-and-executeafteraccountsetup.md "undefined#/properties/envvariables")

### envvariables Type

`object` ([list of environment variables on OS level to be used within commands defined in the \`executeBeforeAccountSetup\` and \`executeAfterAccountSetup\`.](btpsa-parameters-properties-list-of-environment-variables-on-os-level-to-be-used-within-commands-defined-in-the-executebeforeaccountsetup-and-executeafteraccountsetup.md))

## fallbackserviceplan

if defined, the tool will use the defined name as fallback service plan, if the plan defined in the use case is not supported

`fallbackserviceplan`

*   is optional

*   Type: `string` ([fallback service plan, if the plan defined in the use case is not supported](btpsa-parameters-properties-fallback-service-plan-if-the-plan-defined-in-the-use-case-is-not-supported.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-fallback-service-plan-if-the-plan-defined-in-the-use-case-is-not-supported.md "undefined#/properties/fallbackserviceplan")

### fallbackserviceplan Type

`string` ([fallback service plan, if the plan defined in the use case is not supported](btpsa-parameters-properties-fallback-service-plan-if-the-plan-defined-in-the-use-case-is-not-supported.md))

## globalaccount

the 'subdomain id' of your SAP BTP global account (please check it in the SAP BTP cockpit)

`globalaccount`

*   is optional

*   Type: `string` ([your SAP BTP global account](btpsa-parameters-properties-your-sap-btp-global-account.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-your-sap-btp-global-account.md "undefined#/properties/globalaccount")

### globalaccount Type

`string` ([your SAP BTP global account](btpsa-parameters-properties-your-sap-btp-global-account.md))

## iashost

IAS host for your SAP BTP sub account in case you want to make use of it in your use case (create a service instance for service 'xsuaa' and plan 'apiaccess')

`iashost`

*   is optional

*   Type: `string` ([IAS host for your SAP BTP sub account](btpsa-parameters-properties-ias-host-for-your-sap-btp-sub-account.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-ias-host-for-your-sap-btp-sub-account.md "undefined#/properties/iashost")

### iashost Type

`string` ([IAS host for your SAP BTP sub account](btpsa-parameters-properties-ias-host-for-your-sap-btp-sub-account.md))

## k8snamespace

name for the Kubernetes namespace to be used for your use case

`k8snamespace`

*   is optional

*   Type: `string` ([name for the Kubernetes namespace](btpsa-parameters-properties-name-for-the-kubernetes-namespace.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-name-for-the-kubernetes-namespace.md "undefined#/properties/k8snamespace")

### k8snamespace Type

`string` ([name for the Kubernetes namespace](btpsa-parameters-properties-name-for-the-kubernetes-namespace.md))

### k8snamespace Default Value

The default value is:

```json
"default"
```

## kubeconfigpath

path to kubeconfig file to be used for your use case

`kubeconfigpath`

*   is optional

*   Type: `string` ([path to kubeconfig file](btpsa-parameters-properties-path-to-kubeconfig-file.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-path-to-kubeconfig-file.md "undefined#/properties/kubeconfigpath")

### kubeconfigpath Type

`string` ([path to kubeconfig file](btpsa-parameters-properties-path-to-kubeconfig-file.md))

### kubeconfigpath Default Value

The default value is:

```json
".kube/configsa"
```

## logcommands

if set to True, the script will log all commands sent to the SAP BTP account. If set to False it won't

`logcommands`

*   is optional

*   Type: `boolean` ([log all commands sent to your SAP BTP account](btpsa-parameters-properties-log-all-commands-sent-to-your-sap-btp-account.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-log-all-commands-sent-to-your-sap-btp-account.md "undefined#/properties/logcommands")

### logcommands Type

`boolean` ([log all commands sent to your SAP BTP account](btpsa-parameters-properties-log-all-commands-sent-to-your-sap-btp-account.md))

### logcommands Default Value

The default value is:

```json
true
```

## logfile

file including all logged information

`logfile`

*   is optional

*   Type: `string` ([log file](btpsa-parameters-properties-log-file.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-log-file.md "undefined#/properties/logfile")

### logfile Type

`string` ([log file](btpsa-parameters-properties-log-file.md))

### logfile Default Value

The default value is:

```json
"log/script.log"
```

## loginmethod

if set to sso, you'll need to open a link provided in a browser to login. Set to basicAuthentication (default) the script will ask if you want to provide username and password. If set to **envVariables** you need to provide the email address and password by setting the environment variable **BTPSA\_PARAM\_MYEMAIL** and **BTPSA\_PARAM\_MYPASSWORD**. In addition you can as well provide the global account through the environment variable **BTPSA\_PARAM\_GLOBALACCOUNT**. Like this: export BTPSA\_PARAM\_MYEMAIL=<youremail@x.com>

`loginmethod`

*   is required

*   Type: `string` ([login method to SAP BTP](btpsa-parameters-properties-login-method-to-sap-btp.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-login-method-to-sap-btp.md "undefined#/properties/loginmethod")

### loginmethod Type

`string` ([login method to SAP BTP](btpsa-parameters-properties-login-method-to-sap-btp.md))

### loginmethod Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"basicAuthentication"` |             |
| `"sso"`                 |             |
| `"envVariables"`        |             |

### loginmethod Default Value

The default value is:

```json
"basicAuthentication"
```

## metadatafile

file for log information

`metadatafile`

*   is optional

*   Type: `string` ([file for log information](btpsa-parameters-properties-file-for-log-information.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-file-for-log-information.md "undefined#/properties/metadatafile")

### metadatafile Type

`string` ([file for log information](btpsa-parameters-properties-file-for-log-information.md))

### metadatafile Default Value

The default value is:

```json
"log/metadata_log.json"
```

## myemail

Email address you use to access your SAP BTP account

`myemail`

*   is optional

*   Type: `string` ([Your email address](btpsa-parameters-properties-your-email-address.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-your-email-address.md "undefined#/properties/myemail")

### myemail Type

`string` ([Your email address](btpsa-parameters-properties-your-email-address.md))

### myemail Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## mypassword

password for the user of your SAP BTP account (USE WITH CARE!)

`mypassword`

*   is optional

*   Type: `string` ([password for the user of your SAP BTP account (USE WITH CARE!)](btpsa-parameters-properties-password-for-the-user-of-your-sap-btp-account-use-with-care.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-password-for-the-user-of-your-sap-btp-account-use-with-care.md "undefined#/properties/mypassword")

### mypassword Type

`string` ([password for the user of your SAP BTP account (USE WITH CARE!)](btpsa-parameters-properties-password-for-the-user-of-your-sap-btp-account-use-with-care.md))

## myusergroups

list of user groups to be used in btpsa

`myusergroups`

*   is optional

*   Type: `object[]` ([Details](btpsa-parameters-properties-list-of-user-groups-to-be-used-in-btpsa-items.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-list-of-user-groups-to-be-used-in-btpsa.md "undefined#/properties/myusergroups")

### myusergroups Type

`object[]` ([Details](btpsa-parameters-properties-list-of-user-groups-to-be-used-in-btpsa-items.md))

## org

org name of the Cloud Foundry environment to be used for your use case

`org`

*   is optional

*   Type: `string` ([org name of the CF environment for use case](btpsa-parameters-properties-org-name-of-the-cf-environment-for-use-case.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-org-name-of-the-cf-environment-for-use-case.md "undefined#/properties/org")

### org Type

`string` ([org name of the CF environment for use case](btpsa-parameters-properties-org-name-of-the-cf-environment-for-use-case.md))

## orgid

org id of the Cloudfoundry environment to be used for your use case

`orgid`

*   is optional

*   Type: `string` ([org id of the CF environment for use case](btpsa-parameters-properties-org-id-of-the-cf-environment-for-use-case.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-org-id-of-the-cf-environment-for-use-case.md "undefined#/properties/orgid")

### orgid Type

`string` ([org id of the CF environment for use case](btpsa-parameters-properties-org-id-of-the-cf-environment-for-use-case.md))

## parameterfile

file to deliver all parameters within a single json file

`parameterfile`

*   is optional

*   Type: `string` ([parameters file for btp-setup-automator](btpsa-parameters-properties-parameters-file-for-btp-setup-automator.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-parameters-file-for-btp-setup-automator.md "undefined#/properties/parameterfile")

### parameterfile Type

`string` ([parameters file for btp-setup-automator](btpsa-parameters-properties-parameters-file-for-btp-setup-automator.md))

### parameterfile Default Value

The default value is:

```json
"parameters.json"
```

## pollingIntervalForKymaCreationInMinutes

Polling interval in minutes when tool is waiting for the Kyma instance to be created

`pollingIntervalForKymaCreationInMinutes`

*   is optional

*   Type: `integer` ([Polling interval in minutes when tool is waiting for the Kyma instance to be created](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-created.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-created.md "undefined#/properties/pollingIntervalForKymaCreationInMinutes")

### pollingIntervalForKymaCreationInMinutes Type

`integer` ([Polling interval in minutes when tool is waiting for the Kyma instance to be created](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-created.md))

### pollingIntervalForKymaCreationInMinutes Default Value

The default value is:

```json
5
```

## pollingIntervalForKymaDeprovisioningInMinutes

Polling interval in minutes when tool is waiting for the Kyma instance to be deprovisioned/deleted

`pollingIntervalForKymaDeprovisioningInMinutes`

*   is optional

*   Type: `integer` ([Polling interval in minutes when tool is waiting for the Kyma instance to be deprovisioned/deleted](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-deprovisioneddeleted.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-deprovisioneddeleted.md "undefined#/properties/pollingIntervalForKymaDeprovisioningInMinutes")

### pollingIntervalForKymaDeprovisioningInMinutes Type

`integer` ([Polling interval in minutes when tool is waiting for the Kyma instance to be deprovisioned/deleted](btpsa-parameters-properties-polling-interval-in-minutes-when-tool-is-waiting-for-the-kyma-instance-to-be-deprovisioneddeleted.md))

### pollingIntervalForKymaDeprovisioningInMinutes Default Value

The default value is:

```json
5
```

## prunesubaccount

if set to True: same like -pruneusecase, but on-top deletes the subaccount. USE WITH CARE!!!

`prunesubaccount`

*   is optional

*   Type: `boolean` ([same like parameter 'pruneusecase', but on-top deletes the subaccount](btpsa-parameters-properties-same-like-parameter-pruneusecase-but-on-top-deletes-the-subaccount.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-same-like-parameter-pruneusecase-but-on-top-deletes-the-subaccount.md "undefined#/properties/prunesubaccount")

### prunesubaccount Type

`boolean` ([same like parameter 'pruneusecase', but on-top deletes the subaccount](btpsa-parameters-properties-same-like-parameter-pruneusecase-but-on-top-deletes-the-subaccount.md))

## pruneusecase

if set to True: deletes all assets of a usecase based on the collected info in the metadatafile. No confirmation message. USE WITH CARE!!!

`pruneusecase`

*   is optional

*   Type: `boolean` ([delete all assets of a usecase based on the collected info in the metadatafile](btpsa-parameters-properties-delete-all-assets-of-a-usecase-based-on-the-collected-info-in-the-metadatafile.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-delete-all-assets-of-a-usecase-based-on-the-collected-info-in-the-metadatafile.md "undefined#/properties/pruneusecase")

### pruneusecase Type

`boolean` ([delete all assets of a usecase based on the collected info in the metadatafile](btpsa-parameters-properties-delete-all-assets-of-a-usecase-based-on-the-collected-info-in-the-metadatafile.md))

## region

region for the SAP BTP sub account that should be used for the use case

`region`

*   is optional

*   Type: `string` ([region for SAP BTP subaccount](btpsa-parameters-properties-region-for-sap-btp-subaccount.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-region-for-sap-btp-subaccount.md "undefined#/properties/region")

### region Type

`string` ([region for SAP BTP subaccount](btpsa-parameters-properties-region-for-sap-btp-subaccount.md))

### region Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"ae1"`  |             |
| `"ap1"`  |             |
| `"ap10"` |             |
| `"ap11"` |             |
| `"ap12"` |             |
| `"ap2"`  |             |
| `"ap20"` |             |
| `"ap21"` |             |
| `"br1"`  |             |
| `"br10"` |             |
| `"ca1"`  |             |
| `"ca10"` |             |
| `"ca2"`  |             |
| `"ch20"` |             |
| `"cn1"`  |             |
| `"eu1"`  |             |
| `"eu10"` |             |
| `"eu11"` |             |
| `"eu2"`  |             |
| `"eu20"` |             |
| `"eu3"`  |             |
| `"eu30"` |             |
| `"in30"` |             |
| `"jp1"`  |             |
| `"jp10"` |             |
| `"jp20"` |             |
| `"sa1"`  |             |
| `"us1"`  |             |
| `"us10"` |             |
| `"us2"`  |             |
| `"us20"` |             |
| `"us21"` |             |
| `"us3"`  |             |
| `"us30"` |             |
| `"us4"`  |             |

### region Default Value

The default value is:

```json
"us10"
```

## repeatstatusrequest

time in seconds to wait after requesting status info (pulling)

`repeatstatusrequest`

*   is optional

*   Type: `integer` ([time in seconds to wait after requesting status info (pulling)](btpsa-parameters-properties-time-in-seconds-to-wait-after-requesting-status-info-pulling.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-time-in-seconds-to-wait-after-requesting-status-info-pulling.md "undefined#/properties/repeatstatusrequest")

### repeatstatusrequest Type

`integer` ([time in seconds to wait after requesting status info (pulling)](btpsa-parameters-properties-time-in-seconds-to-wait-after-requesting-status-info-pulling.md))

### repeatstatusrequest Default Value

The default value is:

```json
4
```

## repeatstatustimeout

timeout in seconds after which requests should be stopped

`repeatstatustimeout`

*   is optional

*   Type: `integer` ([timeout in seconds after which requests should be stopped](btpsa-parameters-properties-timeout-in-seconds-after-which-requests-should-be-stopped.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-timeout-in-seconds-after-which-requests-should-be-stopped.md "undefined#/properties/repeatstatustimeout")

### repeatstatustimeout Type

`integer` ([timeout in seconds after which requests should be stopped](btpsa-parameters-properties-timeout-in-seconds-after-which-requests-should-be-stopped.md))

### repeatstatustimeout Default Value

The default value is:

```json
4200
```

## rundefaulttests

switch to run default tests at the beginning of the script (INTERNAL USAGE)

`rundefaulttests`

*   is optional

*   Type: `boolean` ([switch to run default tests at the beginning of the script](btpsa-parameters-properties-switch-to-run-default-tests-at-the-beginning-of-the-script.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-switch-to-run-default-tests-at-the-beginning-of-the-script.md "undefined#/properties/rundefaulttests")

### rundefaulttests Type

`boolean` ([switch to run default tests at the beginning of the script](btpsa-parameters-properties-switch-to-run-default-tests-at-the-beginning-of-the-script.md))

### rundefaulttests Default Value

The default value is:

```json
true
```

## subaccountid

id of your sub account that should be used

`subaccountid`

*   is optional

*   Type: `string` ([subaccount id of SAP BTP sub account](btpsa-parameters-properties-subaccount-id-of-sap-btp-sub-account.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-subaccount-id-of-sap-btp-sub-account.md "undefined#/properties/subaccountid")

### subaccountid Type

`string` ([subaccount id of SAP BTP sub account](btpsa-parameters-properties-subaccount-id-of-sap-btp-sub-account.md))

## subaccountname

name of your sub account in case you want to define a specific name for your sub account

`subaccountname`

*   is optional

*   Type: `string` ([sub account name for use case](btpsa-parameters-properties-sub-account-name-for-use-case.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-sub-account-name-for-use-case.md "undefined#/properties/subaccountname")

### subaccountname Type

`string` ([sub account name for use case](btpsa-parameters-properties-sub-account-name-for-use-case.md))

## subdomain

name of the subdomain of your sub account

`subdomain`

*   is optional

*   Type: `string` ([subdomain of sub account](btpsa-parameters-properties-subdomain-of-sub-account.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-subdomain-of-sub-account.md "undefined#/properties/subdomain")

### subdomain Type

`string` ([subdomain of sub account](btpsa-parameters-properties-subdomain-of-sub-account.md))

## suffixinstancename

suffix attached to each service instance that is created (e.g. hana\_yoursuffixinstancename)

`suffixinstancename`

*   is optional

*   Type: `string` ([suffix attached to each service instance created](btpsa-parameters-properties-suffix-attached-to-each-service-instance-created.md))

*   can be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-suffix-attached-to-each-service-instance-created.md "undefined#/properties/suffixinstancename")

### suffixinstancename Type

`string` ([suffix attached to each service instance created](btpsa-parameters-properties-suffix-attached-to-each-service-instance-created.md))

## timeoutLimitForKymaCreationInMinutes

Limit in minutes until the tool should wait for the Kyma instance to be created

`timeoutLimitForKymaCreationInMinutes`

*   is optional

*   Type: `integer` ([Limit in minutes until the tool should wait for the Kyma instance to be created](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-created.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-created.md "undefined#/properties/timeoutLimitForKymaCreationInMinutes")

### timeoutLimitForKymaCreationInMinutes Type

`integer` ([Limit in minutes until the tool should wait for the Kyma instance to be created](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-created.md))

### timeoutLimitForKymaCreationInMinutes Default Value

The default value is:

```json
40
```

## timeoutLimitForKymaDeprovisioningInMinutes

Limit in minutes until the tool should wait for the Kyma instance to be deprovisioned/deleted

`timeoutLimitForKymaDeprovisioningInMinutes`

*   is optional

*   Type: `integer` ([Limit in minutes until the tool should wait for the Kyma instance to be deprovisioned/deleted](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-deprovisioneddeleted.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-deprovisioneddeleted.md "undefined#/properties/timeoutLimitForKymaDeprovisioningInMinutes")

### timeoutLimitForKymaDeprovisioningInMinutes Type

`integer` ([Limit in minutes until the tool should wait for the Kyma instance to be deprovisioned/deleted](btpsa-parameters-properties-limit-in-minutes-until-the-tool-should-wait-for-the-kyma-instance-to-be-deprovisioneddeleted.md))

### timeoutLimitForKymaDeprovisioningInMinutes Default Value

The default value is:

```json
40
```

## usecasefile

file with usecase config

`usecasefile`

*   is required

*   Type: `string` ([file with usecase config](btpsa-parameters-properties-file-with-usecase-config.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-file-with-usecase-config.md "undefined#/properties/usecasefile")

### usecasefile Type

`string` ([file with usecase config](btpsa-parameters-properties-file-with-usecase-config.md))

## usedirectory

Should the tool create/use a directory for the subaccount?

`usedirectory`

*   is optional

*   Type: `boolean` ([Trigger creation/usage of a directory for the subaccount?](btpsa-parameters-properties-trigger-creationusage-of-a-directory-for-the-subaccount.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-trigger-creationusage-of-a-directory-for-the-subaccount.md "undefined#/properties/usedirectory")

### usedirectory Type

`boolean` ([Trigger creation/usage of a directory for the subaccount?](btpsa-parameters-properties-trigger-creationusage-of-a-directory-for-the-subaccount.md))

## waitForKymaEnvironmentCreation

Should the tool wait for the creation of the Kyma environment

`waitForKymaEnvironmentCreation`

*   is optional

*   Type: `boolean` ([Should the tool wait for the creation of the Kyma environment](btpsa-parameters-properties-should-the-tool-wait-for-the-creation-of-the-kyma-environment.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-should-the-tool-wait-for-the-creation-of-the-kyma-environment.md "undefined#/properties/waitForKymaEnvironmentCreation")

### waitForKymaEnvironmentCreation Type

`boolean` ([Should the tool wait for the creation of the Kyma environment](btpsa-parameters-properties-should-the-tool-wait-for-the-creation-of-the-kyma-environment.md))

### waitForKymaEnvironmentCreation Default Value

The default value is:

```json
true
```
