from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    # character = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200)


class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


# 배우 : 영화(영화감독) = M : N
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    original_language = models.CharField(max_length=10, null=True)
    original_title = models.CharField(max_length=100, null=True)
    overview = models.TextField(null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    backdrop_path = models.CharField(max_length=200, null=True)
    runtime = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)
    # actors = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    # director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    keywords = models.ManyToManyField(Keyword)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies') #, null=True) # 좋아요
    # user.article_set에서 article_set이 유저가 작성한 글인지, 좋아요를 누른 글인지를 알 수 없게된다. 따라서 동일한 모델에서 위와 같이 진행 할 때는 반드시 역참조를 해줘야한다. 만약 위와같은 상황에서 migrations를 하면 relate_name을 추가하라고 코드에 뜬다.


class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character = models.CharField(max_length=50)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')
    watch_movie = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watched_movies') #, null=True) # 본 영화 
    title = models.CharField(max_length=100)
    content = models.TextField()
    hashtags = models.ManyToManyField(Tag, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews') #, null=True) # 좋아요
    watched_at = models.DateTimeField(default=timezone.now) # default로 현재시간, 변경 가능
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)]) # 0.5 단위 값만 가질 수 있음

    def save(self, *args, **kwargs):
        self.rating = round(self.rating * 2) / 2  # Round to nearest half point
        super().save(*args, **kwargs)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)