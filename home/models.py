from distutils.command.upload import upload


from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
  
  
  
class Slide(models.Model):
    imageSlide = models.ImageField(upload_to='slide_pic')
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    body = RichTextField(blank=True, null=True)
    
class  Dest(models.Model):
    title = models.CharField(max_length=200)
    created =models.DateTimeField(auto_now=True)
    body = RichTextField(blank=True, null=True)
    descImage=models.ImageField(upload_to='page_pic')
    active = models.BooleanField(default=True)


class  Client(models.Model):
    Image_client= models.ImageField(upload_to='pic_client')
    created =models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

class Mission(models.Model):
    title = models.CharField(max_length=200)
    image_about= models.ImageField(upload_to='mission_pict')
    desc= RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)    

class Objective(models.Model):
    title = models.CharField(max_length=200)
    objImage = models.ImageField(upload_to = 'pic_object')
    desc = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
class Goal(models.Model):
    title = models.CharField(max_length=200)
    goImage = models.ImageField(upload_to = 'pic_goal')
    desc = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='port_image')
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now= True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'portfolio'
        verbose_name_plural = 'portfolio'
    
    
    
class Apps(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='app_image')
    Desc = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Apps'
        verbose_name_plural = 'Apps'
    
        

class Weps(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='web_image')
    Desc = RichTextField(blank= True, null=True)
    active = models.BooleanField(default=True)

    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Webs'
        verbose_name_plural = 'Webs'
    

class Wep1 (models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='web1_image')
    Desc = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Wep1'
        verbose_name_plural = 'Wep1'
    