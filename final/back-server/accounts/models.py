from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)

    


# class Follow(models.Model):
    # follower = models.ForeignKey(get_user_model(), related_name='following', on_delete=models.CASCADE)
    # followee = models.ForeignKey(get_user_model(), related_name='followers', on_delete=models.CASCADE)
