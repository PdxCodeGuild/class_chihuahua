from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('url/', views.shortener, name = 'shortener'),
    path('shortened/', views.accepted, name = 'shorten')
]