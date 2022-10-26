## JSON Schema for BTPSA use case definitions Type

`object` ([JSON Schema for BTPSA use case definitions](btpsa-usecase.md))

# JSON Schema for BTPSA use case definitions Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                          |
| :------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [$schema](#schema)                                      | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-schema.md "undefined#/properties/$schema")                                                                    |
| [aboutThisUseCase](#aboutthisusecase)                   | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service.md "undefined#/properties/aboutThisUseCase")                                              |
| [assignrolecollections](#assignrolecollections)         | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service.md "undefined#/properties/assignrolecollections")                |
| [executeAfterAccountSetup](#executeafteraccountsetup)   | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-after-setup-of-sap-btp-account.md "undefined#/properties/executeAfterAccountSetup")           |
| [executeBeforeAccountSetup](#executebeforeaccountsetup) | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-before-setup-of-sap-btp-account.md "undefined#/properties/executeBeforeAccountSetup")         |
| [executeToPruneUseCase](#executetopruneusecase)         | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-to-prune-use-case-from-your-sap-btp-account.md "undefined#/properties/executeToPruneUseCase") |
| [services](#services)                                   | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services.md "undefined#/properties/services")                                                                 |

## $schema



`$schema`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-schema.md "undefined#/properties/$schema")

### $schema Type

`string`

## aboutThisUseCase

name of the service

`aboutThisUseCase`

*   is optional

*   Type: `object` ([name of the service](btpsa-usecase-properties-name-of-the-service.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service.md "undefined#/properties/aboutThisUseCase")

### aboutThisUseCase Type

`object` ([name of the service](btpsa-usecase-properties-name-of-the-service.md))

## assignrolecollections

role collections to be assigned to a service

`assignrolecollections`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service.md "undefined#/properties/assignrolecollections")

### assignrolecollections Type

`object[]` ([Details](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items.md))

## executeAfterAccountSetup

create a list of commands, that should be executed after the SAP BTP account is setup

`executeAfterAccountSetup`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-commands-to-run-after-setup-of-sap-btp-account-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-after-setup-of-sap-btp-account.md "undefined#/properties/executeAfterAccountSetup")

### executeAfterAccountSetup Type

`object[]` ([Details](btpsa-usecase-properties-commands-to-run-after-setup-of-sap-btp-account-items.md))

## executeBeforeAccountSetup

create a list of commands, that should be executed before the SAP BTP account is setup

`executeBeforeAccountSetup`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-commands-to-run-before-setup-of-sap-btp-account-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-before-setup-of-sap-btp-account.md "undefined#/properties/executeBeforeAccountSetup")

### executeBeforeAccountSetup Type

`object[]` ([Details](btpsa-usecase-properties-commands-to-run-before-setup-of-sap-btp-account-items.md))

## executeToPruneUseCase

create a list of commands, that should be executed to prune the use case from your SAP BTP account

`executeToPruneUseCase`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-commands-to-run-to-prune-use-case-from-your-sap-btp-account-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-commands-to-run-to-prune-use-case-from-your-sap-btp-account.md "undefined#/properties/executeToPruneUseCase")

### executeToPruneUseCase Type

`object[]` ([Details](btpsa-usecase-properties-commands-to-run-to-prune-use-case-from-your-sap-btp-account-items.md))

## services



`services`

*   is optional

*   Type: `object[]` ([Details](btpsa-usecase-properties-services-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services.md "undefined#/properties/services")

### services Type

`object[]` ([Details](btpsa-usecase-properties-services-items.md))
