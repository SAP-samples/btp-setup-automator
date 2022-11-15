## maintenance\_window Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window.md))

# maintenance\_window Properties

| Property                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                |
| :---------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [day\_of\_week](#day_of_week)       | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-day_of_week.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/day_of_week")       |
| [duration](#duration)               | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-duration.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/duration")             |
| [start\_hour\_utc](#start_hour_utc) | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-start_hour_utc.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/start_hour_utc") |

## day\_of\_week

Day of the week when the PostgreSQL database instance can be patched.

`day_of_week`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-day_of_week.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/day_of_week")

### day\_of\_week Type

`string`

### day\_of\_week Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"Monday"`    |             |
| `"Tuesday"`   |             |
| `"Wednesday"` |             |
| `"Thursday"`  |             |
| `"Friday"`    |             |
| `"Saturday"`  |             |
| `"Sunday"`    |             |

### day\_of\_week Default Value

The default value is:

```json
"Sunday"
```

## duration

Duration of the time block in hours.

`duration`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-duration.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/duration")

### duration Type

`integer`

### duration Constraints

**maximum**: the value of this number must smaller than or equal to: `23`

**minimum**: the value of this number must greater than or equal to: `1`

### duration Default Value

The default value is:

```json
1
```

## start\_hour\_utc

Start hour of the time block (in UTC).

`start_hour_utc`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-1-then-properties-parameters-properties-maintenance_window-properties-start_hour_utc.md "http://example.com/schemas/postgres-premium-create.json#/properties/services/items/allOf/1/then/allOf/86/then/allOf/1/then/properties/parameters/properties/maintenance_window/properties/start_hour_utc")

### start\_hour\_utc Type

`integer`

### start\_hour\_utc Constraints

**maximum**: the value of this number must smaller than or equal to: `23`

**minimum**: the value of this number must greater than or equal to: `0`

### start\_hour\_utc Default Value

The default value is:

```json
4
```
