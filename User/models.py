from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#User = get_user_model()

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=30,blank=True)
	first_name = models.CharField(max_length=30,blank=True)
	last_name = models.CharField(max_length=30,blank=True)
	contact = models.CharField(max_length=13,blank=True)
	state = models.CharField(max_length=100,blank=True)
	country = models.CharField(max_length=30,blank=True)
	city = models.CharField(max_length=30,blank=True)
	dob = models.DateField(null = True)
	interests = models.CharField(max_length=100,blank=True)
	gender = models.CharField(max_length=20,blank=True)
	education = models.CharField(max_length=20,blank=True)
	follows = models.ManyToManyField('self',blank=True,null=True,related_name='followed_by',symmetrical=False)


	def get_followers_count(self):
		return self.follows.count

	def get_followers(self):
		return self.follows.count

	def check_follower(self,value):
		if value in self.follows.all:
			return True
		return False

	def __str__(self):
		return self.user.username

	def get_interest_list(self):
		return self.interests.split(';')

class Country(models.Model):
	name = models.CharField(max_length=30)
	code = models.CharField(max_length=4)

	def __str__(self):
		return self.name

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	state = models.CharField(max_length=30)

	def __str__(self):
		return self.state

class City(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	city = models.CharField(max_length=30)

	def __str__(self):
		return self.city
