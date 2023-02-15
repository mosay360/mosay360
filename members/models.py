from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    avatar = models.ImageField(upload_to= 'profile_images', default=None)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    # resizing image
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
             