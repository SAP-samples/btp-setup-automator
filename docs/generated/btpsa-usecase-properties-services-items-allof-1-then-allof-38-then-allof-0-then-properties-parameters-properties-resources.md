## resources Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-38-then-allof-0-then-properties-parameters-properties-resources.md))

# resources Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                              |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [units](#units) | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-38-then-allof-0-then-properties-parameters-properties-resources-properties-units.md "undefined#/properties/services/items/allOf/1/then/allOf/38/then/allOf/0/then/properties/parameters/properties/resources/properties/units") |

## units



`units`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-38-then-allof-0-then-properties-parameters-properties-resources-properties-units.md "undefined#/properties/services/items/allOf/1/then/allOf/38/then/allOf/0/then/properties/parameters/properties/resources/properties/units")

### units Type

`string`

### units Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([1-9][0-9]?[0-9]?[0-9])$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B1-9%5D%5B0-9%5D%3F%5B0-9%5D%3F%5B0-9%5D\)%24 "try regular expression with regexr.com")

### units Default Value

The default value is:

```json
"10"
```
