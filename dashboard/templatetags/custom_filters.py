from django import template

register = template.Library()

@register.filter
def map_attr(queryset, attr):
    """Extracts a list of attribute values from a queryset or list of objects."""
    return [getattr(item, attr, None) for item in queryset]
