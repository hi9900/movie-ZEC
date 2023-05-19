from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = get_user_model()
        model = settings.AUTH_USER_MODEL
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ('movie', 'actor')

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username')

class ReviewSerializer(serializers.ModelSerializer):
    hashtags = TagSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('movie', 'user', 'watch_movie')


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('review')
