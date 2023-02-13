from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import settings
# Create your models here.


class UserProfile(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50)
    profile_pic = models.ImageField(blank=True)