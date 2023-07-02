from django.urls import path

import store.views as store
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', store.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', store.CategoryDetailSubCategoryListView.as_view(), name='category_detail'),
    path('subcategory/<slug:slug>/', store.SubCategoryDetailProductListView.as_view(), name='subcategory_detail'),
    path('product/<slug:slug>/', store.ProductDetailView.as_view(), name='product_detail'),
]
