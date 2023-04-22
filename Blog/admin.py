from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	pass

class LikeAdmin(admin.ModelAdmin):
	pass


class ShareAdmin(admin.ModelAdmin):
	pass


class CommentAdmin(admin.ModelAdmin):
	pass



admin.site.register(Blog,BlogAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Share,ShareAdmin)
admin.site.register(Comment,CommentAdmin)
