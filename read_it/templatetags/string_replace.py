from django import template

register = template.Library()

@register.filter
def string_replace(value):
    return value.replace(" ","_")