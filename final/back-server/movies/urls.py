from django.urls import path
from . import views
from .views import MovieListCreate


urlpatterns = [
    path('movies/', views.MovieListCreate.as_view()),
    path('movies/search/', views.search_movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    # path('reviews/', views.review_list),
    path('movies/<int:movie_id>/reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('reviews/<int:review_pk>/comments/', views.comment_create),
]