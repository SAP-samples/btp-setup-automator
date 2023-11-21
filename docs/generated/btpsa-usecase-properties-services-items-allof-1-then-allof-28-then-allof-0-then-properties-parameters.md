## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [email](#email)            | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-email.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/email")           |
| [first\_name](#first_name) | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-first_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/first_name") |
| [host\_name](#host_name)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-host_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/host_name")   |
| [last\_name](#last_name)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-last_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/last_name")   |

## email



`email`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-email.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/email")

### email Type

`string`

### email Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## first\_name



`first_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-first_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/first_name")

### first\_name Type

`string`

### first\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## host\_name

The host name of the tenant can only contain numbers (0-9), lower case letters (a-z), and
hyphens (-). The same host name can't be reused to create other instances.

`host_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-host_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/host_name")

### host\_name Type

`string`

### host\_name Constraints

**maximum length**: the maximum number of characters for this string is: `100`

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z0-9-]*$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z0-9-%5D*%24 "try regular expression with regexr.com")

## last\_name



`last_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-28-then-allof-0-then-properties-parameters-properties-last_name.md "undefined#/properties/services/items/allOf/1/then/allOf/28/then/allOf/0/then/properties/parameters/properties/last_name")

### last\_name Type

`string`

### last\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`
