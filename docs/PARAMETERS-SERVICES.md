# Parameters used for defining services

## Parameter name

name of the service

Type: str

Mandatory: True

Default: None

## Parameter entitleonly

if set to true, no service instances will be created by the tool

Type: bool

Mandatory: False

Default: False

## Parameter category

category of the service

Type: str

Mandatory: True

Default: None

## Parameter createinenvironment

environment in which the service should be created

Type: str

Mandatory: True

Default: cloudfoundry

## Parameter plan

plan name of the service

Type: str

Mandatory: False

Default: None

## Parameter instancename

name of the service

Type: str

Mandatory: False

Default: None

## Parameter parameters

parameters for the service

Type: dict

Mandatory: False

Default: None

## Parameter amount

amount to be used for the service

Type: int

Mandatory: False

Default: None

## Parameter repeatstatusrequest

number of seconds when status should be checked

Type: int

Mandatory: False

Default: 5

## Parameter repeatstatustimeout

timeout in seconds after which the script will stop checking the status

Type: int

Mandatory: False

Default: 3600

## Parameter createServiceKeys

list of service keys to be created for a service 

Type: array

Mandatory: False

Default: None

## Parameter requiredrolecollections

list of role collections to be created for a service

Type: list

Mandatory: False

Default: None

