from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sensors, Image, Command
# Register your models here.

class CMD(admin.ModelAdmin):
	list_display = ('cmd','mH','mL')
	list_filter = ('cmd',)
	search_fields = ['cmd','mH']

class Just(admin.ModelAdmin):
	list_display = ('name','create')
	list_filter = ('name',)
	search_fields = ['name','create']
class Cunit(admin.ModelAdmin):
	list_display = ('light','humidity','temperature','flowrate1','flowrate2','distance','soil_moisture','created')
	list_filter = ('soil_moisture',)
	search_fields = ['soil_moisture','distance']
admin.site.register(Sensors,Cunit)

admin.site.register(Image,Just)
admin.site.register(Command,CMD)
