import os, sys

# from urllib import quote_plus

if sys.platform.startswith('linux'):
	from urllib import quote_plus
else:
	from urllib.parse import quote_plus

from django import template


register = template.Library()

@register.filter
def urlify(value):
	return quote_plus(value)
