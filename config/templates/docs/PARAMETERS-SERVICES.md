# Parameters used for defining services

The `usecase.json` file has a section to define all services. 

If you use VS Code or any other IDE that supports JSON schemas, you can just add the following key/value pair to your use case file to get auto-fill help, when creating it:

````json
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/schemas/btpsa-parameters.json",
````

These services can be configured through the following parameters:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
{% for param in params -%}
| {{ param.argument }} | {{ param.help }} | {{ param.type }} | {{ param.mandatory }} | {{ param.default }} |
{% endfor %}
Checkout the [SAMPLECONFIG.md](/docs/SAMPLECONFIG.md) documentation for some examples.
