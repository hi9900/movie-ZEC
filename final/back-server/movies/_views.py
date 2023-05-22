from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, filters

from .models import *
from .serializers import *
from .filters import *

import random

@api_view(['GET'])
def movie_list_by_genre_random(request):
    # 랜덤 장르 추출
    genre = get_list_or_404(Genre)
    random_genre = random.choice(genre)

    # 장르 별로 전체 movie list
    movies = list(Movie.objects.filter(genres__id=random_genre.id).order_by('-popularity'))
    genre_data = get_object_or_404(Genre, pk=random_genre.id)

    # 랜덤 20개 추출하기 (20개 보다 작다면 그만큼만)
    # num_movies = min(20, len(movies))
    # random_movies = random.sample(movies, num_movies)
    
    # 직렬 데이터
    serializer = MovieSerializer(movies, many=True)
    serializer_g = GenreSerializer(genre_data)
    response = {
        'genre_data': serializer_g.data,
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_by_director_random(request):
    director = get_list_or_404(Director)
    random_director = random.choice(director)
    movies = list(Movie.objects.filter(director__id=random_director.id).order_by('-popularity'))
    director_data = get_object_or_404(Director, pk=random_director.id)

    # 랜덤 20개 추출하기 (20개 보다 작다면 그만큼만)
    # num_movies = min(20, len(movies))
    # random_movies = random.sample(movies, num_movies)
    
    # 직렬 데이터
    serializer = MovieSerializer(movies, many=True)
    serializer_d = DirectorSerializer(director_data)
    response = {
        'director_data': serializer_d.data,
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_by_actor_random(request):
    actor = get_list_or_404(Actor)
    random_actor = random.choice(actor)
    # 배우 별로 전체 movie list
    movies_a = list(Movie.objects.filter(characters__actor__id=random_actor.id).order_by('-popularity'))
    actor_data = get_object_or_404(Actor, pk=random_actor.id)
    serializer_am = MovieSerializer(movies_a, many=True)
    serializer_aa = ActorSerializer(actor_data)
    response = {
        'actor_data': serializer_aa.data,
        'data': serializer_am.data
    }
    
    return Response(response, status=status.HTTP_200_OK)