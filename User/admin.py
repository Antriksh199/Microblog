from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	pass

class CountryAdmin(admin.ModelAdmin):
	pass


class StateAdmin(admin.ModelAdmin):
	pass


class CityAdmin(admin.ModelAdmin):
	pass


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(State,StateAdmin)