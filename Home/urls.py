from django.urls import path,include
from .views import main


app_name='Home'
urlpatterns = [
    path('',main,name="main"),
]