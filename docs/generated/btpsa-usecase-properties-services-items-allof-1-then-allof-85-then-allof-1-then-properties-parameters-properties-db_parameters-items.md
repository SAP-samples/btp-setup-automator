## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-85-then-allof-1-then-properties-parameters-properties-db_parameters-items.md))

# items Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-85-then-allof-1-then-properties-parameters-properties-db_parameters-items-properties-name.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/85/then/allOf/1/then/properties/parameters/properties/db_parameters/items/properties/name")   |
| [value](#value) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-85-then-allof-1-then-properties-parameters-properties-db_parameters-items-properties-value.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/85/then/allOf/1/then/properties/parameters/properties/db_parameters/items/properties/value") |

## name

Name of the system configuration

`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-85-then-allof-1-then-properties-parameters-properties-db_parameters-items-properties-name.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/85/then/allOf/1/then/properties/parameters/properties/db_parameters/items/properties/name")

### name Type

`string`

### name Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                              | Explanation |
| :--------------------------------- | :---------- |
| `"max_wal_size"`                   |             |
| `"checkpoint_timeout"`             |             |
| `"autovacuum_max_workers"`         |             |
| `"autovacuum_vacuum_scale_factor"` |             |
| `"max_locks_per_transaction"`      |             |

## value

Value of the system configuration

`value`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-85-then-allof-1-then-properties-parameters-properties-db_parameters-items-properties-value.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/85/then/allOf/1/then/properties/parameters/properties/db_parameters/items/properties/value")

### value Type

`string`
