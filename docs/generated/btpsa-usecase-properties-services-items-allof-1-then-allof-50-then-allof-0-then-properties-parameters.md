## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                        | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :------------------------------ | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [grant-types](#grant-types)     | `array` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-grant-types.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/grant-types")     |
| [redirect-uris](#redirect-uris) | `array` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-redirect-uris.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/redirect-uris") |
| [roles](#roles)                 | `array` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-roles.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/roles")                 |

## grant-types

Grant-types related to the service instance

`grant-types`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-grant-types.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/grant-types")

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

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-redirect-uris.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/redirect-uris")

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

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-50-then-allof-0-then-properties-parameters-properties-roles.md "undefined#/properties/services/items/allOf/1/then/allOf/50/then/allOf/0/then/properties/parameters/properties/roles")

### roles Type

`string[]`

### roles Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
