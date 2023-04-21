## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-2-then-allof-46-then-allof-1-then-properties-parameters.md))

# parameters Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                   |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cloud\_service](#cloud_service) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-2-then-allof-46-then-allof-1-then-properties-parameters-properties-service-type.md "undefined#/properties/services/items/allOf/2/then/allOf/46/then/allOf/1/then/properties/parameters/properties/cloud_service") |
| Additional Properties            | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                              |

## cloud\_service

Choose a productive or test service type from the drop down.

`cloud_service`

*   is optional

*   Type: `string` ([Service type](btpsa-usecase-properties-services-items-allof-2-then-allof-46-then-allof-1-then-properties-parameters-properties-service-type.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-2-then-allof-46-then-allof-1-then-properties-parameters-properties-service-type.md "undefined#/properties/services/items/allOf/2/then/allOf/46/then/allOf/1/then/properties/parameters/properties/cloud_service")

### cloud\_service Type

`string` ([Service type](btpsa-usecase-properties-services-items-allof-2-then-allof-46-then-allof-1-then-properties-parameters-properties-service-type.md))

### cloud\_service Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"PRODUCTIVE"` |             |
| `"TEST"`       |             |

### cloud\_service Default Value

The default value is:

```json
"PRODUCTIVE"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
