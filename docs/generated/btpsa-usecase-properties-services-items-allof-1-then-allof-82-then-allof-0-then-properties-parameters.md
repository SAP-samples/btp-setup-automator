## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                       |
| :-------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cosmosDb](#cosmosdb)             | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/cosmosDb") |
| [requestMessage](#requestmessage) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-request-message.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/requestMessage")                 |
| [resourceId](#resourceid)         | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-resource-id.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/resourceId")                         |
| [subResource](#subresource)       | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-subresource.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/subResource")                        |

## cosmosDb

Specifies CosmosDB-specific creation parameters.

`cosmosDb`

*   is optional

*   Type: `object` ([CosmosDB-specific creation parameters](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/cosmosDb")

### cosmosDb Type

`object` ([CosmosDB-specific creation parameters](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-cosmosdb-specific-creation-parameters.md))

## requestMessage

Specifies the request message which is displayed to the approver.

`requestMessage`

*   is optional

*   Type: `string` ([Request Message](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-request-message.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-request-message.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/requestMessage")

### requestMessage Type

`string` ([Request Message](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-request-message.md))

### requestMessage Constraints

**maximum length**: the maximum number of characters for this string is: `60`

## resourceId

Specifies the Azure Resource ID of the service for which the private endpoint should be created.

Example: /subscriptions/<subscription>/resourceGroups/<rg>/providers/Microsoft.Network/privateLinkServices/<myPrivateLinkService>

`resourceId`

*   is required

*   Type: `string` ([Resource ID](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-resource-id.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-resource-id.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/resourceId")

### resourceId Type

`string` ([Resource ID](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-resource-id.md))

### resourceId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
/subscriptions/.+/resourceGroups/.+/providers/.+?/.+?/[^/#?]+
```

[try pattern](https://regexr.com/?expression=%2Fsubscriptions%2F.%2B%2FresourceGroups%2F.%2B%2Fproviders%2F.%2B%3F%2F.%2B%3F%2F%5B%5E%2F%23%3F%5D%2B "try regular expression with regexr.com")

## subResource

Specifies the subresource for a specific Resource ID. Note that subresource is not required for Azure Private Link resources.

Example: mysqlServer

All supported native Azure services including subresources can be found here: <https://help.sap.com/viewer/product/PRIVATE_LINK/CLOUD/en-US>

`subResource`

*   is optional

*   Type: `string` ([Subresource](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-subresource.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-subresource.md "undefined#/properties/services/items/allOf/1/then/allOf/82/then/allOf/0/then/properties/parameters/properties/subResource")

### subResource Type

`string` ([Subresource](btpsa-usecase-properties-services-items-allof-1-then-allof-82-then-allof-0-then-properties-parameters-properties-subresource.md))
