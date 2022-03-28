# Parameters used for defining services

The `usecase.json` file has a section to define all services. These services can be configured through the following parameters:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
{% for param in params -%}
| {{ param.argument }} | {{ param.help }} | {{ param.type }} | {{ param.mandatory }} | {{ param.default }} |
{% endfor %}

Checkout the [SAMPLECONFIG.md](SAMPLECONFIG.md) documentation for some examples.