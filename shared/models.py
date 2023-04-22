from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime,date

class FollowRequest(models.Model):
	from_user = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE)
	to_user = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=True)

	def __str__(self):
		return "FollowRequest - "+str(self.pk)

