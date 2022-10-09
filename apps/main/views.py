from django.shortcuts import render
from django.shortcuts import render

from apps.main.mixins import DetailListViewBreadCrumbsMixin
from apps.main.models import Page, ProductSet


def home(request):
    products_sets = ProductSet.objects.filter(is_active=True)
    return render(request, 'index.html', {'products_sets': products_sets})


class PageView(DetailListViewBreadCrumbsMixin):
    model = Page
    template_name = 'main/page.html'

    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True)
        return queryset

    def set_bread_crumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs
