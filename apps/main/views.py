from django.shortcuts import render

from apps.main.mixins import DetailListViewBreadCrumbsMixin
from apps.main.models import Page


class PageView(DetailListViewBreadCrumbsMixin):
    model = Page
    template_name = 'main/page.html'

    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True)
        return queryset

    def set_bread_crumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs


class ContactsView(DetailListViewBreadCrumbsMixin):
    model = Page
    template_name = 'main/contacts_page.html'

    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True)
        return queryset

    def set_bread_crumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs
