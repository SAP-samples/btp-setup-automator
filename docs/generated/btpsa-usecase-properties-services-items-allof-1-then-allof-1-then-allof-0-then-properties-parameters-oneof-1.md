## 1 Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1.md))

# 1 Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [consumer\_id\_pattern](#consumer_id_pattern) | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-consumer_id_pattern.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/consumer_id_pattern") |
| [name](#name)                                 | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/name")                               |
| [plans](#plans)                               | `array`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-plans.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/plans")                             |
| [xs-security](#xs-security)                   | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/xs-security")                 |

## consumer\_id\_pattern

String containing a regular expression with a capturing group. The subdomain of the consumer is matched against this regular expression. The value of the first capturing group is used as consumer id.

`consumer_id_pattern`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-consumer_id_pattern.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/consumer_id_pattern")

### consumer\_id\_pattern Type

`string`

## name

Name of the solution

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/name")

### name Type

`string`

## plans



`plans`

*   is required

*   Type: `object[]` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-plans-items.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-plans.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/plans")

### plans Type

`object[]` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-plans-items.md))

### plans Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## xs-security



`xs-security`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-xs-security.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/1/properties/xs-security")

### xs-security Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-1-properties-xs-security.md))
