## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                           | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                 |
| :--------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [allow\_access](#allow_access)     | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-allow_access.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/allow_access")     |
| [engine\_version](#engine_version) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/engine_version") |
| [locale](#locale)                  | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/locale")                 |
| [region](#region)                  | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-region.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/region")                 |
| Additional Properties              | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                            |

## allow\_access

Comma separated list of IPs and CF landscape domains from which connectivity to the instance can be established. Default behaviour will be to block all access to the instance from any public IP or CF Domain.

`allow_access`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-allow_access.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/allow_access")

### allow\_access Type

`string`

## engine\_version

The major version of the PostgreSQL database to use. If not provided, the major version is defaulted to 12

`engine_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-engine_version.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/engine_version")

### engine\_version Type

`string`

### engine\_version Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"11"` |             |
| `"12"` |             |
| `"13"` |             |
| `"14"` |             |

### engine\_version Default Value

The default value is:

```json
"12"
```

## locale

Indicates the locale for the instance (TODO)

`locale`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-locale.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/locale")

### locale Type

`string`

### locale Default Value

The default value is:

```json
"en_US"
```

## region

The infrastructure region where the instance will be deployed.

`region`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-84-then-allof-0-then-properties-parameters-properties-region.md "http://example.com/schemas/postgres-free-create.json#/properties/services/items/allOf/1/then/allOf/84/then/allOf/0/then/properties/parameters/properties/region")

### region Type

`string`

### region Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"ap-northeast-1"` |             |
| `"ap-northeast-2"` |             |
| `"ap-northeast-3"` |             |
| `"ap-south-1"`     |             |
| `"ap-southeast-1"` |             |
| `"ap-southeast-2"` |             |
| `"ca-central-1"`   |             |
| `"eu-central-1"`   |             |
| `"eu-north-1"`     |             |
| `"eu-west-1"`      |             |
| `"eu-west-2"`      |             |
| `"eu-west-3"`      |             |
| `"sa-east-1"`      |             |
| `"us-east-1"`      |             |
| `"us-east-2"`      |             |
| `"us-west-1"`      |             |
| `"us-west-2"`      |             |

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
