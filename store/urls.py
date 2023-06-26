from django.urls import path

from store import views
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    # path("subcategories/<int:pk>/products/", views.CoursesListView.as_view(), name="courses"),
    # path(
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