## cosmosDb Type

`object` ([CosmosDB-specific creation parameters](btpsa-usecase-properties-services-items-allof-1-then-allof-88-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters.md))

# cosmosDb Properties

| Property             | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------- | :------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [regions:](#regions) | `array` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-88-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters-properties-cosmosdb-geo-replication-regions.md "undefined#/properties/services/items/allOf/1/then/allOf/88/then/allOf/0/then/properties/parameters/properties/cosmosDb/properties/regions:") |

## regions:

Specifies the regions a CosmosDB instance is geo-replicated in to enable Private Endpoint connections to them.

`regions:`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-88-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters-properties-cosmosdb-geo-replication-regions.md "undefined#/properties/services/items/allOf/1/then/allOf/88/then/allOf/0/then/properties/parameters/properties/cosmosDb/properties/regions:")

### regions: Type

`string[]`

### regions: Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
