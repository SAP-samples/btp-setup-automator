## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                |
| :----------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [engine\_version](#engine_version)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/redis-free-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/0/then/properties/parameters/properties/engine_version")   |
| [eviction\_policy](#eviction_policy) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-0-then-properties-parameters-properties-eviction_policy.md "http://example.com/schemas/redis-free-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/0/then/properties/parameters/properties/eviction_policy") |
| Additional Properties                | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                           |

## engine\_version

The major version number of the cache engine to be used for the clusters. If not provided, the major version is defaulted to 4.0

`engine_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/redis-free-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/0/then/properties/parameters/properties/engine_version")

### engine\_version Type

`string`

### engine\_version Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"4.0"` |             |
| `"6.0"` |             |

### engine\_version Default Value

The default value is:

```json
"4.0"
```

## eviction\_policy

The eviction policy for keys when maximum memory usage is reached. Default is 'noeviction'

`eviction_policy`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-0-then-properties-parameters-properties-eviction_policy.md "http://example.com/schemas/redis-free-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/0/then/properties/parameters/properties/eviction_policy")

### eviction\_policy Type

`string`

### eviction\_policy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"allkeys-lru"`     |             |
| `"volatile-lru"`    |             |
| `"allkeys-lfu"`     |             |
| `"volatile-lfu"`    |             |
| `"allkeys-random"`  |             |
| `"volatile-random"` |             |
| `"volatile-ttl"`    |             |
| `"noeviction"`      |             |

### eviction\_policy Default Value

The default value is:

```json
"noeviction"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
