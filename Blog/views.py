from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import QueryDict
from User.models import *
from .models import *
from .forms import *
from django.views.decorators.cache import cache_control
#from django.views.decorators import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def landing(request,pk):
	user = request.user
	#print(user)
	#print(user.username)
	blogs = Blog.objects.filter(created_by=user).order_by('-modified_date')
	#print('blogs = '+ str(len(blogs)))
	#print('user = '+str(user))

	if (len(blogs)==0):
		text = 'You have not posted anything yet. Create your first Blog'

	#print('text = '+text)
	#print('Call received for - '+str(user.username))
	return render(request, 'Blog/Homepage.html',{'user':user,'blog':blogs})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def post_blog(request):
	user = request.user
	#print('Call received from ajax')
	#print('user : '+str(user.pk))
	#print('Hit')
	form = BlogForm(user)
	if request.method == 'POST':
		form_data = QueryDict(request.POST['form'].encode('ASCII'))
		form = BlogForm(user,form_data)
		print('hit')
		if form.is_valid():
			blog = Blog()
			blog.created_by = user
			blog.category = form.cleaned_data.get('category')
			blog.content = form.cleaned_data.get('content')
			blog.title = form.cleaned_data.get('title')
			blog.modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
			blog.save()
			blog.refresh_from_db()
			return redirect('Blog:landing',pk=user.id)

		
	
	return render(request, 'Blog/create_blog.html',{'form':form,'user':user.pk})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def edit_blog(request,pk):
	print('pK = '+str(pk))
	user = request.user
	blog = Blog.objects.get(id=pk)
	print('Blog - '+str(blog))
	if request.method == 'GET':
		print('GET')
		initial={'category': blog.category, 'title' : blog.title, 'content': blog.content }
		form = EditBlogForm(user,initial=initial)

	if request.method == 'POST':
		form_data = QueryDict(request.POST['form'].encode('ASCII'))
		print(form_data)
		form = EditBlogForm(user,form_data)
		print('hit from edit form.')
		if form.is_valid():
			print(form.cleaned_data)
			if (blog.category != form.cleaned_data.get('category') or (blog.content != form.cleaned_data.get('content')) or (blog.title != form.cleaned_data.get('title'))):
				blog.modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
			blog.category = form.cleaned_data.get('category')
			blog.content = form.cleaned_data.get('content')
			blog.title = form.cleaned_data.get('title')
			blog.save()
			blog.refresh_from_db()
			return redirect('Blog:landing',pk=user.id)

	return render(request, 'Blog/edit_blog.html',{'form':form,'b':blog}) 


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def view_blogs(request):
	user = request.user
	users = [u['follows'] for u in UserProfile.objects.filter(user=request.user).values('follows')]
	#users1 = [(u.id,u) for u in User.objects.all()]
	#print(users1)
	blogs = Blog.objects.filter(created_by__in=User.objects.filter(id__in=users))
	#print(blogs)
	print()
	return render(request, 'Blog/view_blogs.html',{'blogs':blogs,'user':user}) 






