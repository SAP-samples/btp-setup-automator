## data Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data.md))

# data Properties

| Property                                                 | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ase\_admin\_password](#ase_admin_password)              | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-ase_admin_password.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/ase_admin_password")             |
| [backup\_interval\_hour](#backup_interval_hour)          | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup_interval_hour.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup_interval_hour")         |
| [backup\_retention\_days](#backup_retention_days)        | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup_retention_days.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup_retention_days")       |
| [character\_set](#character_set)                         | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-character_set.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/character_set")                       |
| [compute](#compute)                                      | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-compute.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/compute")                                   |
| [data\_size\_gib](#data_size_gib)                        | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-data_size_gib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/data_size_gib")                       |
| [enableAutoBackups](#enableautobackups)                  | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-enableautobackups.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/enableAutoBackups")               |
| [full\_db\_backup\_schedule](#full_db_backup_schedule)   | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-full_db_backup_schedule.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/full_db_backup_schedule")   |
| [logWriteAccelerator](#logwriteaccelerator)              | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-logwriteaccelerator.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/logWriteAccelerator")           |
| [log\_size\_gib](#log_size_gib)                          | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-log_size_gib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/log_size_gib")                         |
| [memory](#memory)                                        | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-memory.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/memory")                                     |
| [page\_size\_kib](#page_size_kib)                        | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-page_size_kib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/page_size_kib")                       |
| [serviceStopped](#servicestopped)                        | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-servicestopped.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/serviceStopped")                     |
| [sort\_order](#sort_order)                               | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-sort_order.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/sort_order")                             |
| [tran\_backup\_freq\_minutes](#tran_backup_freq_minutes) | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-tran_backup_freq_minutes.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/tran_backup_freq_minutes") |
| [versionIndicator](#versionindicator)                    | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-versionindicator.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/versionIndicator")                 |
| [whitelist\_ips](#whitelist_ips)                         | `array`   | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-whitelist_ips.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/whitelist_ips")                       |

## ase\_admin\_password

ASE DBA password

`ase_admin_password`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-ase_admin_password.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/ase_admin_password")

### ase\_admin\_password Type

`string`

### ase\_admin\_password Constraints

**minimum length**: the minimum number of characters for this string is: `8`

## backup\_interval\_hour

Cron job frequency in hours for taking the database dump

`backup_interval_hour`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup_interval_hour.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup_interval_hour")

### backup\_interval\_hour Type

`integer`

### backup\_interval\_hour Constraints

**maximum**: the value of this number must smaller than or equal to: `500`

**minimum**: the value of this number must greater than or equal to: `1`

**unknown format**: the value of this string must follow the format: `int32`

### backup\_interval\_hour Default Value

The default value is:

```json
24
```

## backup\_retention\_days

Retention Period in Days for ASE

`backup_retention_days`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup_retention_days.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup_retention_days")

### backup\_retention\_days Type

`integer`

### backup\_retention\_days Constraints

**maximum**: the value of this number must smaller than or equal to: `30`

**minimum**: the value of this number must greater than or equal to: `1`

**unknown format**: the value of this string must follow the format: `int32`

### backup\_retention\_days Default Value

The default value is:

```json
14
```

## character\_set

Character set used by ASE instance

`character_set`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-character_set.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/character_set")

### character\_set Type

`string`

### character\_set Default Value

The default value is:

```json
"utf8"
```

## compute

Number of vCPUs

`compute`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-compute.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/compute")

### compute Type

`integer`

### compute Constraints

**maximum**: the value of this number must smaller than or equal to: `60`

**minimum**: the value of this number must greater than or equal to: `2`

**unknown format**: the value of this string must follow the format: `int32`

## data\_size\_gib

Data size in GiB

`data_size_gib`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-data_size_gib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/data_size_gib")

### data\_size\_gib Type

`integer`

### data\_size\_gib Constraints

**unknown format**: the value of this string must follow the format: `int32`

## enableAutoBackups

enableAutoBackups enables/disables DB and tran backups

`enableAutoBackups`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-enableautobackups.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/enableAutoBackups")

### enableAutoBackups Type

`boolean`

### enableAutoBackups Default Value

The default value is:

```json
true
```

## full\_db\_backup\_schedule

Full Db backup schedule for ASE

`full_db_backup_schedule`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-full_db_backup_schedule.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/full_db_backup_schedule")

### full\_db\_backup\_schedule Type

`string`

### full\_db\_backup\_schedule Default Value

The default value is:

```json
"0 */24 * * *"
```

## logWriteAccelerator

Accelerated writes for log PVs

`logWriteAccelerator`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-logwriteaccelerator.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-logwriteaccelerator.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/logWriteAccelerator")

### logWriteAccelerator Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-logwriteaccelerator.md))

## log\_size\_gib

Log size in GiB

`log_size_gib`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-log_size_gib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/log_size_gib")

### log\_size\_gib Type

`integer`

### log\_size\_gib Constraints

**unknown format**: the value of this string must follow the format: `int32`

## memory

Memory size in GiB

`memory`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-memory.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/memory")

### memory Type

`integer`

### memory Constraints

**unknown format**: the value of this string must follow the format: `int32`

## page\_size\_kib

Ase server page size

`page_size_kib`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-page_size_kib.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/page_size_kib")

### page\_size\_kib Type

`string`

### page\_size\_kib Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"2k"`  |             |
| `"4k"`  |             |
| `"8k"`  |             |
| `"16k"` |             |

### page\_size\_kib Default Value

The default value is:

```json
"16k"
```

## serviceStopped

Shutdown all the computing resources associated with ASE

`serviceStopped`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-servicestopped.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/serviceStopped")

### serviceStopped Type

`boolean`

## sort\_order

Sort order for given charset

`sort_order`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-sort_order.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/sort_order")

### sort\_order Type

`string`

### sort\_order Default Value

The default value is:

```json
"binary"
```

## tran\_backup\_freq\_minutes

Transaction backup frequency for ASE

`tran_backup_freq_minutes`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-tran_backup_freq_minutes.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/tran_backup_freq_minutes")

### tran\_backup\_freq\_minutes Type

`integer`

### tran\_backup\_freq\_minutes Constraints

**maximum**: the value of this number must smaller than or equal to: `960`

**minimum**: the value of this number must greater than or equal to: `1`

**unknown format**: the value of this string must follow the format: `int32`

### tran\_backup\_freq\_minutes Default Value

The default value is:

```json
30
```

## versionIndicator

ase version to be created

`versionIndicator`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-versionindicator.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/versionIndicator")

### versionIndicator Type

`string`

## whitelist\_ips

IP address or range for whitelisting

`whitelist_ips`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-whitelist_ips.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/whitelist_ips")

### whitelist\_ips Type

`string[]`

### whitelist\_ips Constraints

**maximum number of items**: the maximum number of items for this array is: `45`
