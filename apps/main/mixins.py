from django.views import generic
from django.db import models


class MetaTagMixin(models.Model):
    name = None
    meta_title = models.CharField(verbose_name='Meta Title', max_length=255, null=True, blank=True)
    meta_description = models.TextField(verbose_name='Meta Description', null=True, blank=True)
    meta_keywords = models.CharField(verbose_name='Meta Keywords', max_length=255, null=True, blank=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.name

    class Meta:
        abstract = True


class ListViewBreadCrumbsMixin(generic.ListView):
    bread_crumbs = {}

    def set_bread_crumbs(self):
        return self.bread_crumbs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListViewBreadCrumbsMixin, self).get_context_data(**kwargs)
        context['breadcrumbs'] = self.set_bread_crumbs()
        return context


class DetailListViewBreadCrumbsMixin(generic.DetailView):
    bread_crumbs = {}

    def set_bread_crumbs(self):
        return self.bread_crumbs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailListViewBreadCrumbsMixin, self).get_context_data(**kwargs)
        context['breadcrumbs'] = self.set_bread_crumbs()
        return context
