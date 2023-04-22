from django.shortcuts import render
from User.models import *
from django.views.decorators.cache import cache_control
#from django.views.decorators import login_required
from django.contrib.auth.decorators import login_required
from Blog.models import *

# Create your views here.
@login_required(login_url = 'User:Login_view')

def user_list(request):
	user = request.user
	users = UserProfile.objects.all().exclude(user=request.user)
	current_user = UserProfile.objects.filter(user=request.user).first()
	follows = [i.pk for i in current_user.follows.all()]
	print(follows)
	return render(request, 'shared/user_list.html',{'user':user,'users' :users,'follows':follows})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def follow(request,pk):
	user = request.user
	profile = UserProfile.objects.filter(user=user).first()
	user_to_follow = UserProfile.objects.filter(id=pk).first()
	print(user_to_follow.user.username)
	print(pk)
	try:
		profile.follows.add(pk)
		profile.save()
		profile.refresh_from_db()
		text = 'You have successfully followed '+ user_to_follow.user.username +'.'
		print('try completed.')
		status = 200
	except Exception as e:
		print(str(e))
		text = 'Some error occured while following '+ user_to_follow.user.username +'.'
		print('try failed.')
		status = 400
	return render(request, 'shared/follow_unfollow_message.html',{'text':text,'status':status,'pk':pk})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def unfollow(request,pk):
	user = request.user
	profile = UserProfile.objects.filter(user=user).first()
	user_to_follow = UserProfile.objects.filter(id=pk).first()
	print(user_to_follow.user.username)
	print(pk)
	try:
		profile.follows.remove(pk)
		profile.save()
		profile.refresh_from_db()
		text = 'You have successfully unfollowed '+ user_to_follow.user.username +'.'
		print('try completed.')
		status = 200
	except Exception as e:
		print(str(e))
		text = 'Some error occured while unfollowing '+ user_to_follow.user.username +'.'
		print('try failed.')
		status = 400
	return render(request, 'shared/follow_unfollow_message.html',{'text':text,'status':status,'pk':pk})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Like(request,pk):
	user = request.user
	#profile = UserProfile.objects.filter(user=user).first()
	blog = Blog.objects.get(id=pk)
	#user_to_follow = UserProfile.objects.filter(id=pk).first()
	#print(user_to_follow.user.username)
	print(pk)
	try:
		blog.likes.add(user.id)
		blog.save()
		blog.refresh_from_db()
		text = 'You have successfully liked blog by '+ blog.get_user_full_name() +'.'
		print('try completed.')
		status = 200
	except Exception as e:
		print(str(e))
		text = 'Some error occured while liking a post.'
		print('try failed.')
		status = 400
	return render(request, 'shared/like_unlike.html',{'text':text,'status':status,'pk':pk,'likes':blog.likes_count()})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Unlike(request,pk):
	user = request.user
	#profile = UserProfile.objects.filter(user=user).first()
	blog = Blog.objects.get(id=pk)
	#user_to_follow = UserProfile.objects.filter(id=pk).first()
	#print(user_to_follow.user.username)
	print(pk)
	try:
		blog.likes.remove(user)
		blog.save()
		blog.refresh_from_db()
		text = 'You have successfully unliked blog by  '+ blog.get_user_full_name() +'.'
		print('try completed.')
		status = 200
	except Exception as e:
		print(str(e))
		text = 'Some error occured while unliking a blog.'
		print('try failed.')
		status = 400
	return render(request, 'shared/like_unlike.html',{'text':text,'status':status,'pk':pk,'likes':blog.likes_count()})



