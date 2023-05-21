from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# 하 simplejwt 머임 ㅆ....
# from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    email = request.data.get('email')

	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def login(request):


# @api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def follow(request, username):

#     person = get_object_or_404(get_user_model(), username=username)
#     user = request.user
#     if person != user:
#         if user.following.filter(pk=person.pk).exists():
#             user.following.remove(person)
#             follow = False
#         else:
#             user.following.add(person)
#             follow = True
#         follow_status ={
#             'follow':follow,
#             'count':person.followers.all().count(),  # change here
#         }
#         return JsonResponse(follow_status)
#     else:
#         return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['get'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def profile(request, username):    
#     person = get_object_or_404(get_user_model(), username=username)
#     context ={
#         'username': person.username,
#         'email': person.email,
#         'created_at': person.date_joined,
#         'followers':person.followers.all().count(),  # change here
#         'followings':person.following.all().count(),  # change here
#         # 'followers': UserSerializer(person.followers, many=True).data,
#         # 'following': UserSerializer(person.following, many=True).data, 팔로잉 한 사람 정보까지 띄우려면 주석해제
#     }
#     return JsonResponse(context)

