## items Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-trusts-items.md))

# items Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [alias](#alias)       | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-trusts-items-properties-alias.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/trusts/items/properties/alias")       |
| [certData](#certdata) | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-trusts-items-properties-certdata.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/trusts/items/properties/certData") |

## alias



`alias`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-trusts-items-properties-alias.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/trusts/items/properties/alias")

### alias Type

`string`

### alias Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-z0-9]{1}[a-z0-9-]{0,14}[a-z0-9]{1}$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-z0-9%5D%7B1%7D%5Ba-z0-9-%5D%7B0%2C14%7D%5Ba-z0-9%5D%7B1%7D%24 "try regular expression with regexr.com")

## certData



`certData`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-6-then-properties-parameters-properties-data-properties-filecontainer-properties-trusts-items-properties-certdata.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/6/then/properties/parameters/properties/data/properties/fileContainer/properties/trusts/items/properties/certData")

### certData Type

`string`

### certData Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^-----BEGIN CERTIFICATE-----\s[A-Za-z0-9+/\s]+={0,2}\s-----END CERTIFICATE-----$
```

[try pattern](https://regexr.com/?expression=%5E-----BEGIN%20CERTIFICATE-----%5Cs%5BA-Za-z0-9%2B%2F%5Cs%5D%2B%3D%7B0%2C2%7D%5Cs-----END%20CERTIFICATE-----%24 "try regular expression with regexr.com")
