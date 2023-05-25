from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from .models import *
from .serializers import *
from .filters import *

import random


class IsAuthenticatedPostOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# Create your views /rializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 감독, 장르, 영화 랜덤으로 영화 찾기: 30개씩
@api_view(['GET'])
def movie_lists_random(request):
    # 랜덤 감독
    director = get_list_or_404(Director)
    random_director = random.choice(director)
    movies_d = list(Movie.objects.filter(director__id=random_director.id).order_by('-popularity')[:30])
    director_data = get_object_or_404(Director, pk=random_director.id)
    serializer_dm = MovieSerializer(movies_d, many=True)
    serializer_dd = DirectorSerializer(director_data)

    # 랜덤 장르
    genre = get_list_or_404(Genre)
    random_genre = random.choice(genre)
    movies_g = list(Movie.objects.filter(genres__id=random_genre.id).order_by('-popularity')[:30])
    genre_data = get_object_or_404(Genre, pk=random_genre.id)
    serializer_gm = MovieSerializer(movies_g, many=True)
    serializer_gg = GenreSerializer(genre_data)

    # 랜덤 배우
    actor = get_list_or_404(Actor)
    random_actor = random.choice(actor)
    # 배우 별로 전체 movie list
    movies_a = list(Movie.objects.filter(characters__actor__id=random_actor.id).order_by('-popularity')[:30])
    actor_data = get_object_or_404(Actor, pk=random_actor.id)
    serializer_am = MovieSerializer(movies_a, many=True)
    serializer_aa = ActorSerializer(actor_data)

    response = {
        'director_movies': {
            'director': serializer_dd.data,
            'data': serializer_dm.data,
        },
        'genre_movies' :{
            'genre': serializer_gg.data,
            'data': serializer_gm.data,
        },
        'actor_movies': {
            'actor': serializer_aa.data,
            'data': serializer_am.data
        }
    }
    return Response(response, status=status.HTTP_200_OK)


# 감독별 영화 찾기
@api_view(['GET'])
def movie_list_by_director(request, director_id):
    page = request.query_params.get('page', 1)

    # 감독 별로 전체 movie list
    movies = Movie.objects.filter(director__id=director_id).order_by('-popularity')
    director_data = get_object_or_404(Director, pk=director_id)

    # 페이지네이션 설정
    paginator = Paginator(movies, 30)  # 한 페이지당 30개의 영화 표시
    movies_paginated = paginator.get_page(page)

    serializer = MovieSerializer(movies_paginated, many=True)
    serializer_d = DirectorSerializer(director_data)

    response = {
        'director_data': serializer_d.data,
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)


