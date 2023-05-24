from django.urls import path
from . import views
from .views import MovieListCreate

urlpatterns = [
    path('movies/', views.MovieListCreate.as_view()),
    path('movies/search/', views.search_movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/<int:movie_id>/like/', views.update_like_movie),

    # 감독, 장르, 배우 조회
    path('movies/directors/<int:director_id>/', views.movie_list_by_director),
    path('movies/actors/<int:actor_id>/', views.movie_list_by_actor),
    path('movies/genres/<int:genre_id>/', views.movie_list_by_genre),
    # 키워드 조회 추가


    path('movies/random/', views.movie_lists_random),

    path("movie_lists/", views.movie_list_create),
    path("movie_lists/<int:list_id>/", views.movie_list_detail_update_delete),

    # 리뷰
    # path('reviews/', views.review_list),
    path('movies/<int:movie_id>/reviews/', views.review_list),
    path('reviews/<int:review_id>/', views.review_detail),
    path('reviews/<int:review_id>/like/', views.update_like_review),
    # path('reviews/<int:review_pk>/unlike/', views.unlike),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('reviews/<int:review_pk>/comments/', views.comment_create),
    # path('liked_reviews/', views.get_liked_reviews),
    path('user/detail/<int:user_id>/', views.user_detail_view, name='user_detail'),
    
    
    # 리뷰 댓글
    path('reviews/<int:review_id>/comments/', views.comment_list),
    path('comments/<int:comment_id>/', views.comment_detail),
    
    # 대댓글
    path("reviews/<int:review_id>/comments/<int:parent_id>/replies/", views.reply_list),
]