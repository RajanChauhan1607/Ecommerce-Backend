from django.urls import path
from .views import ProductList, ProductByCategory, TopRatedProducts, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view()),

    #  Category filter
    path('products/category/<str:category>/', ProductByCategory.as_view()),

    #  Top rated
    path('products/top-rated/', TopRatedProducts.as_view()),

    #  Single product
    path('products/<int:pk>/', ProductDetail.as_view()),
]