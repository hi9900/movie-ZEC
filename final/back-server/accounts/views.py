from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from .models import *
from .serializers import *


# Create your views here.

class FollowViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = FollowSerializer