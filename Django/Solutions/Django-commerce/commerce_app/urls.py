from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_product, name="add_product"),
    path('all_products/', views.all_products, name='all_products'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart')

]
