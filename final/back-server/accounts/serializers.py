# serializers.py

from .models import *
from rest_framework import serializers


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['follower', 'followee']