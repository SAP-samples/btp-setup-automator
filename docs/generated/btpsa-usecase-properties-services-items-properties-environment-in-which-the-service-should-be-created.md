## targetenvironment Type

`string` ([environment in which the service should be created](btpsa-usecase-properties-services-items-properties-environment-in-which-the-service-should-be-created.md))

## targetenvironment Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"cloudfoundry"` |             |
| `"kymaruntime"`  |             |
| `"sapbtp"`       |             |

## targetenvironment Default Value

The default value is:

```json
"cloudfoundry"
```
