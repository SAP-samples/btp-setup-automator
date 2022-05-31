# Parameters used for defining services

The `usecase.json` file has a section to define all services. 

If you use VS Code or any other IDE that supports JSON schemas, you can just add the following key/value pair to your use case file to get auto-fill help, when creating it:

````json
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-parameters.json",
````

These services can be configured through the following parameters:

| Parameter | Description | Type |
|---|---|---|
{% for key, value in parameters.items() -%}
| {{ key }} | {{ value.description }} | {{ value.type }} |
{% endfor %}
Checkout the [SAMPLECONFIG.md](/docs/SAMPLECONFIG.md) documentation for some examples.
