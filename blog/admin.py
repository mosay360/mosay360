from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('title','slug','author','publish','status')
    ordering=['-created']
    list_filter=('status','publish')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',),'tags':('title',)}
    list_per_page = 10
    raw_id_fields=('author',)
    date_hierarchy= 'publish'
    ordering= ('status', 'publish')
 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('name','email','post','created','active')
    list_filter =('active', 'created', 'updated')
    search_fields = ('name','email','body')
    
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('title','body','created')