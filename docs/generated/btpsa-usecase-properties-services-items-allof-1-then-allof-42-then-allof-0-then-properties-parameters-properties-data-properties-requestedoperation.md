## requestedOperation Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation.md))

# requestedOperation Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [arguments](#arguments) | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-arguments.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/0/then/properties/parameters/properties/data/properties/requestedOperation/properties/arguments") |
| [name](#name)           | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/0/then/properties/parameters/properties/data/properties/requestedOperation/properties/name")           |

## arguments

List of operation arguments

`arguments`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-arguments.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-arguments.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/0/then/properties/parameters/properties/data/properties/requestedOperation/properties/arguments")

### arguments Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-arguments.md))

## name

create instance for template recovery

`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-0-then-properties-parameters-properties-data-properties-requestedoperation-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/0/then/properties/parameters/properties/data/properties/requestedOperation/properties/name")

### name Type

`string`

### name Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"none"`              |             |
| `"TEMPLATE_RECOVERY"` |             |
