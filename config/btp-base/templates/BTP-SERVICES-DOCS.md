# BTP SERVICES

This page provides an overview over the services, app subscriptions (applications) and environments.

{%- for category in btpservicelist %}
# {{ category.name }}

Services are listed and sorted by their technical name. The display name is added in parentheses.
{% for service in category.list %}
- [{{ service.name }} ({{ service.displayName }})](#{{ service.name|lower }})
{%- endfor %}

{%- endfor %}

{%- for category in btpservicelist %}

{%- for service in category.list %}
# {{ service.name }}

**{{ service.displayName }}**: {{ service.description }}

## Service plans
| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
{%- for plan in service.servicePlans %}
|  {{ service.name }}  |  {{ service.displayName }}  |  {%- for datacenter in plan.dataCenters %} {{ datacenter.region }} - {{ datacenter.displayName }}{% if not loop.last %}<br>{% endif %} {%- endfor %}  |


{%- endfor %}

{%- endfor %}

{%- endfor %}

