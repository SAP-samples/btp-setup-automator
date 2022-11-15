## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-21-then-allof-1-then-properties-parameters.md))

# parameters Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [grantType](#granttype) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-21-then-allof-1-then-properties-parameters-properties-authorization-type.md "undefined#/properties/services/items/allOf/1/then/allOf/21/then/allOf/1/then/properties/parameters/properties/grantType") |
| Additional Properties   | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                |

## grantType

Use the Password grant type for Cloud Foundry and Password, or Client Credentials grant type for Other Environments.

`grantType`

*   is optional

*   Type: `string` ([Authorization Type](btpsa-usecase-properties-services-items-allof-1-then-allof-21-then-allof-1-then-properties-parameters-properties-authorization-type.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-21-then-allof-1-then-properties-parameters-properties-authorization-type.md "undefined#/properties/services/items/allOf/1/then/allOf/21/then/allOf/1/then/properties/parameters/properties/grantType")

### grantType Type

`string` ([Authorization Type](btpsa-usecase-properties-services-items-allof-1-then-allof-21-then-allof-1-then-properties-parameters-properties-authorization-type.md))

### grantType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"password"`          |             |
| `"clientCredentials"` |             |

### grantType Default Value

The default value is:

```json
"password"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
