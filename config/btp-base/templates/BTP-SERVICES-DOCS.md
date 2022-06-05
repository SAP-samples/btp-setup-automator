# BTP SERVICES

This page provides an overview over the services, app subscriptions (applications) and environments.

{%- for category in btpservicelist %}
# {{ category.name }}

{%- for service in category.list %}

## {{ service.displayName }} ({{ service.name }})

{{ service.description }}

{%- for plan in service.servicePlans %}

#### Service plan "{{ plan.name }}"
{{ plan.description }}
{%- endfor %}
{%- endfor %}
{%- endfor %}
