from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from apps.api.user.serializers import TokenSerializer

from apps.blog.models import BlogCategory, Article, Tag, Comment, User
from config.settings import PAGE_NAMES


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list_categories.html',
                  {'categories': blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog'], 'current': category.name}
    return render(
        request,
        'blog/article/list.html',
        {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs}
    )


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {
        reverse('blog_category_list'): PAGE_NAMES['blog'],
        reverse('article_list', args=[category.id]): category.name,
        'current': article.title
    }
    return render(
        request,
        'blog/article/view.html',
        {'article': article, 'category': category, 'breadcrumbs': breadcrumbs}
    )


def tag_search_article_list(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    # articles = Article.objects.filter(tags=tag_id)
    articles = Article.objects.filter(tags__in=[tag_id])
    breadcrumbs = {
        reverse('blog_category_list'): PAGE_NAMES['blog'],
        'current': tag.name
    }
    return render(
        request,
        'blog/article/tag_search.html',
        {'articles': articles, 'tag': tag, 'breadcrumbs': breadcrumbs}
    )


def comment_view(request, comment_id, article_id):
    comment = Comment.objects.get(id=comment_id)
    article = Article.objects.get(id=article_id)
    user = request.user
    if request.user.is_authenticated:
        user.comment_set(is_checked=True)
        return render(request, 'blog/comment/comment_added.html')
    else:
        user.comment_set(is_checked=False)
        return 'Залогинся сначала'
