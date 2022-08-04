from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail','created_at']
    list_display_links = ['id', 'title', 'image_tag_thumbnail']


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag_thumbnail', 'image']
    readonly_fields = ['image_tag']

    @admin.register(Tag)
    class TagAdmin(admin.ModelAdmin):
        list_display = ['name']
