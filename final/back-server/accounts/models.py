from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    blocked_users = models.ManyToManyField('self', symmetrical=False, related_name='blocked_by', blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)