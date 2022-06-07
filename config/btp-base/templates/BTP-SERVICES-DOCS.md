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

# ALL SERVICES OF TYPE "{{ category.name }}"

{%- for service in category.list %}

# {{ service.name }}

<img src="data:{{ service.iconFormat }}, {{ service.iconBase64 }}" />

**{{ service.displayName }}**

{{ service.description }}

### Related categories
{%- for serviceCategory in service.serviceCategories %}
- {{ serviceCategory }}
{%- endfor %}
{%- for businessCategory in service.businessCategories %}
- {{ businessCategory }}
{%- endfor %}

### Additional information
{%- for link in service.links %}
- [{{ link.title }}]({{ link.linkURL }})
{%- endfor %}

### Service plans for {{ service.name }}

| Name | Display name | Data center availability  |
|------|----------------|---------------------------|
{%- for plan in service.servicePlans %}
|  {{ plan.name }}  |  {{ plan.displayName }}  |  {%- for datacenter in plan.dataCenters %} {{ datacenter.region }} - {{ datacenter.displayName }}{% if not loop.last %}<br>{% endif %} {%- endfor %}  |
{%- endfor %}

{%- endfor %}

{%- endfor %}
