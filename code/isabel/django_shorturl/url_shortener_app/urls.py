from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_all, name = 'show'),
    path('', views.enter_url, name = 'enter'),
]


