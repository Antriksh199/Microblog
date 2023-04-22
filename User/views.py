from django.shortcuts import render,redirect
from .forms import *
from datetime import datetime
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.cache import cache_control



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def landing(request):
	return render(request, 'User/landing_page.html')

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
	form = SignUpForm()
	if request.method == 'POST':
		form=SignUpForm(request.POST or None)
		if form.is_valid():
			#print(Country.objects.filter(id=int(form.cleaned_data.get('country'))).values('code'))
			#print(form.cleaned_data)
			user = form.save()
			user.refresh_from_db()
			user.username = form.cleaned_data.get('username')
			user.first_name = form.cleaned_data.get('fname')
			user.last_name = form.cleaned_data.get('lname')
			user.email = form.cleaned_data.get('email')
			user.userprofile.first_name = form.cleaned_data.get('fname')
			user.userprofile.last_name = form.cleaned_data.get('lname')
			user.userprofile.email = form.cleaned_data.get('email')
			user.userprofile.contact = form.cleaned_data.get('contact')
			user.userprofile.dob = datetime.strptime(form.cleaned_data.get('dob'),'%Y-%m-%d')
			user.userprofile.state = State.objects.filter(id=int(form.cleaned_data.get('state'))).values('state')
			user.userprofile.city = City.objects.filter(id=int(form.cleaned_data.get('city'))).values('city')
			user.userprofile.country = Country.objects.filter(id=int(form.cleaned_data.get('country'))).values('name')
			user.userprofile.gender = form.cleaned_data.get('gender')
			user.userprofile.education = form.cleaned_data.get('education')
			user.userprofile.interests = (";").join(form.cleaned_data.get('interest'))
			user.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=password)
			login(request, user)
			users = User.objects.all()
			return redirect('Blog:landing',pk=user.id)
 
	return render(request, 'User/signup.html', {'form': form})

def load_cities(request):
    country_id = request.GET.get('state')
    if country_id == 'NA':
    	return render(request, 'User/city_dropdown_list.html')
    cities = City.objects.filter(state_id=country_id).order_by('city')
    return render(request, 'User/city_dropdown_list.html', {'cities': cities})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def Logout_view(request):
	logout(request)
	return redirect('Home:main')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login_view(request):
	status = ''
	if request.method=="POST":
		form = AuthenticationForm(request.POST or None)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is None:
			messages.error(request, 'Login Failed due to Incorrect Credentials')
		else:
			messages.success(request, 'You are logged in as '+username.upper())
			login(request, user)
			return redirect("Blog:landing",pk=user.id)


	else:
		form = AuthenticationForm()
	return render(request,'User/Login.html',{'form':form})


def load_states(request):
    country_id = request.GET.get('country')
    if country_id == 'NA':
    	return render(request, 'User/state_dropdown_list.html')
    #print('coutry is - '+str(country_id))
    states = State.objects.filter(country_id=country_id).order_by('state')
    return render(request, 'User/state_dropdown_list.html', {'states': states}) 


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='User:Login_view')
def edit_profile(request,pk):
	u = UserProfile.objects.get(user=request.user)
	print(u.gender)
	print(u.interests.split(';'))
	if request.method == 'GET':
		initial = {
		'username': u.user.username,
		'email': u.email,
		'fname': u.first_name,
		'lname': u.last_name,
		'contact': u.contact,
		'country': u.country,
		'state': u.state,
		'city': u.city,
		'dob': u.dob,
		'gender': u.gender,
		'education' : u.education,
		'interest' : tuple(u.interests.split(';'))
		}
		form = EditUserForm(initial=initial)
	else:
		form = EditUserForm(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data.get('interest'))
			u.first_name = form.cleaned_data.get('fname')
			u.last_name = form.cleaned_data.get('lname')
			u.email = form.cleaned_data.get('email')
			u.contact = form.cleaned_data.get('contact')
			u.country = form.cleaned_data.get('country')
			u.state = form.cleaned_data.get('state')
			u.city = form.cleaned_data.get('city')
			u.gender = form.cleaned_data.get('gender')
			u.education = form.cleaned_data.get('education')
			u.interests = (";").join(form.cleaned_data.get('interest'))
			u.dob = form.cleaned_data.get('dob')
			u.save()
			return redirect("Blog:landing",pk=u.user.id)
	return render(request, 'User/edit_profile.html',{'form':form,'pk':request.user.pk})