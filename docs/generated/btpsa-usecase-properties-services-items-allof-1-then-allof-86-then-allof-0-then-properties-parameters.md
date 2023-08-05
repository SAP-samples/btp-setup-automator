## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters.md))

# parameters Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                |
| :-------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [desiredAZs](#desiredazs)         | `integer` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-desired-azs.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/desiredAZs")                  |
| [policyDocument](#policydocument) | `object`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-endpoint-policy-document.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/policyDocument") |
| [serviceName](#servicename)       | `string`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-service-name.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/serviceName")                |

## desiredAZs

Specifies the desired number of Availability Zones of the endpoint.

Example: 2

By default, SAP Private Link service only creates the endpoint if the endpoint service is deployed in the same AZs as SAP BTP, to maximize High Availability.
In case fewer AZs than SAP BTPs should be allowed (i.e. only one or two AZs), please explicitly allow it by specifying the desired number of AZs via this parameter.

`desiredAZs`

*   is optional

*   Type: `integer` ([Desired AZs](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-desired-azs.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-desired-azs.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/desiredAZs")

### desiredAZs Type

`integer` ([Desired AZs](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-desired-azs.md))

### desiredAZs Default Value

The default value is:

```json
3
```

## policyDocument

Specifies the Endpoint Policy.\n\nThe endpoint policy controls which AWS principals (AWS accounts, IAM users, and IAM roles) can use the VPC endpoint to access the endpoint service.

`policyDocument`

*   is optional

*   Type: `object` ([Endpoint Policy Document](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-endpoint-policy-document.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-endpoint-policy-document.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/policyDocument")

### policyDocument Type

`object` ([Endpoint Policy Document](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-endpoint-policy-document.md))

## serviceName

Specifies the service name for which the VPC Endpoint should be created.\n\nExample: "com.amazonaws.us-east-1.monitoring" or "com.amazonaws.vpce.us-east-1.vpce-svc-09ac27c2a0cd319fa" for AWS or custom VPC Endpoint Services respectively

`serviceName`

*   is required

*   Type: `string` ([Service Name](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-service-name.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-service-name.md "undefined#/properties/services/items/allOf/1/then/allOf/86/then/allOf/0/then/properties/parameters/properties/serviceName")

### serviceName Type

`string` ([Service Name](btpsa-usecase-properties-services-items-allof-1-then-allof-86-then-allof-0-then-properties-parameters-properties-service-name.md))

### serviceName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
com\.amazonaws\..+
```

[try pattern](https://regexr.com/?expression=com%5C.amazonaws%5C..%2B "try regular expression with regexr.com")
