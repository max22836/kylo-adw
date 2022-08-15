from django.views import generic
from apps.catalog.models import Category, Product


class CatalogIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/index.html'

    def get_queryset(self):
        return


class ProductByCategoryView(generic.ListView):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(categories=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductByCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        return context

