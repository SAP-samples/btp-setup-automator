## items Type

`object` ([Details](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items.md))

# items Properties

| Property                                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :-------------------------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assignedRoles](#assignedroles)                                             | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-roles-for-custom-role-collection.md "undefined#/properties/assignrolecollections/items/properties/assignedRoles")                      |
| [assignedUserGroupsFromParameterFile](#assignedusergroupsfromparameterfile) | `array`  | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-user-groups-from-parameter-file.md "undefined#/properties/assignrolecollections/items/properties/assignedUserGroupsFromParameterFile") |
| [level](#level)                                                             | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-level-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/level")                                  |
| [name](#name)                                                               | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-name-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/name")                                    |
| [type](#type)                                                               | `string` | Required | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-type-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/type")                                    |

## assignedRoles

roles to be assigned to a custom role collection

`assignedRoles`

*   is optional

*   Type: `string[]` ([roles name](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-roles-for-custom-role-collection-roles-name.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-roles-for-custom-role-collection.md "undefined#/properties/assignrolecollections/items/properties/assignedRoles")

### assignedRoles Type

`string[]` ([roles name](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-roles-for-custom-role-collection-roles-name.md))

## assignedUserGroupsFromParameterFile

user groups to be assigned from the parameter file

`assignedUserGroupsFromParameterFile`

*   is required

*   Type: `array` ([user groups from parameter file](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-user-groups-from-parameter-file.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-user-groups-from-parameter-file.md "undefined#/properties/assignrolecollections/items/properties/assignedUserGroupsFromParameterFile")

### assignedUserGroupsFromParameterFile Type

`array` ([user groups from parameter file](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-user-groups-from-parameter-file.md))

## level

level of the role collection

`level`

*   is optional

*   Type: `string` ([level of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-level-of-the-role-collection.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-level-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/level")

### level Type

`string` ([level of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-level-of-the-role-collection.md))

### level Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"global account"` |             |
| `"sub account"`    |             |
| `"org"`            |             |
| `"space"`          |             |

## name

name of the role collection

`name`

*   is required

*   Type: `string` ([name of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-name-of-the-role-collection.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-name-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/name")

### name Type

`string` ([name of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-name-of-the-role-collection.md))

## type

type of the role collection

`type`

*   is required

*   Type: `string` ([type of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-type-of-the-role-collection.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-type-of-the-role-collection.md "undefined#/properties/assignrolecollections/items/properties/type")

### type Type

`string` ([type of the role collection](btpsa-usecase-properties-role-collections-to-be-assigned-to-a-service-items-properties-type-of-the-role-collection.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"account"`      |             |
| `"cloudfoundry"` |             |
| `"custom"`       |             |
