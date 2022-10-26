## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-databasemappings-items.md))

# items Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                |
| :--------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [organization\_guid](#organization_guid) | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-databasemappings-items-properties-organization_guid.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/databaseMappings/items/properties/organization_guid") |
| [space\_guid](#space_guid)               | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-databasemappings-items-properties-space_guid.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/databaseMappings/items/properties/space_guid")               |

## organization\_guid



`organization_guid`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-databasemappings-items-properties-organization_guid.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/databaseMappings/items/properties/organization_guid")

### organization\_guid Type

`string`

### organization\_guid Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-fA-F%5D%7B8%7D-\(%5B0-9a-fA-F%5D%7B4%7D-\)%7B3%7D%5B0-9a-fA-F%5D%7B12%7D%24 "try regular expression with regexr.com")

## space\_guid



`space_guid`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-37-then-allof-2-then-properties-parameters-properties-data-properties-databasemappings-items-properties-space_guid.md "undefined#/properties/services/items/allOf/1/then/allOf/37/then/allOf/2/then/properties/parameters/properties/data/properties/databaseMappings/items/properties/space_guid")

### space\_guid Type

`string`

### space\_guid Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-fA-F%5D%7B8%7D-\(%5B0-9a-fA-F%5D%7B4%7D-\)%7B3%7D%5B0-9a-fA-F%5D%7B12%7D%24 "try regular expression with regexr.com")
