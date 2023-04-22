from django.urls import path,include
from .views import *


app_name = "User"

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('ajax/load_cities/',load_cities,name='load_cities'),
    path('ajax/load_states/',load_states,name='load_states'),
    path('landing/',landing,name='landing'),
    path('logout/',Logout_view,name='Logout_view'),
    path('login/',Login_view,name='Login_view'),
    path('edit_user/<int:pk>',edit_profile,name='EditProfile')
]