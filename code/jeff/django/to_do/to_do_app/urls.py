from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.list_index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('new/', views.new, name = 'new'),
    path('edit/<str:pk>', views.edit, name = 'edit'),
]
