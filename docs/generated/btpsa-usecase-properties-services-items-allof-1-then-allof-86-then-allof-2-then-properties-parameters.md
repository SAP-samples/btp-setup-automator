## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters.md))

# parameters Properties

| Property                                   | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                             |
| :----------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [audit\_log\_level](#audit_log_level)      | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-audit_log_level.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/audit_log_level")       |
| [engine\_version](#engine_version)         | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/engine_version")         |
| [locale](#locale)                          | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/locale")                         |
| [maintenance\_window](#maintenance_window) | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-maintenance_window.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/maintenance_window") |
| [memory](#memory)                          | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-memory.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/memory")                         |
| [multi\_az](#multi_az)                     | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-multi_az.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/multi_az")                     |
| [storage](#storage)                        | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-storage.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/storage")                       |
| Additional Properties                      | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                        |

## audit\_log\_level

Defines which classes of statements will be logged by session audit logging

`audit_log_level`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-audit_log_level.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/audit_log_level")

### audit\_log\_level Type

`string[]`

### audit\_log\_level Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### audit\_log\_level Default Value

The default value is:

```json
[
  "ROLE",
  "DDL"
]
```

## engine\_version

The major version of the PostgreSQL database to use. If not provided, the major version is defaulted to 12

`engine_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/engine_version")

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

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/locale")

### locale Type

`string`

### locale Default Value

The default value is:

```json
"en_US"
```

## maintenance\_window

Indicates the preferred maintenance window for the PostgreSQL database instance. The 30-minute maintenance window is selected at random from the specified block of time.

`maintenance_window`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-maintenance_window.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-maintenance_window.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/maintenance_window")

### maintenance\_window Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-maintenance_window.md))

## memory

Defines amount of memory (in GB) to be used for the instance. The number of CPU cores is also derived from the value based on the standard plan's semantics

`memory`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-memory.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/memory")

### memory Type

`integer`

### memory Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `2`   |             |
| `4`   |             |

### memory Default Value

The default value is:

```json
2
```

## multi\_az

Indicates whether the instance is a multi-AZ deployment. If not provided, it is defaulted to true. For a multi-AZ instance, twice the number of storage SKU units are deducted from available entitlements

`multi_az`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-multi_az.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/multi_az")

### multi\_az Type

`boolean`

### multi\_az Default Value

The default value is:

```json
true
```

## storage

Amount of storage in GB to be allocated to the instance

`storage`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-2-then-properties-parameters-properties-storage.md "http://example.com/schemas/postgres-standard-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/2/then/properties/parameters/properties/storage")

### storage Type

`integer`

### storage Default Value

The default value is:

```json
5
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
