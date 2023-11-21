## data Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data.md))

# data Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [datalakeID](#datalakeid)             | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakeid.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakeID")             |
| [datalakePassword](#datalakepassword) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakepassword.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakePassword") |
| [datalakeUser](#datalakeuser)         | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakeuser.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakeUser")         |
| [hanaID](#hanaid)                     | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanaid.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaID")                     |
| [hanaPassword](#hanapassword)         | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanapassword.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaPassword")         |
| [hanaUser](#hanauser)                 | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanauser.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaUser")                 |

## datalakeID

Service instance GUID of the data-lake instance

`datalakeID`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakeid.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakeID")

### datalakeID Type

`string`

### datalakeID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## datalakePassword

Password in the data lake instance

`datalakePassword`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakepassword.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakePassword")

### datalakePassword Type

`string`

### datalakePassword Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## datalakeUser

User ID in the data lake instance

`datalakeUser`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-datalakeuser.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/datalakeUser")

### datalakeUser Type

`string`

### datalakeUser Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## hanaID

Service instance GUID of the HANA instance

`hanaID`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanaid.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaID")

### hanaID Type

`string`

### hanaID Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## hanaPassword

Password for the HANA user

`hanaPassword`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanapassword.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaPassword")

### hanaPassword Type

`string`

### hanaPassword Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## hanaUser

User ID for HANA (for example, SYSTEM)

`hanaUser`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-42-then-allof-1-then-properties-parameters-properties-data-properties-hanauser.md "undefined#/properties/services/items/allOf/1/then/allOf/42/then/allOf/1/then/properties/parameters/properties/data/properties/hanaUser")

### hanaUser Type

`string`

### hanaUser Constraints

**minimum length**: the minimum number of characters for this string is: `1`
