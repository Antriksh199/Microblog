from django.urls import path,include
from .views import *

app_name = 'shared'

urlpatterns = [
    path('userlist/',user_list,name='UserList'),
    path('ajax/follow/<int:pk>',follow,name='Follow'),
    path('ajax/unfollow/<int:pk>',unfollow,name='Unfollow'),
    path('ajax/like/<int:pk>',Like,name='Like'),
    path('ajax/unlike/<int:pk>',Unlike,name='Unlike')
]