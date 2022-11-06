from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='todo'),
    path('list', views.list, name='list')
]