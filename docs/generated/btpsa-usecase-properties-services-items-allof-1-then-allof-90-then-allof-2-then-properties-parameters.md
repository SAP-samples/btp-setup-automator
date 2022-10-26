## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters.md))

# parameters Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cluster\_mode](#cluster_mode)                      | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-cluster_mode.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/cluster_mode")                     |
| [engine\_version](#engine_version)                  | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/engine_version")                 |
| [eviction\_policy](#eviction_policy)                | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-eviction_policy.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/eviction_policy")               |
| [maintenance\_window](#maintenance_window)          | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-maintenance_window.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/maintenance_window")         |
| [memory](#memory)                                   | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-memory.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/memory")                                 |
| [multi\_az](#multi_az)                              | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-multi_az.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/multi_az")                             |
| [node\_count](#node_count)                          | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-node_count.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/node_count")                         |
| [notify\_keyspace\_events](#notify_keyspace_events) | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-notify_keyspace_events.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/notify_keyspace_events") |
| [shard\_count](#shard_count)                        | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-shard_count.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/shard_count")                       |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                             |

## cluster\_mode

Indicates whether the instance is clustered redis deployment. If not provided, it is defaulted to true.

`cluster_mode`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-cluster_mode.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/cluster_mode")

### cluster\_mode Type

`boolean`

### cluster\_mode Default Value

The default value is:

```json
true
```

## engine\_version

The major version number of the cache engine to be used for the clusters. If not provided, the major version is defaulted to 4.0

`engine_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/engine_version")

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

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-eviction_policy.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/eviction_policy")

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

## maintenance\_window

Indicates the maintenance window for the Redis cache.

`maintenance_window`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-maintenance_window.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-maintenance_window.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/maintenance_window")

### maintenance\_window Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-maintenance_window.md))

## memory

Defines amount of memory (in GB) to be used for the instance. The number of CPU cores is also derived from the value based on the standard plan's semantics

`memory`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-memory.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/memory")

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

Indicates whether the instance is a multi-AZ deployment. If not provided, it is defaulted to true.

`multi_az`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-multi_az.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/multi_az")

### multi\_az Type

`boolean`

### multi\_az Default Value

The default value is:

```json
true
```

## node\_count

Indicates the number of nodes per shard within the Redis cluster. If not provided, it is defaulted to 3. For instances with multiple shards and nodes per shard, the number of storage SKU units deducted from available entitlements is equal to the total nodes count in the cluster.

`node_count`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-node_count.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/node_count")

### node\_count Type

`integer`

### node\_count Constraints

**maximum**: the value of this number must smaller than or equal to: `6`

**minimum**: the value of this number must greater than or equal to: `3`

### node\_count Default Value

The default value is:

```json
3
```

## notify\_keyspace\_events

Indicates the keyspace events for which notifications are enabled. If not provided, notifications are disabled.

`notify_keyspace_events`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-notify_keyspace_events.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/notify_keyspace_events")

### notify\_keyspace\_events Type

`string`

### notify\_keyspace\_events Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[KEg$lshzxeA]*$
```

[try pattern](https://regexr.com/?expression=%5E%5BKEg%24lshzxeA%5D*%24 "try regular expression with regexr.com")

## shard\_count

Indicates the number of shards within the Redis cluster. If not provided, it is defaulted to 1. For instances with multiple shards and nodes per shard, the number of storage SKU units deducted from available entitlements is equal to the total nodes count in the cluster.

`shard_count`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-90-then-allof-2-then-properties-parameters-properties-shard_count.md "http://example.com/schemas/redis-standard-create.json#/properties/services/items/allOf/1/then/allOf/90/then/allOf/2/then/properties/parameters/properties/shard_count")

### shard\_count Type

`integer`

### shard\_count Constraints

**maximum**: the value of this number must smaller than or equal to: `90`

**minimum**: the value of this number must greater than or equal to: `1`

### shard\_count Default Value

The default value is:

```json
1
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
