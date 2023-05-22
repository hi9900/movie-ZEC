# serializers.py
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(required=True, 
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    profile_image = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'profile_image': self.validated_data.get('profile_image', None)
        }

class UserSerializer(serializers.ModelSerializer):
    # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
    # 비밀번호를 응답에 표현한다면 보안상의 유출이 된다고 함
    password = serializers.CharField(write_only=True)
    # following = serializers.StringRelatedField(many=True)
    # followers = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = '__all__'  # 이거는 디테일하고 구별할때 변경가능

class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # following = serializers.StringRelatedField(many=True)
    # followers = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = '__all__' # 이거는 기본하고 구별할때 변경가능


class UserProfileSerializer(serializers.ModelSerializer):
    # 리뷰랑 코멘트, 무비리스트 시리얼라이저 추가하기 임포트 먼저 해야해
    # reviews = ReviewSerializer(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile_image', 'following', 'blocked_users', 'is_staff']
        # fields = '__all__'
        # read_only_fields = ['email', 'username']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email = validated_data['email'],
#             password = validated_data['password']
#         )
#         return user