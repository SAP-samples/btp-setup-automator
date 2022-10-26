## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [admin\_email](#admin_email)                        | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-email-address.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/admin_email")           |
| [description](#description)                         | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-description.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/description")       |
| [is\_development\_allowed](#is_development_allowed) | `boolean` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-development-system.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/is_development_allowed") |
| [sapsystemname](#sapsystemname)                     | `string`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md "undefined#/properties/services/items/allOf/1/then/allOf/0/then/allOf/0/then/properties/parameters/properties/sapsystemname")              |

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

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>()\[\]\\,;:\s@"`]+@([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E\(\)%5C%5B%5C%5D%5C%5C%2C%3B%3A%5Cs%40%22%60%5D%2B%40\(%5Ba-zA-Z%5C-0-9%5D%2B%5C.\)%2B%5Ba-zA-Z%5D%7B2%2C%7D%24 "try regular expression with regexr.com")

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

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^']{0,256}$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E'%5D%7B0%2C256%7D%24 "try regular expression with regexr.com")

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

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?!ADD|ALL|AMD|AND|ANY|ARE|ASC|AUX|AVG|BIT|CDC|COM|CON|DBA|END|EPS|FOR|GET|GID|IBM|INT|KEY|LOG|LPT|MAP|MAX|MIN|MON|NIX|NOT|NUL|OFF|OLD|OMS|OUT|PAD|PRN|RAW|REF|ROW|SAP|SET|SGA|SHG|SID|SQL|SUM|SYS|TMP|TOP|UID|USE|USR|VAR)[A-Z][A-Z0-9]{2}$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F!ADD%7CALL%7CAMD%7CAND%7CANY%7CARE%7CASC%7CAUX%7CAVG%7CBIT%7CCDC%7CCOM%7CCON%7CDBA%7CEND%7CEPS%7CFOR%7CGET%7CGID%7CIBM%7CINT%7CKEY%7CLOG%7CLPT%7CMAP%7CMAX%7CMIN%7CMON%7CNIX%7CNOT%7CNUL%7COFF%7COLD%7COMS%7COUT%7CPAD%7CPRN%7CRAW%7CREF%7CROW%7CSAP%7CSET%7CSGA%7CSHG%7CSID%7CSQL%7CSUM%7CSYS%7CTMP%7CTOP%7CUID%7CUSE%7CUSR%7CVAR\)%5BA-Z%5D%5BA-Z0-9%5D%7B2%7D%24 "try regular expression with regexr.com")

### sapsystemname Default Value

The default value is:

```json
"H01"
```
