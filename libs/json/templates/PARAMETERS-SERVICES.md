# Parameters used for defining services

{% for param in params -%}## Parameter {{ param.argument }}

{{ param.help }}

Type: {{ param.type }}

Mandatory: {{ param.mandatory }}

Default: {{ param.default }}

{% endfor %}
