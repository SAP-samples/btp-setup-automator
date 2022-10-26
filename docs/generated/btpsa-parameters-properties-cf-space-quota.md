## cfspacequota Type

`object` ([CF space quota](btpsa-parameters-properties-cf-space-quota.md))

# cfspacequota Properties

| Property                                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                               |
| :------------------------------------------------------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [createQuotaPlan](#createquotaplan)                                 | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-create-new-quota-plan.md "undefined#/properties/cfspacequota/properties/createQuotaPlan")                                       |
| [spaceQuotaAllowPaidServicePlans](#spacequotaallowpaidserviceplans) | `boolean` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-allow-paid-service-plans.md "undefined#/properties/cfspacequota/properties/spaceQuotaAllowPaidServicePlans")                    |
| [spaceQuotaAppInstances](#spacequotaappinstances)                   | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-application-instances.md "undefined#/properties/cfspacequota/properties/spaceQuotaAppInstances")                |
| [spaceQuotaInstanceMemory](#spacequotainstancememory)               | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-instance-memory-limit-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaInstanceMemory")               |
| [spaceQuotaName](#spacequotaname)                                   | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-name-of-the-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaName")                                       |
| [spaceQuotaReservedRoutePorts](#spacequotareservedrouteports)       | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-maximum-number-of-reserved-routes.md "undefined#/properties/cfspacequota/properties/spaceQuotaReservedRoutePorts")              |
| [spaceQuotaRoutes](#spacequotaroutes)                               | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-routes-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaRoutes")                      |
| [spaceQuotaServiceInstances](#spacequotaserviceinstances)           | `integer` | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-service-instances-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaServiceInstances") |
| [spaceQuotaTotalMemory](#spacequotatotalmemory)                     | `string`  | Optional | cannot be null | [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-memory-limit-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaTotalMemory")                     |

## createQuotaPlan

if set to true, a new quota plan will be created

`createQuotaPlan`

*   is optional

*   Type: `boolean` ([create new quota plan](btpsa-parameters-properties-cf-space-quota-properties-create-new-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-create-new-quota-plan.md "undefined#/properties/cfspacequota/properties/createQuotaPlan")

### createQuotaPlan Type

`boolean` ([create new quota plan](btpsa-parameters-properties-cf-space-quota-properties-create-new-quota-plan.md))

## spaceQuotaAllowPaidServicePlans

if set to true, paid service plans are allowed

`spaceQuotaAllowPaidServicePlans`

*   is optional

*   Type: `boolean` ([allow paid service plans](btpsa-parameters-properties-cf-space-quota-properties-allow-paid-service-plans.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-allow-paid-service-plans.md "undefined#/properties/cfspacequota/properties/spaceQuotaAllowPaidServicePlans")

### spaceQuotaAllowPaidServicePlans Type

`boolean` ([allow paid service plans](btpsa-parameters-properties-cf-space-quota-properties-allow-paid-service-plans.md))

### spaceQuotaAllowPaidServicePlans Default Value

The default value is:

```json
true
```

## spaceQuotaAppInstances

total number of application instances. -1 represents an unlimited amount.

`spaceQuotaAppInstances`

*   is optional

*   Type: `integer` ([total number of application instances](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-application-instances.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-application-instances.md "undefined#/properties/cfspacequota/properties/spaceQuotaAppInstances")

### spaceQuotaAppInstances Type

`integer` ([total number of application instances](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-application-instances.md))

### spaceQuotaAppInstances Default Value

The default value is:

```json
-1
```

## spaceQuotaInstanceMemory

instance memory limit for the quota plan

`spaceQuotaInstanceMemory`

*   is optional

*   Type: `string` ([instance memory limit for quota plan](btpsa-parameters-properties-cf-space-quota-properties-instance-memory-limit-for-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-instance-memory-limit-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaInstanceMemory")

### spaceQuotaInstanceMemory Type

`string` ([instance memory limit for quota plan](btpsa-parameters-properties-cf-space-quota-properties-instance-memory-limit-for-quota-plan.md))

### spaceQuotaInstanceMemory Default Value

The default value is:

```json
"1024M"
```

## spaceQuotaName

name of the quota plan to be created

`spaceQuotaName`

*   is optional

*   Type: `string` ([name of the quota plan](btpsa-parameters-properties-cf-space-quota-properties-name-of-the-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-name-of-the-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaName")

### spaceQuotaName Type

`string` ([name of the quota plan](btpsa-parameters-properties-cf-space-quota-properties-name-of-the-quota-plan.md))

### spaceQuotaName Default Value

The default value is:

```json
"development-quota"
```

## spaceQuotaReservedRoutePorts

maximum number of routes that may be created with reserved ports

`spaceQuotaReservedRoutePorts`

*   is optional

*   Type: `integer` ([maximum number of reserved routes](btpsa-parameters-properties-cf-space-quota-properties-maximum-number-of-reserved-routes.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-maximum-number-of-reserved-routes.md "undefined#/properties/cfspacequota/properties/spaceQuotaReservedRoutePorts")

### spaceQuotaReservedRoutePorts Type

`integer` ([maximum number of reserved routes](btpsa-parameters-properties-cf-space-quota-properties-maximum-number-of-reserved-routes.md))

## spaceQuotaRoutes

total number of routes for the quota plan

`spaceQuotaRoutes`

*   is optional

*   Type: `integer` ([total number of routes for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-routes-for-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-routes-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaRoutes")

### spaceQuotaRoutes Type

`integer` ([total number of routes for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-routes-for-quota-plan.md))

### spaceQuotaRoutes Default Value

The default value is:

```json
5
```

## spaceQuotaServiceInstances

total number of service instances for the quota plan

`spaceQuotaServiceInstances`

*   is optional

*   Type: `integer` ([total number of service instances for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-service-instances-for-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-service-instances-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaServiceInstances")

### spaceQuotaServiceInstances Type

`integer` ([total number of service instances for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-number-of-service-instances-for-quota-plan.md))

### spaceQuotaServiceInstances Default Value

The default value is:

```json
5
```

## spaceQuotaTotalMemory

total memory limit for the quota plan

`spaceQuotaTotalMemory`

*   is optional

*   Type: `string` ([total memory limit for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-memory-limit-for-quota-plan.md))

*   cannot be null

*   defined in: [JSON Schema for service parameters used in BTPSA](btpsa-parameters-properties-cf-space-quota-properties-total-memory-limit-for-quota-plan.md "undefined#/properties/cfspacequota/properties/spaceQuotaTotalMemory")

### spaceQuotaTotalMemory Type

`string` ([total memory limit for quota plan](btpsa-parameters-properties-cf-space-quota-properties-total-memory-limit-for-quota-plan.md))

### spaceQuotaTotalMemory Default Value

The default value is:

```json
"2048M"
```
