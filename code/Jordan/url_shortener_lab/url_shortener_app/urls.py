from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('url/', views.create, name = 'create'),
    path('shorturl/', views.random_, name = 'shortened')
]