from django import template
register=template.Library()
def trunc(value):
    result=value[0:5]
    return result
register.filter("trunc",trunc)
