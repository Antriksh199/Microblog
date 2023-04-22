from django import template
from django.contrib.auth.models import User
from User.models import *
from Blog.models import *


register = template.Library()

@register.simple_tag
def check_like(value,arg):
	b = Blog.objects.get(id=value.id).values('likes')
	likes = [x.created_by for x in b.likes.all()]


