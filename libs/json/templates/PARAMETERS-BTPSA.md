# Parameters that can be used when calling btp-setup-automator

{% for param in params -%}## Parameter {{ param.argument }}

{{ param.help }}

Type: {{ param.type }}

Mandatory: {{ param.mandatory }}

Default: {{ param.default }}

{% endfor %}