# 배우별 영화 찾기
@api_view(['GET'])
def movie_list_by_actor(request, actor_id):
    page = request.query_params.get('page', 1)

    actor = get_list_or_404(Actor)
    # 배우 별로 전체 movie list
    movies = list(Movie.objects.filter(characters__actor__id=actor.id).order_by('-popularity'))
    
    # 랜덤 20개 추출하기 (20개 보다 작다면 그만큼만)
    # num_movies = min(20, len(movies))
    # random_movies = random.sample(movies, num_movies)
    
    serializer = MovieSerializer(movies, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# 장르별 영화 찾기
@api_view(['GET'])
def movie_list_by_genre(request, genre_id):
    # 장르 별로 전체 movie list
    movies = list(Movie.objects.filter(genres__id=genre_id).order_by('-popularity'))
    
    # 랜덤 20개 추출하기 (20개 보다 작다면 그만큼만)
    # num_movies = min(20, len(movies))
    # random_movies = random.sample(movies, num_movies)
    
    serializer = MovieSerializer(movies, many=True)
    genre_data = get_object_or_404(Genre, pk=genre_id)
    serializer_g = GenreSerializer(genre_data)
    response = {
        'genre_data': serializer_g.data,
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)


class MovieListCreate(APIView):
    def get(self, request):
        genres = get_list_or_404(Genre)
        serializers_g = GenreSerializer(genres, many=True)

        keyword = get_list_or_404(Keyword)
        serializers_k = KeywordSerializer(keyword, many=True)

        response = {
            'genres': serializers_g.data,
            'keyword': serializers_k.data
        }
        return Response(response)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 영화 상세
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# 영화 검색
@api_view(['GET'])
def search_movies(request):
    queryset = Movie.objects.all()
    # get 매개변수 기준으로 검색된 필터
    filter = MovieFilter(request.GET, queryset=queryset)

    # movie_id 순
    # movies = filter.qs

    # popularity를 기준으로 많은순 정렬(내림)
    if request.GET.get('ordering') == 'popularity_desc':
        movies = filter.qs.order_by('-popularity')
    # popularity를 기준으로 정렬(으름)
    elif request.GET.get('ordering') == 'popularity_asc':
        movies = filter.qs.order_by('popularity')
    # 개봉일 기준 오래된 순 정렬
    elif request.GET.get('ordering') == 'release_date_asc':
        movies = filter.qs.order_by('release_date')
    # 개봉일 기준 최신순 정렬
    elif request.GET.get('ordering') == 'release_date_desc':
        movies = filter.qs.order_by('-release_date')
    # 런타임 기준 정렬 긴 순
    elif request.GET.get('ordering') == 'runtime_desc':
        movies = filter.qs.order_by('-runtime')
    # 런타임 기준 정렬 짧은 순
    elif request.GET.get('ordering') == 'runtime_asc':
        movies = filter.qs.order_by('runtime')
    # 평점 수가 많고 평점이 좋은 순
    # elif request.GET.get('ordering') == 'vote_average':
    else:
        movies = filter.qs.order_by('-vote_count', '-vote_average')

    # 전체 검색된 영화 수
    count = movies.count()

    # Paginator 객체 생성
    paginator = Paginator(movies, 30)  # 한 페이지에 표시할 객체의 개수 설정
    # GET 매개변수에서 페이지 검색
    page = request.GET.get('page', 1)
    # 해당 페이지의 객체 목록 반환
    filtered_movies = paginator.page(page)

    serializer = MovieSerializer(filtered_movies.object_list, many=True)
    response = {
        'current_page': filtered_movies.number,
        'total_pages': filtered_movies.paginator.num_pages,
        'count': count,
        'data': serializer.data
    }
    return Response(response)

##########################
# admin 사이트로는 됨 
# list
@api_view(["GET", "POST"])
def movie_list_create(request):
    if request.method == "GET":
        movie_lists = get_list_or_404(MovieList)
        # movie_lists = MovieList.objects.filter(user=request.user)
        serializer = MovieListSerializer(movie_lists, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def movie_list_detail_update_delete(request, list_id):
    try:
        movie_list = MovieList.objects.get(id=list_id)
    except MovieList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MovieListSerializer(movie_list)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MovieListSerializer(movie_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##########################


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedPostOnly])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        reviews = list(Review.objects.filter(movie__id=movie_id).order_by('-created_at'))
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 댓글
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'GET':
        comments = list(Comment.objects.filter(review__id=review_id, parent_comment__isnull=True).order_by('-created_at'))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
# 대댓글
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def reply_list(request, review_id, parent_id):
    review = get_object_or_404(Review, id=review_id)
    comment = get_object_or_404(Comment, id=parent_id)
    
    if request.method == 'GET':
        comments = list(Comment.objects.filter(parent_comment__id=parent_id).order_by('created_at'))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user, parent_comment=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 영화 좋아요 목록
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_liked_movies(request):
    user = request.user
    liked_movies = user.liked_movies.all()
    serializer = MovieSerializer(liked_movies, many=True)
    return Response(serializer.data)

# 리뷰 좋아요여부 변경
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    user = request.user
    
    # 이미 좋아요한 경우 취소
    if user in review.like_users.all():
        review.like_users.remove(user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_200_OK)
    
    # 없는 경우 좋아요
    else:
        review.like_users.add(user)
        return Response({"message": "좋아요 성공"}, status=status.HTTP_200_OK)


# 영화 좋아요 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    
    # 이미 좋아요한 경우 취소
    if user in movie.like_users.all():
        movie.like_users.remove(user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_200_OK)
    
    # 없는 경우 좋아요
    else:
        movie.like_users.add(user)
        return Response({"message": "좋아요 성공"}, status=status.HTTP_200_OK)


# 유저 정보
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)


# # 리뷰 좋아요
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     authentication_classes = [TokenAuthentication]

#     @action(detail=True, methods=['post'])
#     def like(self, request, pk=None):
#         review = self.get_object()
#         user = request.user
#         review.like_users.add(user)
#         return Response({'status': 'like set'})

#     @action(detail=True, methods=['post'])
#     def unlike(self, request, pk=None):
#         review = self.get_object()
#         user = request.user
#         # review.likes.remove(user)   ##### 원래 코드인데 내가 맞다 생각해서 밑으로 고쳤는데 안되면 다시 ㄱㄱ
#         review.like_users.remove(user)
#         return Response({'status': 'like removed'})


# 리뷰 좋아요 목록
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_liked_reviews(request):
    user = request.user
    liked_reviews = user.liked_reviews.all()
    serializer = ReviewSerializer(liked_reviews, many=True)
    return Response(serializer.data)