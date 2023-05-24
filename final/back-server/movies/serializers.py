from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # model = settings.AUTH_USER_MODEL
        fields = '__all__'


class UsersimplifySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'profile_image')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
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


class CharacterSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    class Meta:
        model = Character
        fields = ('character', 'actor', )


class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('id', 'author', 'content', 'created_at')
        read_only_fields = ('review', 'user')
    
    def get_replies(self, obj):
        replies = obj.replies.all()
        serializers = CommentSerializer(replies, many=True)
        return serializers.data;


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    hashtags = TagSerializer(many=True, read_only=True)
    # like_users = UserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'created_at', 'updated_at')


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MoviesimplifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ('id', 'title', 'release_date', 'poster_path', 'runtime', 'original_title')


##########################
# 되는지 모르겠음
class MovieListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    # 유저 pk로 유저 정보도 저장해서 내보내줘
    # user_name = UserSerializer(read_only=True)
    class Meta:
        model = MovieList
        fields = '__all__'
        read_only_fields = ('user',)
##########################


# class ReviewListSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Review
#         # fields = ('id', 'title', 'content')
#         # fields = ('id', 'title', 'content', 'user', 'username')
#         fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UsersimplifySerializer()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('id', 'author', 'content', 'created_at')
        read_only_fields = ('review', 'user')
    
    def get_replies(self, obj):
        replies = obj.replies.all()
        serializers = CommentSerializer(replies, many=True)
        return serializers.data;


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# class ReviewSerializer(serializers.ModelSerializer):
#     hashtags = TagSerializer(many=True, read_only=True)
#     # like_users = UserSerializer(many=True, read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#     movie = MovieSerializer(read_only=True)

#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('user', 'created_at', 'updated_at')

class ReviewSerializer(serializers.ModelSerializer):
    hashtags = TagSerializer(many=True, read_only=True)
    # like_users = UserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UsersimplifySerializer(read_only=True)
    movie = MoviesimplifySerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class LikeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LikeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'poster_path', 'runtime')  
        # Movie 모델에서 더 필요한거 있으면 fields에 추가


class UserDetailSerializer(serializers.ModelSerializer):
    like_reviews = LikeReviewSerializer(many=True, read_only=True)
    like_movies = LikeMovieSerializer(many=True, read_only=True)
    following = UserSerializer(many=True, read_only=True)
    followers = UserSerializer(many=True, read_only=True)
    following_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'following', 'followers', 'following_count', 'followers_count', 'like_reviews', 'like_movies')
    
    def get_following_count(self, obj):
        return obj.following.count()

    def get_followers_count(self, obj):
        return obj.followers.count()