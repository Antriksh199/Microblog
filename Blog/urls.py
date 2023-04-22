from django.urls import path,include
from .views import *

app_name = 'Blog'

urlpatterns = [
    path('main/<int:pk>/',landing,name='landing'),
    path('main/newblog/',post_blog,name='Postblog'),
    path('edit/<int:pk>/',edit_blog,name='EditBlog'),
    path('view/blogs/',view_blogs,name='ViewBlog')
]