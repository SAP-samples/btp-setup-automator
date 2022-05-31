# Parameters that can be used when calling btp-setup-automator

When calling the '`btp-setup-automator` you can provide additional parameters to the command line of add the parameters in the `parameters.json` file.

If you use VS Code or any other IDE that supports JSON schemas, you can just add the following key/value pair to your parameters file to get auto-fill help, when creating it:

````json
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
````

These are the available parameters:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
{% for param in params -%}
| {{ param.argument }} | {{ param.help }} | {{ param.type }} | {{ param.mandatory }} | {{ param.default }} |
{% endfor %}
You can get an overview of those commands as well, by simply typing the following command in your command line terminal:

```bash
./btpsa -h
```
