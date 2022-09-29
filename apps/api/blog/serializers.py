from rest_framework import serializers

from apps.blog.models import BlogCategory, Article, Tag


class CategoryBlogSerializer(serializers.ModelSerializer):
    meta_title = serializers.CharField(write_only=True)
    meta_description = serializers.CharField(write_only=True)
    meta_keywords = serializers.CharField(write_only=True)
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords'
        )


class ArticleWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price'
        )


class ProductReadSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    def get_main_image(self, obj):
        serializer = ArticleImageSerializer(obj.main_image(), context=self.context)
        return serializer.data

    def get_images(self, obj):
        images = obj.images().exclude(id=obj.main_image().id)
        serializer = ArticleImageSerializer(obj.images(), context=self.context, many=True)
        return serializer.data

    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'categories',
            'main_image',
            'images'
        )


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'image',
            'product',
            'is_main'
        )


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'image',
            'product',
            'is_main'
        )