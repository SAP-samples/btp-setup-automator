# Setup of SAP Build Apps

The files provided in this directory contain the necessary configuration to setup the infrastructure for SAP Build Apps on the SAP BTP.

## Scenario

To setup SAP Build Apps in a sub account several steps must be executed. This can either be done via a [Booster](https://help.sap.com/docs/build-apps/service-guide/booster-automatic-configuration) or in a [manual fashion](https://help.sap.com/docs/build-apps/service-guide/manual-configuration).

The files delivered in this use case combine the comfort of an automatic setup with the flexibility given in the manual setup. 

## Setup in BTP Setup Automator

The setup comprises several steps that must be executed in sequence. This is reflected in the `parameters.json` and `usecase.json` files provided in this directory namely:

1. Setup of trust with a custom IDP as defined in the file [step1_usecase.json](./step1_usecase.json).
2. Creation of the app subscriptions and service instances needed for SAP build Apps including the creation of the relevant role collections based on the role templates provided by the SAP Build Apps application. The setup is given in the file [step2_usecase.json](./step2_usecase.json).
3. Assignment of the role collections to the defined users or user groups is executed as defined in [step3_usecase.json](./step3_usecase.json). The user groups are defined in the file [step3_parameters.json](./step3_parameters.json).

## Github Action Sample

Due to the sequential execution of the the different steps, it ist the most comprehensive way to put the execution in a CI/CD pipeline. this sample contains a template on how to achieve this via GitHub Actions. The sample code is available [here](./github_action_samples/btpsa_sap_build_app.yml). 

Be aware that you must store several parameters as secret in the GitHub repository namely:

| Name  | Content
| ---   | ---
| BTPSA_PARAM_GLOBALACCOUNT | ID of the SAP BTP global account
| BTPSA_PARAM_MYEMAIL       | Email to be used for login to SAP BTP
| BTPSA_PARAM_MYPASSWORD    | Password of the user
| BTPSA_PARAM_IDP_TENANT    | Name of the IDP Tenant to establish trust with

You find more information about GitHub Actions [here](https://docs.github.com/en/actions).
