## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-roles-items.md))

# items Properties

| Property                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)             | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-roles-items-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/roles/items/properties/name")             |
| [privileges](#privileges) | `array`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-roles-items-properties-privileges.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/roles/items/properties/privileges") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-roles-items-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/roles/items/properties/name")

### name Type

`string`

### name Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z0-9]{1}[a-z0-9-]{0,14}[a-z0-9]{1}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z0-9%5D%7B1%7D%5Ba-z0-9-%5D%7B0%2C14%7D%5Ba-z0-9%5D%7B1%7D%24 "try regular expression with regexr.com")

## privileges



`privileges`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-roles-items-properties-privileges.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/roles/items/properties/privileges")

### privileges Type

`string[]`
