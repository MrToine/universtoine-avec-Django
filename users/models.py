from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="default.png")
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    theme = models.CharField(max_length=155, default='default')
    citation = models.CharField(max_length=255, blank=True)
    signature = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    

    def __str__(self):
        return self.user.username
