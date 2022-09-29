from rest_framework import serializers

from apps.blog.models import BlogCategory, Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    meta_title = serializers.CharField(write_only=True)
    meta_description = serializers.CharField(write_only=True)
    meta_keywords = serializers.CharField(write_only=True)
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )


