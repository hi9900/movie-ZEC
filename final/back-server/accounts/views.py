from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view

from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def is_admin(request, user_id):
    user = User.objects.get(id=user_id)
    is_admin = user.is_superuser or user.is_staff
    return JsonResponse({'is_admin': is_admin})


@api_view(['GET'])
def check_nickname(request, nickname):
    if User.objects.filter(nickname=nickname).exists():
        return Response({'message': '중복된 닉네임입니다.', 'result': False})
    return Response({'message': '회원가입이 가능한 닉네임입니다.', 'result': True})


@api_view(['GET'])
def check_email(request, email):
    if User.objects.filter(email=email).exists():
        return Response({'message': '중복된 이메일입니다.', 'result': False})
    return Response({'message': '회원가입이 가능한 이메일입니다.', 'result': True})


@api_view(['POST'])
def follow(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({'message': '팔로우 성공', 'result': True})

@api_view(['POST'])
def unfollow(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': '팔로우 취소', 'result': True})

@api_view(['GET'])
def following(request, user_id):
    user = User.objects.get(id=user_id)
    following_list = user.following.all()
    data = []
    for user in following_list:
        data.append({'id': user.id, 'username': user.username})
    return Response({'following': data})

@api_view(['GET'])
def followers(request, user_id):
    user = User.objects.get(id=user_id)
    followers_list = user.followers.all()
    data = []
    for user in followers_list:
        data.append({'id': user.id, 'username': user.username})
    return Response({'followers': data})

@api_view(['POST'])
def block_user(request, user_id):
    user_to_block = User.objects.get(id=user_id)
    request.user.blocked_users.add(user_to_block)
    return Response({'message': '차단 완료', 'result': True})

@api_view(['POST'])
def unblock_user(request, user_id):
    user_to_unblock = User.objects.get(id=user_id)
    request.user.blocked_users.remove(user_to_unblock)
    return Response({'message': '차단 해제 완료', 'result': True})