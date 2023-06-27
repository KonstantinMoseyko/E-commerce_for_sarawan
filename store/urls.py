from django.urls import path

from store import views
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailSubCategoryListView.as_view(), name='category_detail'),
    path('subcategory/<slug:slug>/', views.SubCategoryDetailProductListView.as_view(), name='subcategory_detail'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    #     "subcategories/<int:pk>/products/<int:pk>/",
    #     views.CoursesDetailView.as_view(),
    #     name="courses_detail",),
]


# extra_patterns = [
#     path("reports/", credit_views.report),
#     path("reports/<int:id>/", credit_views.report),
#     path("charge/", credit_views.charge),
# ]

# urlpatterns = [
#     path("", main_views.homepage),
#     path("help/", include("apps.help.urls")),
#     path("credit/", include(extra_patterns)),
# ]