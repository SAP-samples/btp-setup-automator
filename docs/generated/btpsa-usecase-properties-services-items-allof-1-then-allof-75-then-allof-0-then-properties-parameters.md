## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-75-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [authorities](#authorities)                                   | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-75-then-allof-0-then-properties-parameters-properties-authorities.md "undefined#/properties/services/items/allOf/1/then/allOf/75/then/allOf/0/then/properties/parameters/properties/authorities")                                   |
| [defaultCollectionQueryFilter](#defaultcollectionqueryfilter) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-75-then-allof-0-then-properties-parameters-properties-defaultcollectionqueryfilter.md "undefined#/properties/services/items/allOf/1/then/allOf/75/then/allOf/0/then/properties/parameters/properties/defaultCollectionQueryFilter") |

## authorities

Configures scopes that are available in the client credentials flow.

`authorities`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-75-then-allof-0-then-properties-parameters-properties-authorities.md "undefined#/properties/services/items/allOf/1/then/allOf/75/then/allOf/0/then/properties/parameters/properties/authorities")

### authorities Type

`string[]`

## defaultCollectionQueryFilter

Configures the default behavior of queries that return a collection of Workflow entities.

`defaultCollectionQueryFilter`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-75-then-allof-0-then-properties-parameters-properties-defaultcollectionqueryfilter.md "undefined#/properties/services/items/allOf/1/then/allOf/75/then/allOf/0/then/properties/parameters/properties/defaultCollectionQueryFilter")

### defaultCollectionQueryFilter Type

`string`

### defaultCollectionQueryFilter Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"own"`    |             |
| `"shared"` |             |
