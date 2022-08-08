from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag
from django.urls import reverse
from django.utils.html import format_html


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail', 'category', 'created_at']
    list_display_links = ['id', 'title', 'image_tag_thumbnail']
    fields = ['category', 'image_tag', 'image', 'tags', 'title', 'text_preview', 'text']
    readonly_fields = ['image_tag']
    list_filter = ['category', 'tags']

    def category_link(self, obj):
        url = reverse('admin:blog_blogcategory_change', args=[obj.category.id])
        return format_html(f"html<a href='{url}'>{obj.category.name}</a>")

    category_link.short_description = 'Категория'

    def tag_links(self, obj):
        tags_links = []
        for tag in obj.tags.all():
            url = reverse('admin:blog_tag_change', args=[tag.id])
            tags_links.append(f"html<a href='{url}'>{tag.name}</a>")
        return format_html(', '.join(tags_links))


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]
