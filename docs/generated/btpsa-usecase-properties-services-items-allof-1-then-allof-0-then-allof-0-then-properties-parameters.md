## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [admin\_email](#admin_email)                        | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-email-address.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/admin_email")           |
| [admin\_user\_name](#admin_user_name)               | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-user-name.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/admin_user_name")           |
| [description](#description)                         | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-description.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/description")       |
| [is\_development\_allowed](#is_development_allowed) | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-development-system.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/is_development_allowed") |
| [login\_attribute](#login_attribute)                | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-login-attribute.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/login_attribute")           |
| [sapsystemname](#sapsystemname)                     | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/sapsystemname")              |
| [size\_of\_persistence](#size_of_persistence)       | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-hana-memory-size.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/size_of_persistence")      |
| [size\_of\_runtime](#size_of_runtime)               | `integer` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-runtime-size.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/size_of_runtime")         |

## admin\_email

Enter the administrator's email address

`admin_email`

*   is required

*   Type: `string` ([Admin Email Address](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-email-address.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-email-address.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/admin_email")

### admin\_email Type

`string` ([Admin Email Address](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-email-address.md))

### admin\_email Constraints

**maximum length**: the maximum number of characters for this string is: `256`

**minimum length**: the minimum number of characters for this string is: `6`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>()\[\]\\,;:\s@"`]+@([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E\(\)%5C%5B%5C%5D%5C%5C%2C%3B%3A%5Cs%40%22%60%5D%2B%40\(%5Ba-zA-Z%5C-0-9%5D%2B%5C.\)%2B%5Ba-zA-Z%5D%7B2%2C%7D%24 "try regular expression with regexr.com")

## admin\_user\_name

Optionally enter the username of the administrator. The username must not begin with SAP\_ or \_, must only contain uppercase letters, digits, underscores, hyphens and periods, and must not be longer than 40 characters.

`admin_user_name`

*   is optional

*   Type: `string` ([Admin User Name](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-user-name.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-user-name.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/admin_user_name")

### admin\_user\_name Type

`string` ([Admin User Name](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-user-name.md))

### admin\_user\_name Constraints

**maximum length**: the maximum number of characters for this string is: `40`

**minimum length**: the minimum number of characters for this string is: `0`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?!SAP_|_)[\.A-Z0-9_-]{0,40}$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F!SAP_%7C_\)%5B%5C.A-Z0-9_-%5D%7B0%2C40%7D%24 "try regular expression with regexr.com")

## description

Enter a description for the ABAP system

`description`

*   is optional

*   Type: `string` ([ABAP System Description](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-description.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-description.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/description")

### description Type

`string` ([ABAP System Description](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-description.md))

### description Constraints

**maximum length**: the maximum number of characters for this string is: `256`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^'\x00-\x1f]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E'%5Cx00-%5Cx1f%5D*%24 "try regular expression with regexr.com")

## is\_development\_allowed

Specify, if development shall be allowed on this ABAP system

`is_development_allowed`

*   is optional

*   Type: `boolean` ([Development System](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-development-system.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-development-system.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/is_development_allowed")

### is\_development\_allowed Type

`boolean` ([Development System](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-development-system.md))

### is\_development\_allowed Default Value

The default value is:

```json
true
```

## login\_attribute

Which attribute should be used for login.

`login_attribute`

*   is optional

*   Type: `string` ([Login Attribute](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-login-attribute.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-login-attribute.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/login_attribute")

### login\_attribute Type

`string` ([Login Attribute](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-login-attribute.md))

### login\_attribute Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"email"`     |             |
| `"user_name"` |             |

### login\_attribute Default Value

The default value is:

```json
"email"
```

## sapsystemname

Enter a valid system ID (SID) for the ABAP system. The ID must consist of exactly three alphanumeric characters. Only uppercase letters are allowed. The first character must be a letter (not a digit). The ID does not have to be technically unique. The following IDs are reserved and cannot be used: ADD ALL AMD AND ANY ARE ASC AUX AVG BIT CDC COM CON DBA END EPS FOR GET GID IBM INT KEY LOG LPT MAP MAX MIN MON NIX NOT NUL OFF OLD OMS OUT PAD PRN RAW REF ROW SAP SET SGA SHG SID SQL SUM SYS TMP TOP UID USE USR VAR.

`sapsystemname`

*   is optional

*   Type: `string` ([ABAP System ID](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/sapsystemname")

### sapsystemname Type

`string` ([ABAP System ID](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md))

### sapsystemname Constraints

**maximum length**: the maximum number of characters for this string is: `3`

**minimum length**: the minimum number of characters for this string is: `3`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?!ADD|ALL|AMD|ADM|AND|ANY|ARE|ASC|AUX|AVG|BIT|CDC|COM|CON|DAA|DBA|ECO|END|EPS|FOR|GET|GID|IBM|INT|KEY|LOG|LPT|MAP|MAX|MIN|MON|NIX|NOT|NUL|OFF|OLD|OMS|OUT|PAD|PRN|RAW|REF|ROW|SAP|SET|SGA|SHG|SID|SQL|SUM|SYS|TMP|TOP|UID|USE|USR|VAR)[A-Z][A-Z0-9]{2}$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F!ADD%7CALL%7CAMD%7CADM%7CAND%7CANY%7CARE%7CASC%7CAUX%7CAVG%7CBIT%7CCDC%7CCOM%7CCON%7CDAA%7CDBA%7CECO%7CEND%7CEPS%7CFOR%7CGET%7CGID%7CIBM%7CINT%7CKEY%7CLOG%7CLPT%7CMAP%7CMAX%7CMIN%7CMON%7CNIX%7CNOT%7CNUL%7COFF%7COLD%7COMS%7COUT%7CPAD%7CPRN%7CRAW%7CREF%7CROW%7CSAP%7CSET%7CSGA%7CSHG%7CSID%7CSQL%7CSUM%7CSYS%7CTMP%7CTOP%7CUID%7CUSE%7CUSR%7CVAR\)%5BA-Z%5D%5BA-Z0-9%5D%7B2%7D%24 "try regular expression with regexr.com")

### sapsystemname Default Value

The default value is:

```json
"H01"
```

## size\_of\_persistence

Enter the size of the HANA memory in blocks of 15 GB on AWS or 16 GB on Azure

`size_of_persistence`

*   is required

*   Type: `integer` ([HANA Memory Size](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-hana-memory-size.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-hana-memory-size.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/size_of_persistence")

### size\_of\_persistence Type

`integer` ([HANA Memory Size](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-hana-memory-size.md))

### size\_of\_persistence Constraints

**constant**: the value of this property must be equal to:

```json
4
```

### size\_of\_persistence Default Value

The default value is:

```json
4
```

## size\_of\_runtime

Enter the size of the ABAP runtime in blocks of 16 GB

`size_of_runtime`

*   is required

*   Type: `integer` ([ABAP Runtime Size](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-runtime-size.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-runtime-size.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/size_of_runtime")

### size\_of\_runtime Type

`integer` ([ABAP Runtime Size](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-runtime-size.md))

### size\_of\_runtime Constraints

**constant**: the value of this property must be equal to:

```json
1
```

### size\_of\_runtime Default Value

The default value is:

```json
1
```
