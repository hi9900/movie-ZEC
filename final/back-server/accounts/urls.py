# from django.urls import path, include
# from . import views

# from rest_framework_simplejwt.views import TokenObtainPairView

# app_name = 'accounts'

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('login/', TokenObtainPairView), # login jwt 토큰 발급
#     path('follow/<str:username>/', views.follow, name='follow'),
#     # path('<int:user_id>/', views.profile, name='profile'),
#     path('<str:username>/', views.profile, name='profile'),
# ]

from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('gnk/', include('allauth.urls')), # google, naver, kakao
    # gnk/logout을 post로 가야 로그아웃됨
    
    # path('login/', obtain_jwt_token), # login jwt 토큰 발급
    # path('follow/<str:username>/', views.follow, name='follow'),
    # path('<int:user_id>/', views.profile, name='profile'),
    # path('<str:username>/', views.profile, name='profile'),
]