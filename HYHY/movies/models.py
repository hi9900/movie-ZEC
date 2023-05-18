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
    title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    # actors = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    # director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    keywords = models.ManyToManyField(Keyword)


class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character = models.CharField(max_length=50)
