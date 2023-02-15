import email
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        
        return super(PublishedManager, self).get_queryset().filter(status= 'published')
    
    
    

class Post(models.Model):
        STATUS_CHOICE= (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
        title = models.CharField(max_length=250)
        tags = TaggableManager()
        slug = models.SlugField(max_length=250,unique_for_date='publish')
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
        blockImage = models.ImageField(upload_to='blogImage', null=True , blank=True)
        body = RichTextField(blank=True, null=True)
        publish = models.DateTimeField(default = timezone.now)
        created = models.DateTimeField(auto_now=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
        objects = models.Manager()
        
        published = PublishedManager()
        
    
        class Meta:
            ordering = ('-publish',)
        def __str__(self):
             return self.title
        
        
        def get_absolute_url(self):
            return reverse('blog:postDetail', args=[
            self.publish.year, self.publish.month, self.publish.day, self.slug
            ])
        
        # Model for comments


class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comments')
    name = models.CharField(max_length=250)
    email= models.EmailField()
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default= True)
    
    
    class Meta:
        ordering = ('created',)
    def __str__(self):
     return f'Comment by {self.name} on {self.post}'

class Slider(models.Model):
    slideImage= models.ImageField(upload_to='SlidePic')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add= True)
    body = RichTextField(blank=True, null=True)
        
