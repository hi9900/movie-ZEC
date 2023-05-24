from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import permission_classes, api_view, authentication_classes, permission_classes
from rest_framework.views    import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse

from .models import *
from .serializers import *

User = get_user_model()

############################################################
# JWT
class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     token = serializer.validated_data["access"]
    #     username = serializer.validated_data["username"]
    #     response_data = {
    #         "access": token,
    #         "username": username,
    #     }
    #     return Response(response_data)


# 인가된 사용자만 접근할 수 있는 View 생성
class OnlyAuthenticatedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
		
    # JWT 인증방식 클래스 지정하기
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        # Token에서 인증된 user만 가져온다.
        user = request.user
        print(f"user 정보 : {user}")
        if not user:
            return Response({"error": "접근 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Accepted"})


############################################################

@api_view(['GET'])
def is_admin(request, user_id):
    user = User.objects.get(id=user_id)
    is_admin = user.is_superuser or user.is_staff
    return JsonResponse({'is_admin': is_admin})


@api_view(['GET'])
def check_username(request, username):
    if User.objects.filter(username=username).exists():
        return Response({'message': '이미 존재하는 이름입니다.', 'result': False})
    return Response({'message': '회원가입이 가능한 이름입니다.', 'result': True})


@api_view(['GET'])
def check_email(request, email):
    if User.objects.filter(email=email).exists():
        return Response({'message': '이미 존재하는 이메일입니다.', 'result': False})
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

############################################################

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

@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def profile(request, username):    
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    # response = {
    #     'username': user.username,
    #     'email': user.email,
    #     'created_at': user.date_joined,
    #     'followers':user.followers.all().count(),  # change here
    #     'followings':user.following.all().count(),  # change here
        # 'followers': UserSerializer(user.followers, many=True).data,
        # 'following': UserSerializer(user.following, many=True).data, 팔로잉 한 사람 정보까지 띄우려면 주석해제
    # } 
    return Response(serializer.data)
