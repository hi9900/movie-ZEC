from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.TextField(blank=False)
    writer = models.TextField(blank=False)
    password = models.TextField(blank=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)  # 좋아요
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class ArticleComment(models.Model):
    writer = models.TextField(blank=False)
    password = models.TextField(blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='article_replies', null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id