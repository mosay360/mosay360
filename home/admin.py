
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display= ('title','imageSlide','created')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= ('Image_client','created','active')
    

@admin.register(Dest)
class DestAdmin(admin.ModelAdmin):
    list_display = ('title', 'descImage','created','active')
    
    
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display=('title', 'image_about','created', 'active')
    
@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display=('title', 'created','image')
    
@admin.register(Apps)
class Apps(admin.ModelAdmin):
    list_display =('title','img','id','active')

@admin.register(Weps)
class Weps(admin.ModelAdmin):
    list_display =('title','img','id', 'active')
    
@admin.register(Wep1)
class Wep1(admin.ModelAdmin):
    list_display =('title','img','id', 'active')

@admin.register(Objective)
class Objective(admin.ModelAdmin):
    list_display= ('title', 'objImage','id','active')


@admin.register(Goal)
class Goal(admin.ModelAdmin):
    list_display= ('title', 'goImage','id','active')