## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                |
| :-------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [authorities](#authorities) | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-authorities.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/authorities") |
| [emname](#emname)           | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-emname.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/emname")           |
| [namespace](#namespace)     | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-namespace.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/namespace")     |
| [options](#options)         | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-options.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/options")         |
| [resources](#resources)     | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-resources.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/resources")     |
| [rules](#rules)             | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-rules.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/rules")             |
| [version](#version)         | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-version.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/version")         |
| [xs-security](#xs-security) | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/xs-security") |

## authorities



`authorities`

*   is optional

*   Type: an array where each item follows the corresponding schema in the following list:

    1.  [Untitled string in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-authorities-items-0.md "check type definition")

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-authorities.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/authorities")

### authorities Type

an array where each item follows the corresponding schema in the following list:

1.  [Untitled string in JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-authorities-items-0.md "check type definition")

## emname

It specifies the name of the message client. emname is used in the Event Mesh business application to identify message clients with ease.

`emname`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-emname.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/emname")

### emname Type

`string`

### emname Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9_-]{1,100}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9_-%5D%7B1%2C100%7D%24 "try regular expression with regexr.com")

## namespace

It ensures that every message client within a subaccount is unique. The queues managed by the message client and topics used to publish by the message client have the namespace as prefix. Exactly three (firstSegment/secondSegment/thirdSegment)

`namespace`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-namespace.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/namespace")

### namespace Type

`string`

## options

It’s used to define the privileges and access channels for a message client.

`options`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-options.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-options.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/options")

### options Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-options.md))

## resources

Resource Units is a collection of messaging resources such as queues, connections, and so on, required for a message client. You can specify this value in the service descriptor to allocate messaging resources based a specific business scenario.

`resources`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-resources.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-resources.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/resources")

### resources Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-resources.md))

## rules

It defines the publish or consume privileges for a message client.

`rules`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-rules.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-rules.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/rules")

### rules Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-rules.md))

## version

It specifies the version of the service descriptor.

`version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-version.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/version")

### version Type

`string`

### version Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^1.0.0|1.1.0$
```

[try pattern](https://regexr.com/?expression=%5E1.0.0%7C1.1.0%24 "try regular expression with regexr.com")

## xs-security

The xs-security object is used to configure XSUAA-related properties, for example, the supported credential-types for an instance. The first credential-type in the array is set as default.

`xs-security`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-xs-security.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/40/then/allOf/0/then/properties/parameters/properties/xs-security")

### xs-security Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-40-then-allof-0-then-properties-parameters-properties-xs-security.md))
