# serializers.py
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

User = get_user_model()

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
    
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['follower', 'followee']