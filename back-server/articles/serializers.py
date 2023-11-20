from rest_framework import serializers
from .models import *


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ArticleCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('article', 'created_at', 'updated_at')
                            
    def get_replies(self, obj):
        replies = obj.article_replies.all()
        serializers = ArticleCommentSerializer(replies, many=True)
        return serializers.data


class ArticleSerializer(serializers.ModelSerializer):
    comments = ArticleCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')