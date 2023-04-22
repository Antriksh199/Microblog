from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime,date
from User.models import *


class Blog(models.Model):
	created_by=models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=250)
	category=models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField()
	title = models.CharField(max_length=20,blank=True)
	likes = models.ManyToManyField(User,blank=True,null=True,related_name='liked_by',symmetrical=False)

	def __str__(self):
		return self.title

	def get_user_full_name(self):
		u = UserProfile.objects.filter(user=self.created_by).values('first_name','last_name').first()
		return ' '.join(x.capitalize() for x in u.values())

	def likes_count(self):
		return self.likes.all().count()

	def likers(self):
		return [u['id'] for u in self.likes.all().values('id')]



class Like(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	liked_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Share(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	shared_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
	comment=models.CharField(max_length=100, blank=False)  