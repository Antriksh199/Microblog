from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def main(request):
	user = request.user
	if user is None or not user.is_authenticated :
		return (render(request, "home/home.html"))
	else:
		return redirect('User:Logout_view')

# Create your views here.
