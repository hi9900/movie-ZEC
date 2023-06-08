from django.contrib import admin
from .models import Movie, Genre, Actor, Director, Keyword

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Keyword)