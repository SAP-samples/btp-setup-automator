## backup Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup.md))

# backup Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [retentionDays](#retentiondays) | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup-properties-retentiondays.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup/properties/retentionDays") |

## retentionDays

Specifies the retention period for a backup in days

`retentionDays`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-0-then-properties-parameters-properties-data-properties-backup-properties-retentiondays.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/0/then/properties/parameters/properties/data/properties/backup/properties/retentionDays")

### retentionDays Type

`integer`

### retentionDays Constraints

**maximum**: the value of this number must smaller than or equal to: `215`

**minimum**: the value of this number must greater than or equal to: `0`

**unknown format**: the value of this string must follow the format: `int32`
