from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Category, SubCategory, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'store/category_list.html'
    paginate_by = 5
    
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
