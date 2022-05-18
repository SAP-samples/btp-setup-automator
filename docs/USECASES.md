# Use Cases

You find several use cases in the folder [`/usecases/releases`](../usecases/released) that you can use *per se* or as a blueprint for your own scripts.

This file gives you an overview on the content of the different scenarios.

> ⚠ NOTE: You find more use cases and parameters files in the folder [`/usecases`](../usecases), however only the ones available in the directory `released` are tested by us and should work.

## Use case "cap_app_launchpad.json"

The file [cap_app_launchpad.json](../usecases/released/cap_app_launchpad.json) contains the setup and deployment of a of a CAP application to a Cloud Foundry Environment in a SAP BTP account. This includes the necessary service instance, app subscriptions and role collections.

The services and subscriptions that are created are:

* XSUAA
* SAP HANA Cloud
* SAP Launchpad

The code of the application is pulled from the GitHub repository <https://github.com/SAP-samples/cloud-cap-risk-management>.

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest02.json](../integrationtests/parameterfiles/integrationtest02.json).

## Use case "build_resilient_apps_free_tier"

The file [build_resilient_apps_free_tier](../usecases/released/build_resilient_apps_free_tier) contains the setup of an application complementing an existing business process in an SAP solution - currently SAP S/4HANA - with additional business process steps. This includes the necessary service instance, app subscriptions and role collections. In addition the CI/CD service on SAP BTP is provisioned for a true end2end setup.

The services and subscriptions that are created are:

* Connectivity Service
* Destination Service
* Application Log
* XSUAA
* SAP HANA Cloud
* SAP Launchpad
* Enterprise Messaging
* CI/CD Service

The code of the application is pulled from the GitHub repository <https://github.com/SAP-samples/btp-build-resilient-apps/tree/extension>.

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest03.json](../integrationtests/parameterfiles/integrationtest03.json).

## Use case "setup_ABAP_steampunk.json"

The file [setup_ABAP_steampunk.json](../usecases/released/setup_ABAP_steampunk.json) contains the setup of an ABAP Steampunk instance on your SAP BTP account.

## Use case "setup_ias.json"

The file [setup_ias.json](../usecases/released/setup_ias.json) contains the setup i.e. the configuration of services to create trust between the SAP BTP subaccount and a customer IAS tenant.

## Use case "setup_kyma_free_tier.json"

The file [setup_kyma_free_tier.json](../usecases/released/setup_kyma_free_tier.json) contains the setup of a Kyma environment using the `free tier` plan

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest09.json](../integrationtests/parameterfiles/integrationtest09.json).

## Use case "setup_kyma_gcp.json"

The file [setup_kyma_gcp.json](../usecases/released/setup_kyma_gcp.json) contains the setup of a Kyma environment on Google Cloud Platform (GCP) using the `GCP` plan.

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest10.json](../integrationtests/parameterfiles/integrationtest10.json).

## Use case "setup_kyma_TRIAL.json"

The file [setup_kyma_TRIAL.json](../usecases/released/setup_kyma_TRIAL.json) contains the setup of a Kyma environment on SAP BTP Trial.

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest08.json](../integrationtests/parameterfiles/integrationtest08.json).

## Use case "setup_kyma_gcp_with_dapr.json"

The file [setup_kyma_gcp_with_dapr.json](../usecases/released/setup_kyma_gcp_with_dapr.json) contains the setup of a Kyma environment  on Google Cloud Platform (GCP) using the `GCP` plan including the deployment of Dapr, Redis and a sample app.

The code of the application is pulled from the GitHub repository <https://github.com/SAP-samples/kyma-runtime-extension-samples/tree/main/custom-component-dapr>.

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest11.json](../integrationtests/parameterfiles/integrationtest11.json).

## Use case "setup_task_center.json"

The file [setup_task_center.json](../usecases/released/setup_task_center.json) contains the setup of services for the SAP Task Center including establishing the trust with your custom IAS tenant.

The services and subscriptions that are created are:

* XSUAA
* SAP One Inbox
* SAP Launchpad

The use case is referenced from the parameters file [/integrationtests/parameterfiles/integrationtest07.json](../integrationtests/parameterfiles/integrationtest07.json).
