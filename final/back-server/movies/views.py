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


class MovieListCreate(APIView):
    # 전체 영화 조회 -> 이제안써
    def get(self, request):
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 30)
        movies = Movie.objects.order_by('-popularity')
        count = movies.count()
        paginator = Paginator(movies, page_size)
        total_pages = paginator.num_pages  # 전체 페이지 수
        try:
            movies_page = paginator.page(page)
        except:
            return Response({"detail": "Invalid page."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MovieSerializer(movies_page, many=True)
        response = {
        "page": page, 
        "total_pages": total_pages,
        'count': count,
        "data": serializer.data, 
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def search_movies(request):
    queryset = Movie.objects.all()
    filter = MovieFilter(request.GET, queryset=queryset)
    movies = filter.qs.order_by('-popularity')
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


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie) #, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
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
        
    

# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         comments = get_list_or_404(Comment)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk):
#     # comment = Comment.objects.get(pk=comment_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# # 영화 좋아요
# class MovieViewSet(viewsets.ModelViewSet): 
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     @action(detail=True, methods=['post'])
#     def like(self, request, pk=None):
#         movie = self.get_object()
#         user = request.user
#         movie.like_users.add(user)
#         return Response({'status': 'like set'})

#     @action(detail=True, methods=['post'])
#     def unlike(self, request, pk=None):
#         movie = self.get_object()
#         user = request.user
#         movie.like_users.remove(user)
#         return Response({'status': 'like removed'})
    

# # 영화 좋아요 목록
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_liked_movies(request):
#     user = request.user
#     liked_movies = user.liked_movies.all()
#     serializer = MovieSerializer(liked_movies, many=True)
#     return Response(serializer.data)


# # 리뷰 좋아요
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

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


# # 리뷰 좋아요 목록
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_liked_reviews(request):
#     user = request.user
#     liked_reviews = user.liked_reviews.all()
#     serializer = ReviewSerializer(liked_reviews, many=True)
#     return Response(serializer.data)