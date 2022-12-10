from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.data_collection, name='add')

]