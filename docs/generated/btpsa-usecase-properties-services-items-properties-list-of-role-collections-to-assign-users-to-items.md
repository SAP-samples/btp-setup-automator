## items Type

`object` ([Details](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items.md))

# items Properties

| Property                                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)                                                               | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-name-of-the-role-collection.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/name")                                                      |
| [assignedUserGroupsFromParameterFile](#assignedusergroupsfromparameterfile) | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-list-of-user-groups-to-assign-the-role-collection.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/assignedUserGroupsFromParameterFile") |
| [attribute](#attribute)                                                     | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-name-custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/attribute")                                                   |
| [attributeValue](#attributevalue)                                           | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-value--custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/attributeValue")                                            |
| [group](#group)                                                             | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-group-name-custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/group")                                                           |
| [idp](#idp)                                                                 | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-idp-name.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/idp")                                                                          |

## name

name of the role collection

`name`

*   is optional

*   Type: `string` ([name of the role collection](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-name-of-the-role-collection.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-name-of-the-role-collection.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/name")

### name Type

`string` ([name of the role collection](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-name-of-the-role-collection.md))

## assignedUserGroupsFromParameterFile

list of user groups to assign the role collection

`assignedUserGroupsFromParameterFile`

*   is optional

*   Type: `array` ([list of user groups to assign the role collection](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-list-of-user-groups-to-assign-the-role-collection.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-list-of-user-groups-to-assign-the-role-collection.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/assignedUserGroupsFromParameterFile")

### assignedUserGroupsFromParameterFile Type

`array` ([list of user groups to assign the role collection](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-list-of-user-groups-to-assign-the-role-collection.md))

## attribute

the name of the attribute. To be found in the identity provider.

`attribute`

*   is optional

*   Type: `string` ([attribute name (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-name-custom-idp.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-name-custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/attribute")

### attribute Type

`string` ([attribute name (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-name-custom-idp.md))

## attributeValue

the value of the attribute. To be found in the identity provider.

`attributeValue`

*   is optional

*   Type: `string` ([attribute value  (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-value--custom-idp.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-value--custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/attributeValue")

### attributeValue Type

`string` ([attribute value  (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-attribute-value--custom-idp.md))

## group

the name of the user group. To be found in the identity provider.

`group`

*   is optional

*   Type: `string` ([group name (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-group-name-custom-idp.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-group-name-custom-idp.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/group")

### group Type

`string` ([group name (custom IdP)](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-group-name-custom-idp.md))

## idp

the identity provider that hosts the user.

`idp`

*   is optional

*   Type: `string` ([IdP name](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-idp-name.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-idp-name.md "undefined#/properties/services/items/properties/requiredrolecollections/items/properties/idp")

### idp Type

`string` ([IdP name](btpsa-usecase-properties-services-items-properties-list-of-role-collections-to-assign-users-to-items-properties-idp-name.md))
