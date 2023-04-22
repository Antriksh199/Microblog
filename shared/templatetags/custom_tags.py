from django import template

register = template.Library()

@register.simple_tag
def check_follower(value,arg):
	if value is None:
		return False


	return arg in value
