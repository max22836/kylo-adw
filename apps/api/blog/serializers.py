from rest_framework import serializers

from apps.blog.models import BlogCategory, Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
            'tags',
        )


class ArticleWriteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=64), write_only=True)
    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'image',
            'title',
            'text_preview',
            'text',
            'tags',
        )