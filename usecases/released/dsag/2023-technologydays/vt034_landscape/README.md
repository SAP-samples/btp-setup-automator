# Setup of Sample Landscape (DSAG Technology Days - Session VT034)

The files provided in this directory contain the setup of a landscape presented in session VT034 at the DSAG Technology Days.

## Scenario

This demo setup showcases a SAP BTP landscape setup as described in the [best practices guide](https://help.sap.com/doc/463beee05122412db150e08e6f444b7e/Cloud/en-US/Planning_LM.pdf). The setup comprises the creation of different directories with subaccounts for different organizational units like HT, IT and Sales. 
In addition a service entitlement provided, a service instance is created and the corresponding role collections are assigned ot the user groups.

## Setup in BTP Setup Automator

The files relevant for the setup of the accounts are structured in accordance to the organizational structure following the naming pattern `<org-unit>/<environment>`. As an example the relevant files for the organizational unit *"IT"* for the *test* environment are located in the directory `it/test`.

## Github Action Sample

We leverage the CI/CD infrastructure of GitHub Actions to execute the account setup as defined via the `parameters.json` and `usecase.json` files in the different directories. We provide a sample workflow for the setup named [landscape_setup.yml](./github_action_samples/landscape_setup.yml).

Be aware that you must store several parameters as secret in the GitHub repository namely:

| Name  | Content
| ---   | ---
| BTPSA_PARAM_GLOBALACCOUNT | ID of the SAP BTP global account
| BTPSA_PARAM_MYEMAIL       | Email to be used for login to SAP BTP
| BTPSA_PARAM_MYPASSWORD    | Password of the user

In order to cleanup the structure, we also provide a GitHub Action for this task named [landscape_cleanup.yml](./github_action_samples/landscape_cleanup.yml).

> **Attention** - handle with care as this workflow will delete the specified directory.

You find more information about GitHub Actions [here](https://docs.github.com/en/actions).
