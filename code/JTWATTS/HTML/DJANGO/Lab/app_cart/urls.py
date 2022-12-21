from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('choice/', views.about, name = 'choice'),
    path('addtocart/', views.addtocart, name = 'addtocart'),
    
]