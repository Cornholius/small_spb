from django import template
register = template.Library()


@register.filter
def to_class_name(value):
    print(dir(value.__class__.__name__))
    print(dir(value))
    return value.__class__.__name__
