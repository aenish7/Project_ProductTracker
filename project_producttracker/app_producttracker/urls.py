from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_index, name="product.index"),
    path('products/create/', views.product_create, name="product.create"),
]

