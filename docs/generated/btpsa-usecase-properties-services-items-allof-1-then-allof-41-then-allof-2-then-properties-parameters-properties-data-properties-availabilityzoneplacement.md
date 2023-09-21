## availabilityZonePlacement Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement.md))

# availabilityZonePlacement Properties

| Property                                                                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [highAvailabilityCrossMultiAZEnabled](#highavailabilitycrossmultiazenabled) | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-highavailabilitycrossmultiazenabled.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/highAvailabilityCrossMultiAZEnabled") |
| [initialReplicaAvailabilityZone](#initialreplicaavailabilityzone)           | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-initialreplicaavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/initialReplicaAvailabilityZone")           |
| [initialSourceAvailabilityZone](#initialsourceavailabilityzone)             | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-initialsourceavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/initialSourceAvailabilityZone")             |
| [primaryAvailabilityZone](#primaryavailabilityzone)                         | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-primaryavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/primaryAvailabilityZone")                         |
| [secondaryAvailabilityZone](#secondaryavailabilityzone)                     | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-secondaryavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/secondaryAvailabilityZone")                     |

## highAvailabilityCrossMultiAZEnabled

A flag to determine if the HA setup will be cross multi-availability zones or not

`highAvailabilityCrossMultiAZEnabled`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-highavailabilitycrossmultiazenabled.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/highAvailabilityCrossMultiAZEnabled")

### highAvailabilityCrossMultiAZEnabled Type

`boolean`

## initialReplicaAvailabilityZone

This zone will be used by the initial replica

`initialReplicaAvailabilityZone`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-initialreplicaavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/initialReplicaAvailabilityZone")

### initialReplicaAvailabilityZone Type

`string`

## initialSourceAvailabilityZone

This zone will be used by the initial source

`initialSourceAvailabilityZone`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-initialsourceavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/initialSourceAvailabilityZone")

### initialSourceAvailabilityZone Type

`string`

## primaryAvailabilityZone

This zone will be used by the primary instance

`primaryAvailabilityZone`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-primaryavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/primaryAvailabilityZone")

### primaryAvailabilityZone Type

`string`

## secondaryAvailabilityZone

This zone will be used by the secondary instance, if defined in .disasterRecoveryMode

`secondaryAvailabilityZone`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-data-properties-availabilityzoneplacement-properties-secondaryavailabilityzone.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/data/properties/availabilityZonePlacement/properties/secondaryAvailabilityZone")

### secondaryAvailabilityZone Type

`string`
