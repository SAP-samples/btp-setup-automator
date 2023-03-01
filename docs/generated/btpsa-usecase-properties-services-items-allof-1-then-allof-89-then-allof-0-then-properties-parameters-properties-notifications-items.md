## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-89-then-allof-0-then-properties-parameters-properties-notifications-items.md))

# items Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [destinationName](#destinationname) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-89-then-allof-0-then-properties-parameters-properties-notifications-items-properties-destinationname.md "undefined#/properties/services/items/allOf/1/then/allOf/89/then/allOf/0/then/properties/parameters/properties/notifications/items/properties/destinationName") |
| [usage](#usage)                     | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-89-then-allof-0-then-properties-parameters-properties-notifications-items-properties-usage.md "undefined#/properties/services/items/allOf/1/then/allOf/89/then/allOf/0/then/properties/parameters/properties/notifications/items/properties/usage")                     |

## destinationName



`destinationName`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-89-then-allof-0-then-properties-parameters-properties-notifications-items-properties-destinationname.md "undefined#/properties/services/items/allOf/1/then/allOf/89/then/allOf/0/then/properties/parameters/properties/notifications/items/properties/destinationName")

### destinationName Type

`string`

### destinationName Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[\w-]{0,200}$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5Cw-%5D%7B0%2C200%7D%24 "try regular expression with regexr.com")

## usage



`usage`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-89-then-allof-0-then-properties-parameters-properties-notifications-items-properties-usage.md "undefined#/properties/services/items/allOf/1/then/allOf/89/then/allOf/0/then/properties/parameters/properties/notifications/items/properties/usage")

### usage Type

`string`

### usage Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"OMS"` |             |
| `"ISN"` |             |
| `""`    |             |
