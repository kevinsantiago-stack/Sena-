# Ejercicio 28: template filter truncate_chars
from django import template
register = template.Library()
@register.filter
def truncate_chars(value, max_length):
    s = str(value)
    if len(s) > int(max_length):
        return s[:int(max_length)] + '...'
    return s
