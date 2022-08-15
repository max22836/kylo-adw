from django.views import generic
from apps.catalog.models import Category


class CatalogIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/index.html'
