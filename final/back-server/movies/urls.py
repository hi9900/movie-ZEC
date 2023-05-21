from django.urls import path
from . import views
from .views import MovieListCreate

urlpatterns = [
    path('movies/directors/<str:director_id>/', views.movie_list_by_director),
    # path('movies/actors/<str:actor_id>/', views.movie_list_by_actor),
    path('movies/genres/<str:genre_id>/', views.movie_list_by_genre),
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('reviews/<int:review_pk>/comments/', views.comment_create),
]