## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                           | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                 |
| :--------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [engine\_version](#engine_version) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/engine_version") |
| [locale](#locale)                  | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/locale")                 |
| Additional Properties              | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                            |

## engine\_version

The major version of the PostgreSQL database to use. If not provided, the major version is defaulted to 12

`engine_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/engine_version")

### engine\_version Type

`string`

### engine\_version Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"11"` |             |
| `"12"` |             |
| `"13"` |             |

### engine\_version Default Value

The default value is:

```json
"12"
```

## locale

Indicates the locale for the instance (TODO)

`locale`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/locale")

### locale Type

`string`

### locale Default Value

The default value is:

```json
"en_US"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
