## items Type

`object` ([Details](btpsa-usecase-properties-services-items.md))

all of

*   [Untitled undefined type in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-0.md "check type definition")

*   [Untitled undefined type in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1.md "check type definition")

*   [Untitled undefined type in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-2.md "check type definition")

*   [Untitled undefined type in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-3.md "check type definition")

# items Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                             |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [amount](#amount)                                   | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-amount-to-be-used-for-the-service.md "undefined#/properties/services/items/properties/amount")                                                         |
| [assignrolecollections](#assignrolecollections)     | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-be-created-within-the-btp-account.md "undefined#/properties/services/items/properties/assignrolecollections")              |
| [category](#category)                               | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-category-of-the-service.md "undefined#/properties/services/items/properties/category")                                                                 |
| [createServiceKeys](#createservicekeys)             | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-service-keys-to-be-created-for-the-service.md "undefined#/properties/services/items/properties/createServiceKeys")                             |
| [customerDeveloped](#customerdeveloped)             | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-custom-developed-application.md "undefined#/properties/services/items/properties/customerDeveloped")                                                   |
| [entitleonly](#entitleonly)                         | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-only-entitlement-no-service-instances-will-be-created-by-the-tool.md "undefined#/properties/services/items/properties/entitleonly")                    |
| [instancename](#instancename)                       | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-name-of-the-service-instance.md "undefined#/properties/services/items/properties/instancename")                                                        |
| [name](#name)                                       | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-name-of-the-service.md "undefined#/properties/services/items/properties/name")                                                                         |
| [parameters](#parameters)                           | Multiple  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-parameters-for-the-service.md "undefined#/properties/services/items/properties/parameters")                                                            |
| [plan](#plan)                                       | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-plan-name-of-the-service.md "undefined#/properties/services/items/properties/plan")                                                                    |
| [planCatalogName](#plancatalogname)                 | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-catalog-name-of-the-service-plan.md "undefined#/properties/services/items/properties/planCatalogName")                                                 |
| [relatedLinks](#relatedlinks)                       | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-links-related-to-this-service.md "undefined#/properties/services/items/properties/relatedLinks")                                                       |
| [repeatstatusrequest](#repeatstatusrequest)         | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-number-of-seconds-when-status-should-be-checked.md "undefined#/properties/services/items/properties/repeatstatusrequest")                              |
| [repeatstatustimeout](#repeatstatustimeout)         | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-timeout-in-seconds-after-which-the-script-will-stop-checking-the-status.md "undefined#/properties/services/items/properties/repeatstatustimeout")      |
| [requiredrolecollections](#requiredrolecollections) | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to.md "undefined#/properties/services/items/properties/requiredrolecollections")                              |
| [requiredServices](#requiredservices)               | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-services-that-need-to-be-instantiated-before-instantiating-this-service.md "undefined#/properties/services/items/properties/requiredServices") |
| [serviceparameterfile](#serviceparameterfile)       | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-parameter-file-for-the-service.md "undefined#/properties/services/items/properties/serviceparameterfile")                                              |
| [statusResponse](#statusresponse)                   | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-creation-info.md "undefined#/properties/services/items/properties/statusResponse")                                                                     |
| [targetenvironment](#targetenvironment)             | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-environment-in-which-the-service-should-be-created.md "undefined#/properties/services/items/properties/targetenvironment")                             |

## amount

amount to be used for the service

`amount`

*   is optional

*   Type: `integer` ([amount to be used for the service](btpsa-usecase-properties-services-items-properties-amount-to-be-used-for-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-amount-to-be-used-for-the-service.md "undefined#/properties/services/items/properties/amount")

### amount Type

`integer` ([amount to be used for the service](btpsa-usecase-properties-services-items-properties-amount-to-be-used-for-the-service.md))

### amount Default Value

The default value is:

```json
1
```

## assignrolecollections

list of role collections to be created within the btp account

`assignrolecollections`

*   is optional

*   Type: `array` ([list of role collections to be created within the btp account](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-be-created-within-the-btp-account.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-be-created-within-the-btp-account.md "undefined#/properties/services/items/properties/assignrolecollections")

### assignrolecollections Type

`array` ([list of role collections to be created within the btp account](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-be-created-within-the-btp-account.md))

### assignrolecollections Default Value

The default value is:

```json
[]
```

## category

category of the service

`category`

*   is required

*   Type: `string` ([category of the service](btpsa-usecase-properties-services-items-properties-category-of-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-category-of-the-service.md "undefined#/properties/services/items/properties/category")

### category Type

`string` ([category of the service](btpsa-usecase-properties-services-items-properties-category-of-the-service.md))

### category Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"SERVICE"`        |             |
| `"APPLICATION"`    |             |
| `"CF_CUP_SERVICE"` |             |
| `"ENVIRONMENT"`    |             |

## createServiceKeys

list of service keys to be created for the service

`createServiceKeys`

*   is optional

*   Type: `array` ([list of service keys to be created for the service](btpsa-usecase-properties-services-items-properties-list-of-service-keys-to-be-created-for-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-service-keys-to-be-created-for-the-service.md "undefined#/properties/services/items/properties/createServiceKeys")

### createServiceKeys Type

`array` ([list of service keys to be created for the service](btpsa-usecase-properties-services-items-properties-list-of-service-keys-to-be-created-for-the-service.md))

### createServiceKeys Default Value

The default value is:

```json
[]
```

## customerDeveloped

custom developed application

`customerDeveloped`

*   is optional

*   Type: `boolean` ([custom developed application](btpsa-usecase-properties-services-items-properties-custom-developed-application.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-custom-developed-application.md "undefined#/properties/services/items/properties/customerDeveloped")

### customerDeveloped Type

`boolean` ([custom developed application](btpsa-usecase-properties-services-items-properties-custom-developed-application.md))

## entitleonly

only entitlement -  if true, the service will only be entitled, but not assigned to a role collection

`entitleonly`

*   is optional

*   Type: `boolean` ([only entitlement (no service instances will be created by the tool)](btpsa-usecase-properties-services-items-properties-only-entitlement-no-service-instances-will-be-created-by-the-tool.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-only-entitlement-no-service-instances-will-be-created-by-the-tool.md "undefined#/properties/services/items/properties/entitleonly")

### entitleonly Type

`boolean` ([only entitlement (no service instances will be created by the tool)](btpsa-usecase-properties-services-items-properties-only-entitlement-no-service-instances-will-be-created-by-the-tool.md))

### entitleonly Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `true`  |             |
| `false` |             |

## instancename

name of the service instance

`instancename`

*   is optional

*   Type: `string` ([name of the service instance](btpsa-usecase-properties-services-items-properties-name-of-the-service-instance.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-name-of-the-service-instance.md "undefined#/properties/services/items/properties/instancename")

### instancename Type

`string` ([name of the service instance](btpsa-usecase-properties-services-items-properties-name-of-the-service-instance.md))

## name

name of the service

`name`

*   is required

*   Type: `string` ([name of the service](btpsa-usecase-properties-services-items-properties-name-of-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-name-of-the-service.md "undefined#/properties/services/items/properties/name")

### name Type

`string` ([name of the service](btpsa-usecase-properties-services-items-properties-name-of-the-service.md))

## parameters

parameters for the service

`parameters`

*   is optional

*   Type: any of the folllowing: `object` or `string` ([parameters for the service](btpsa-usecase-properties-services-items-properties-parameters-for-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-parameters-for-the-service.md "undefined#/properties/services/items/properties/parameters")

### parameters Type

any of the folllowing: `object` or `string` ([parameters for the service](btpsa-usecase-properties-services-items-properties-parameters-for-the-service.md))

## plan

plan name of the service

`plan`

*   is optional

*   Type: `string` ([plan name of the service](btpsa-usecase-properties-services-items-properties-plan-name-of-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-plan-name-of-the-service.md "undefined#/properties/services/items/properties/plan")

### plan Type

`string` ([plan name of the service](btpsa-usecase-properties-services-items-properties-plan-name-of-the-service.md))

## planCatalogName

catalog name of the service plan

`planCatalogName`

*   is optional

*   Type: `string` ([catalog name of the service plan](btpsa-usecase-properties-services-items-properties-catalog-name-of-the-service-plan.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-catalog-name-of-the-service-plan.md "undefined#/properties/services/items/properties/planCatalogName")

### planCatalogName Type

`string` ([catalog name of the service plan](btpsa-usecase-properties-services-items-properties-catalog-name-of-the-service-plan.md))

## relatedLinks

links related to this service

`relatedLinks`

*   is optional

*   Type: `array` ([links related to this service](btpsa-usecase-properties-services-items-properties-links-related-to-this-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-links-related-to-this-service.md "undefined#/properties/services/items/properties/relatedLinks")

### relatedLinks Type

`array` ([links related to this service](btpsa-usecase-properties-services-items-properties-links-related-to-this-service.md))

## repeatstatusrequest

number of seconds when status should be checked

`repeatstatusrequest`

*   is optional

*   Type: `integer` ([number of seconds when status should be checked](btpsa-usecase-properties-services-items-properties-number-of-seconds-when-status-should-be-checked.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-number-of-seconds-when-status-should-be-checked.md "undefined#/properties/services/items/properties/repeatstatusrequest")

### repeatstatusrequest Type

`integer` ([number of seconds when status should be checked](btpsa-usecase-properties-services-items-properties-number-of-seconds-when-status-should-be-checked.md))

### repeatstatusrequest Default Value

The default value is:

```json
5
```

## repeatstatustimeout

timeout in seconds after which the script will stop checking the status

`repeatstatustimeout`

*   is optional

*   Type: `integer` ([timeout in seconds after which the script will stop checking the status](btpsa-usecase-properties-services-items-properties-timeout-in-seconds-after-which-the-script-will-stop-checking-the-status.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-timeout-in-seconds-after-which-the-script-will-stop-checking-the-status.md "undefined#/properties/services/items/properties/repeatstatustimeout")

### repeatstatustimeout Type

`integer` ([timeout in seconds after which the script will stop checking the status](btpsa-usecase-properties-services-items-properties-timeout-in-seconds-after-which-the-script-will-stop-checking-the-status.md))

### repeatstatustimeout Default Value

The default value is:

```json
3600
```

## requiredrolecollections

list of role collections to assign users to

`requiredrolecollections`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to.md "undefined#/properties/services/items/properties/requiredrolecollections")

### requiredrolecollections Type

`object[]` ([Details](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items.md))

## requiredServices

list of services that need to be instantiated before instantiating this service

`requiredServices`

*   is optional

*   Type: `array` ([list of services that need to be instantiated before instantiating this service](btpsa-usecase-properties-services-items-properties-list-of-services-that-need-to-be-instantiated-before-instantiating-this-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-services-that-need-to-be-instantiated-before-instantiating-this-service.md "undefined#/properties/services/items/properties/requiredServices")

### requiredServices Type

`array` ([list of services that need to be instantiated before instantiating this service](btpsa-usecase-properties-services-items-properties-list-of-services-that-need-to-be-instantiated-before-instantiating-this-service.md))

### requiredServices Default Value

The default value is:

```json
[]
```

## serviceparameterfile

parameter file for the service in case you want to provide the parameters via a file

`serviceparameterfile`

*   is optional

*   Type: `string` ([parameter file for the service](btpsa-usecase-properties-services-items-properties-parameter-file-for-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-parameter-file-for-the-service.md "undefined#/properties/services/items/properties/serviceparameterfile")

### serviceparameterfile Type

`string` ([parameter file for the service](btpsa-usecase-properties-services-items-properties-parameter-file-for-the-service.md))

## statusResponse

information that is available only durng the execution of the script (should not be set in the usecase.json file)

`statusResponse`

*   is optional

*   Type: `object` ([creation info](btpsa-usecase-properties-services-items-properties-creation-info.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-creation-info.md "undefined#/properties/services/items/properties/statusResponse")

### statusResponse Type

`object` ([creation info](btpsa-usecase-properties-services-items-properties-creation-info.md))

## targetenvironment

environment in which the service should be created

`targetenvironment`

*   is optional

*   Type: `string` ([environment in which the service should be created](btpsa-usecase-properties-services-items-properties-environment-in-which-the-service-should-be-created.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-environment-in-which-the-service-should-be-created.md "undefined#/properties/services/items/properties/targetenvironment")

### targetenvironment Type

`string` ([environment in which the service should be created](btpsa-usecase-properties-services-items-properties-environment-in-which-the-service-should-be-created.md))

### targetenvironment Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"cloudfoundry"` |             |
| `"kymaruntime"`  |             |
| `"sapbtp"`       |             |

### targetenvironment Default Value

The default value is:

```json
"cloudfoundry"
```
