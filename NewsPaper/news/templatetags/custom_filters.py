from django import template


register = template.Library()


bad_words = ['редиска','дурак']

@register.filter()
def censor(value):
    if value in bad_words:
        value = '******'

    return value



