from django import template
from django.utils.safestring import mark_safe
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text, extensions=['fenced_code', 'nl2br']))

