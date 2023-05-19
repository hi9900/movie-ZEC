from django.urls import path
from . import views
from .views import MovieListCreate


urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
]