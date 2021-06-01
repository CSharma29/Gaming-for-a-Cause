from django.db import models
from django.db.models.base import Model

# Create your models here.

class game_post(models.Model):
    title = models.CharField(max_length=500, default=None, null=False)
    discreption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
