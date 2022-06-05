# BTP SERVICES

This page provides an overview over the services, app subscriptions (applications) and environments fetched from an [SAP BTP "pay-as-you-go"](https://store.sap.com/dcp/en/product/display-9999951781_live_v1) global account.

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

**{{ service.displayName }}**

{{ service.description }}

### Service plans for {{ service.name }}

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
{%- for plan in service.servicePlans %}
|  {{ service.name }}  |  {{ service.displayName }}  |  {%- for datacenter in plan.dataCenters %} {{ datacenter.region }} - {{ datacenter.displayName }}{% if not loop.last %}<br>{% endif %} {%- endfor %}  |
{%- endfor %}

{%- endfor %}

{%- endfor %}

