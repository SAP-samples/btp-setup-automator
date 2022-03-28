# Parameters that can be used when calling btp-setup-automator

When calling the '`btp-setup-automator` you can provide additional parameters to the command line of add the parameters in the `parameters.json` file.

These are the available commands:

| Parameter | Description | Type  | Mandatory | Default value |
|---|---|---|---|---|
{% for param in params -%}
| {{ param.argument }} | {{ param.help }} | {{ param.type }} | {{ param.mandatory }} | {{ param.default }} |
{% endfor %}

You can get an overview of those commands as well, by simply typing the following command in your command line terminal:

```bash
./btpsa -h
```
