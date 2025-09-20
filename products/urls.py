from .views import product_index, product_detail, category_detail, category_index
from django.urls import path

app_name = 'products'

urlpatterns = [
    path("products/", product_index, name='product_index'),
    path("products/<int:pk>/", product_detail, name='product_detail'),
    path("categories/", category_index, name='category_index'),
    path("categories/<int:pk>/", category_detail, name='category_detail'),
]