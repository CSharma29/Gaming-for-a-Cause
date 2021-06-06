from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
import Pillow

# Create your models here.

class game_post(models.Model):
    title = models.CharField(max_length=500, default=None, null=False)
    discreption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpeg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile' 
