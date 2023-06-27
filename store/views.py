from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from store import models as store_models


class CategoryListView(TemplateView):
    template_name = 'store/category_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = store_models.Category.objects.all()
        return context


class CategoryDetailSubCategoryListView(TemplateView):
    template_name = 'store/category_detail.html'
    
    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(slug=slug, **kwargs)
        context["category_object"] = get_object_or_404(store_models.Category, slug=slug)
        context["subcategories"] = store_models.SubCategory.objects.filter(category=context["category_object"])
        return context


class SubCategoryDetailProductListView(TemplateView):
    template_name = 'store/subcategory_detail.html'
    
    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(slug=slug, **kwargs)
        context["subcategory_object"] = get_object_or_404(store_models.SubCategory, slug=slug)
        context["products"] = store_models.Product.objects.filter(subcategory=context["subcategory_object"])
        return context


class ProductDetailView(TemplateView):
    template_name = 'store/product_detail.html'
    
    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(slug=slug, **kwargs)
        context["product_object"] = get_object_or_404(store_models.Product, slug=slug)
        return context
