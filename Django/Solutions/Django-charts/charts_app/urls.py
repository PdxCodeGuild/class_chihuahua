from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/products/', views.product_list),
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart')
]

urlpatterns = format_suffix_patterns(urlpatterns)
