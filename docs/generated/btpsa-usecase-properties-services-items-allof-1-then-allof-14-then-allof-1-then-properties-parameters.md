## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters.md))

# parameters Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                    |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [documentation](#documentation) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-documentation.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/documentation") |
| [instructions](#instructions)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-instructions.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/instructions")   |
| [type](#type)                   | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-type.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/type")                   |

## documentation



`documentation`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-documentation.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/documentation")

### documentation Type

`string`

### documentation Default Value

The default value is:

```json
"https://help.sap.com/viewer/p/BLOCKCHAIN_APPLICATION_ENABLEMENT"
```

## instructions



`instructions`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-instructions.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/instructions")

### instructions Type

`string`

### instructions Default Value

The default value is:

```json
"Replace this JSON object with the SERVICE KEY for the blockchain technology to which this service must bind."
```

## type

Used blockchain technology (hyperledger-fabric|multichain|quorum)

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-14-then-allof-1-then-properties-parameters-properties-type.md "undefined#/properties/services/items/allOf/1/then/allOf/14/then/allOf/1/then/properties/parameters/properties/type")

### type Type

`string`

### type Default Value

The default value is:

```json
"< Used blockchain technology (hyperledger-fabric|multichain|quorum) >"
```
