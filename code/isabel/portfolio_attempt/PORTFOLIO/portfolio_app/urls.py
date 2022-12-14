from django.urls import path
from . import views

urlpatterns = [
  
#  views.<needs to be name of function in views.py in app 
    path('', views.portfolio_home, name="home"),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('resume', views.resume, name='resume')
]