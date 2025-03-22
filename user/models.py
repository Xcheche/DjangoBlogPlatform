from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    #profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='default_profile_picture.jpg')
    profile_picture = CloudinaryField("profile", folder="blog_profile_images/",default="https://res.cloudinary.com/df6ndrlj2/image/upload/v1739969127/default_sklyca.png",
                            transformation={"width": 300, "height": 300, "crop": "fill"})

    def __str__(self):
        return self.username
