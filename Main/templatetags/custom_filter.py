from django import template

register = template.Library()


@register.filter
def first_char(value):
    result = ''
    for v in value.split(' '):
        result += v[0]
    return result

