from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    

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


class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character = models.CharField(max_length=50)
