from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomTokenObtainPairView, OnlyAuthenticatedUserView

urlpatterns = [
    # 일반 회원 회원가입/로그인
    path('', include('django.contrib.auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    # 회원가입
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/authonly/', OnlyAuthenticatedUserView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # gnk/logout을 post로 가야 로그아웃됨
    path('gnk/', include('allauth.urls')), # google, naver, kakao

    # 관리자 확인
    path('api/is-admin/<int:user_id>/', views.is_admin, name='is_admin'),

    #  중복확인
    path('check-email/<str:email>/', views.check_email),
    path('check-username/<str:username>/', views.check_username),

    # 팔로우
    path('api/follow/<int:user_id>/', views.follow),
    path('api/unfollow/<int:user_id>/', views.unfollow),
    path('api/following/<int:user_id>/', views.following),
    path('api/followers/<int:user_id>/', views.followers),
    
    # 차단 확인/생성/취소
    path('api/block-user/<int:user_id>/', views.block_user),
    path('api/unblock-user/<int:user_id>/', views.unblock_user),

    # 프로필
    path('users/<str:username>/', views.profile)

    # path("register/", RegisterAPIView.as_view()), # post - 회원가입
    # path("auth/", AuthAPIView.as_view()), # post - 로그인, delete - 로그아웃, get - 유저정보
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
