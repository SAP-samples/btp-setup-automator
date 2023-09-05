## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [grant-types](#grant-types)       | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-grant-types.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/grant-types")                         |
| [redirect-uris](#redirect-uris)   | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-redirect-uris.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/redirect-uris")                     |
| [roles](#roles)                   | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-roles.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/roles")                                     |
| [token-validity](#token-validity) | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-access-token-validity-in-seconds.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/token-validity") |

## grant-types

Grant-types related to the service instance

`grant-types`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-grant-types.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/grant-types")

### grant-types Type

`string[]`

### grant-types Constraints

**minimum number of items**: the minimum number of items for this array is: `0`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### grant-types Default Value

The default value is:

```json
[
  "client_credentials"
]
```

## redirect-uris

Redirect-Uris for authorization code grant-type

`redirect-uris`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-redirect-uris.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/redirect-uris")

### redirect-uris Type

`string[]`

### redirect-uris Constraints

**minimum number of items**: the minimum number of items for this array is: `0`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### redirect-uris Default Value

The default value is:

```json
[]
```

## roles

Roles granted to the service instance. For details please check <https://help.sap.com/viewer/368c481cd6954bdfa5d0435479fd4eaf/Cloud/en-US/556d5575d4b0483e85d4f3251f21d0ec.html>

`roles`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-roles.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/roles")

### roles Type

`string[]`

### roles Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## token-validity

Defines the validity of the access token

`token-validity`

*   is optional

*   Type: `integer` ([Access Token Validity (in seconds)](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-access-token-validity-in-seconds.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-access-token-validity-in-seconds.md "undefined#/properties/services/items/allOf/1/then/allOf/55/then/allOf/0/then/properties/parameters/properties/token-validity")

### token-validity Type

`integer` ([Access Token Validity (in seconds)](btpsa-usecase-properties-services-items-allof-1-then-allof-55-then-allof-0-then-properties-parameters-properties-access-token-validity-in-seconds.md))

### token-validity Constraints

**maximum**: the value of this number must smaller than or equal to: `86400`

**minimum**: the value of this number must greater than or equal to: `3600`

### token-validity Default Value

The default value is:

```json
43200
```
