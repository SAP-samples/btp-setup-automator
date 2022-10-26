## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters.md))

# parameters Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [channelId](#channelid)         | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-channelid.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/channelId")         |
| [channelSecret](#channelsecret) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-channelsecret.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/channelSecret") |
| [comment](#comment)             | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-comment.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/comment")             |

## channelId

Reverse DNS id of the channel to configure the service instance for.

`channelId`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-channelid.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/channelId")

### channelId Type

`string`

### channelId Default Value

The default value is:

```json
"< the channel that should be imported >"
```

## channelSecret

Secret to map the new channel service instance to the corresponding hyperledger channel

`channelSecret`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-channelsecret.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/channelSecret")

### channelSecret Type

`string`

### channelSecret Default Value

The default value is:

```json
"< the channel secret >"
```

## comment

Comment that describes the created channel service instance.

`comment`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-1-then-properties-parameters-properties-comment.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/1/then/properties/parameters/properties/comment")

### comment Type

`string`

### comment Default Value

The default value is:

```json
"< user defined comment >"
```
