# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    # 게시글
    path('', views.article_list),
    path('<int:article_id>/', views.article_detail),
    path('<int:article_id>/like/', views.update_like_article),
    
    # 게시글 댓글
    path('<int:article_id>/article-comments/', views.comment_list),
    path('article-comments/<int:article_comment_id>/', views.comment_detail),
    
    # 대댓글
    path("<int:article_id>/article-comments/<int:parent_id>/replies/", views.reply_list),
]
