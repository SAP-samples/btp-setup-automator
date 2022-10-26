## aboutThisUseCase Type

`object` ([name of the service](btpsa-usecase-properties-name-of-the-service.md))

# aboutThisUseCase Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                               |
| :---------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                     | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-id-of-the-service-internal-use-only.md "undefined#/properties/aboutThisUseCase/properties/id")      |
| [name](#name)                 | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-name-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/name")                   |
| [description](#description)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-description-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/description")     |
| [author](#author)             | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-email-of-the-author-of-this-use-case.md "undefined#/properties/aboutThisUseCase/properties/author") |
| [testStatus](#teststatus)     | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-test-status-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/testStatus")      |
| [usageStatus](#usagestatus)   | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-usage-status-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/usageStatus")    |
| [relatedLinks](#relatedlinks) | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-links-related-to-this-use-case.md "undefined#/properties/aboutThisUseCase/properties/relatedLinks") |

## id

ID of the service (internal use only)

`id`

*   is optional

*   Type: `string` ([ID of the service (internal use only)](btpsa-usecase-properties-name-of-the-service-properties-id-of-the-service-internal-use-only.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-id-of-the-service-internal-use-only.md "undefined#/properties/aboutThisUseCase/properties/id")

### id Type

`string` ([ID of the service (internal use only)](btpsa-usecase-properties-name-of-the-service-properties-id-of-the-service-internal-use-only.md))

### id Default Value

The default value is:

```json
"1234"
```

## name

name of the use case

`name`

*   is required

*   Type: `string` ([name of the use case](btpsa-usecase-properties-name-of-the-service-properties-name-of-the-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-name-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/name")

### name Type

`string` ([name of the use case](btpsa-usecase-properties-name-of-the-service-properties-name-of-the-use-case.md))

## description

description of the use case

`description`

*   is optional

*   Type: `string` ([description of the use case](btpsa-usecase-properties-name-of-the-service-properties-description-of-the-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-description-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/description")

### description Type

`string` ([description of the use case](btpsa-usecase-properties-name-of-the-service-properties-description-of-the-use-case.md))

## author

email of the author of this use case

`author`

*   is required

*   Type: `string` ([email of the author of this use case](btpsa-usecase-properties-name-of-the-service-properties-email-of-the-author-of-this-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-email-of-the-author-of-this-use-case.md "undefined#/properties/aboutThisUseCase/properties/author")

### author Type

`string` ([email of the author of this use case](btpsa-usecase-properties-name-of-the-service-properties-email-of-the-author-of-this-use-case.md))

### author Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## testStatus

test status of the use case

`testStatus`

*   is required

*   Type: `string` ([test status of the use case](btpsa-usecase-properties-name-of-the-service-properties-test-status-of-the-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-test-status-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/testStatus")

### testStatus Type

`string` ([test status of the use case](btpsa-usecase-properties-name-of-the-service-properties-test-status-of-the-use-case.md))

### testStatus Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"tested successfully"` |             |
| `"not tested"`          |             |

## usageStatus

usage status of the use case

`usageStatus`

*   is required

*   Type: `string` ([usage status of the use case](btpsa-usecase-properties-name-of-the-service-properties-usage-status-of-the-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-usage-status-of-the-use-case.md "undefined#/properties/aboutThisUseCase/properties/usageStatus")

### usageStatus Type

`string` ([usage status of the use case](btpsa-usecase-properties-name-of-the-service-properties-usage-status-of-the-use-case.md))

### usageStatus Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                    | Explanation |
| :----------------------- | :---------- |
| `"READY TO BE USED"`     |             |
| `"NOT READY TO BE USED"` |             |

## relatedLinks

links related to this use case

`relatedLinks`

*   is optional

*   Type: `array` ([links related to this use case](btpsa-usecase-properties-name-of-the-service-properties-links-related-to-this-use-case.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-name-of-the-service-properties-links-related-to-this-use-case.md "undefined#/properties/aboutThisUseCase/properties/relatedLinks")

### relatedLinks Type

`array` ([links related to this use case](btpsa-usecase-properties-name-of-the-service-properties-links-related-to-this-use-case.md))
