from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

import json


# 게시글
@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = list(Article.objects.order_by('-created_at')[:20])
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        password = json.loads(request.body).get('password')
        if password == article.password:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
        password = json.loads(request.body).get('password')
        print(article.password, password)
        if password == article.password:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"message" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)




# 게시글 댓글
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def comment_list(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        article_comments = list(
            ArticleComment.objects.filter(article__id=article_id, parent_comment__isnull=True).order_by('-created_at'))
        serializer = ArticleCommentSerializer(article_comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 댓글
@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, article_comment_id):
    article_comment = get_object_or_404(ArticleComment, id=article_comment_id)

    if request.method == 'GET':
        serializer = ArticleCommentSerializer(article_comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        password = json.loads(request.body).get('password')
        if password == article_comment.password:
            article_comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
        password = json.loads(request.body).get('password')
        if password == article_comment.password:
            serializer = ArticleCommentSerializer(article_comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"message" : "비밀번호가 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)
        
# 게시글 대댓글
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def reply_list(request, article_id, parent_id):
    article = get_object_or_404(Article, id=article_id)
    article_comment = get_object_or_404(ArticleComment, id=parent_id)

    if request.method == 'GET':
        article_comments = list(ArticleComment.objects.filter(parent_comment__id=parent_id).order_by('created_at'))
        serializer = ArticleCommentSerializer(article_comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, parent_comment=article_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 좋아요 여부 변경
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user

    # 이미 좋아요한 경우 취소
    if user in article.like_users.all():
        article.like_users.remove(user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_200_OK)

    # 없는 경우 좋아요
    else:
        article.like_users.add(user)
        return Response({"message": "좋아요 성공"}, status=status.HTTP_200_OK)