# Parameters that can be used when calling btp-setup-automator

When calling the '`btp-setup-automator` you can provide additional parameters to the command line of add the parameters in the `parameters.json` file.

These are the available commands:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
| name | name of the service | str | True | None |
| entitleonly | if set to true, no service instances will be created by the tool | bool | False | False |
| category | category of the service | str | True | None |
| targetenvironment | environment in which the service should be created | str | True | cloudfoundry |
| plan | plan name of the service | str | False | None |
| planCatalogName | catalog name of the service plan | str | False | None |
| statusResponse | creation info | dict | False | None |
| instancename | name of the service | str | False | None |
| parameters | parameters for the service | ['dict', 'str'] | False | None |
| serviceparameterfile | parameter file for the service | str | False | None |
| amount | amount to be used for the service | int | False | 1 |
| repeatstatusrequest | number of seconds when status should be checked | int | False | 5 |
| repeatstatustimeout | timeout in seconds after which the script will stop checking the status | int | False | 3600 |
| createServiceKeys | list of service keys to be created for a service  | list | False | None |
| requiredServices | list of service keys to be created for a service  | list | False | None |
| requiredrolecollections | list of role collections to be created for a service | list | False | None |


You can get an overview of those commands as well, by simply typing the following command in your command line terminal:

```bash
./btpsa -h
```