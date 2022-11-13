## 0 Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0.md))

# 0 Properties

| Property                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [addon\_product\_name](#addon_product_name)       | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-addon_product_name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/addon_product_name")       |
| [addon\_product\_version](#addon_product_version) | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-addon_product_version.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/addon_product_version") |
| [consumer\_id\_pattern](#consumer_id_pattern)     | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-consumer_id_pattern.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/consumer_id_pattern")     |
| [consumer\_tenant\_limit](#consumer_tenant_limit) | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-consumer_tenant_limit.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/consumer_tenant_limit") |
| [name](#name)                                     | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/name")                                   |
| [provider\_admin\_email](#provider_admin_email)   | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-provider_admin_email.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/provider_admin_email")   |
| [sap\_system\_name](#sap_system_name)             | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-sap_system_name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/sap_system_name")             |
| [size\_of\_persistence](#size_of_persistence)     | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-size_of_persistence.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/size_of_persistence")     |
| [size\_of\_runtime](#size_of_runtime)             | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-size_of_runtime.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/size_of_runtime")             |
| [tenant\_mode](#tenant_mode)                      | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-tenant_mode.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/tenant_mode")                     |
| [usage](#usage)                                   | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-usage.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/usage")                                 |
| [xs-security](#xs-security)                       | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/xs-security")                     |

## addon\_product\_name

Registered name of the addon product. Will be passed through to ABAP OEM Plan

`addon_product_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-addon_product_name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/addon_product_name")

### addon\_product\_name Type

`string`

## addon\_product\_version

Version of the addon product that should be installed. Will be passed through to ABAP OEM Plan

`addon_product_version`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-addon_product_version.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/addon_product_version")

### addon\_product\_version Type

`string`

## consumer\_id\_pattern

String containing a regular expression with a capturing group. The subdomain of the consumer is matched against this regular expression. The value of the first capturing group is used as consumer id.

`consumer_id_pattern`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-consumer_id_pattern.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/consumer_id_pattern")

### consumer\_id\_pattern Type

`string`

## consumer\_tenant\_limit

Maximum number of tenants in ABAP System

`consumer_tenant_limit`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-consumer_tenant_limit.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/consumer_tenant_limit")

### consumer\_tenant\_limit Type

`integer`

### consumer\_tenant\_limit Constraints

**maximum**: the value of this number must smaller than or equal to: `800`

**minimum**: the value of this number must greater than or equal to: `1`

### consumer\_tenant\_limit Default Value

The default value is:

```json
1
```

## name

Name of the solution

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/name")

### name Type

`string`

## provider\_admin\_email

Email address of initial provider user. Will be passed through to ABAP OEM Plan

`provider_admin_email`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-provider_admin_email.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/provider_admin_email")

### provider\_admin\_email Type

`string`

### provider\_admin\_email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## sap\_system\_name

Name of the SAP system

`sap_system_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-sap_system_name.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/sap_system_name")

### sap\_system\_name Type

`string`

### sap\_system\_name Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
(^$)|(^(?!ADD|ALL|AMD|AND|ANY|ARE|ASC|AUX|AVG|BIT|CDC|COM|CON|DBA|END|EPS|FOR|GET|GID|IBM|INT|KEY|LOG|LPT|MAP|MAX|MIN|MON|NIX|NOT|NUL|OFF|OLD|OMS|OUT|PAD|PRN|RAW|REF|ROW|SAP|SET|SGA|SHG|SID|SQL|SUM|SYS|TMP|TOP|UID|USE|USR|VAR)[A-Z][A-Z0-9]{2}$)
```

[try pattern](https://regexr.com/?expression=\(%5E%24\)%7C\(%5E\(%3F!ADD%7CALL%7CAMD%7CAND%7CANY%7CARE%7CASC%7CAUX%7CAVG%7CBIT%7CCDC%7CCOM%7CCON%7CDBA%7CEND%7CEPS%7CFOR%7CGET%7CGID%7CIBM%7CINT%7CKEY%7CLOG%7CLPT%7CMAP%7CMAX%7CMIN%7CMON%7CNIX%7CNOT%7CNUL%7COFF%7COLD%7COMS%7COUT%7CPAD%7CPRN%7CRAW%7CREF%7CROW%7CSAP%7CSET%7CSGA%7CSHG%7CSID%7CSQL%7CSUM%7CSYS%7CTMP%7CTOP%7CUID%7CUSE%7CUSR%7CVAR\)%5BA-Z%5D%5BA-Z0-9%5D%7B2%7D%24\) "try regular expression with regexr.com")

## size\_of\_persistence

Default size of the ABAP system (in blocks of the size 16 GB). Will be passed through to ABAP OEM Plan

`size_of_persistence`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-size_of_persistence.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/size_of_persistence")

### size\_of\_persistence Type

`integer`

### size\_of\_persistence Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `4`   |             |
| `8`   |             |
| `16`  |             |
| `32`  |             |
| `64`  |             |

### size\_of\_persistence Default Value

The default value is:

```json
4
```

## size\_of\_runtime

Default size of the HANA database (in blocks of the size 16 GB) of the ABAP System. Will be passed through to ABAP OEM Plan

`size_of_runtime`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-size_of_runtime.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/size_of_runtime")

### size\_of\_runtime Type

`integer`

### size\_of\_runtime Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `1`   |             |
| `2`   |             |
| `4`   |             |
| `6`   |             |
| `8`   |             |

### size\_of\_runtime Default Value

The default value is:

```json
1
```

## tenant\_mode

Decides whether a customer will have a tenant in a dedicated system (single) or a shared system (multi)

`tenant_mode`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-tenant_mode.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/tenant_mode")

### tenant\_mode Type

`string`

### tenant\_mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"single"` |             |
| `"multi"`  |             |

## usage

Whether it is a test or productive solution

`usage`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-usage.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/usage")

### usage Type

`string`

### usage Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"test"` |             |
| `"prod"` |             |

## xs-security



`xs-security`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-xs-security.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-xs-security.md "undefined#/properties/services/items/allOf/1/then/allOf/1/then/allOf/0/then/properties/parameters/oneOf/0/properties/xs-security")

### xs-security Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-1-then-allof-0-then-properties-parameters-oneof-0-properties-xs-security.md))
