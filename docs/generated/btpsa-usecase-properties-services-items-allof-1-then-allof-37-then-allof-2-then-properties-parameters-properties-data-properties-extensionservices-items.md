## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items.md))

# items Properties

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [enabled](#enabled)           | `boolean` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-enabled.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/enabled")           |
| [name](#name)                 | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/name")                 |
| [whitelistIPs](#whitelistips) | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-whitelistips.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/whitelistIPs") |

## enabled



`enabled`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-enabled.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/enabled")

### enabled Type

`boolean`

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/name")

### name Type

`string`

### name Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(DITenant|ConnectivityProxy)$
```

[try pattern](https://regexr.com/?expression=%5E\(DITenant%7CConnectivityProxy\)%24 "try regular expression with regexr.com")

## whitelistIPs



`whitelistIPs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-extensionservices-items-properties-whitelistips.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/extensionservices/items/properties/whitelistIPs")

### whitelistIPs Type

`string[]`

### whitelistIPs Constraints

**maximum number of items**: the maximum number of items for this array is: `250`
