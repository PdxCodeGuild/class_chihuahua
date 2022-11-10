from django.urls import path
from . import views

urlpatterns = [
  
#  views.<needs to be name of function in views.py in app 
    path('', views.home, name="home"),
    path('update/<int:id>', views.update, name='update'),
    path('add/', views.add_todo, name='add'),
    path('show/', views.show_todo, name='show'),
    path('remove/<int:id>', views.remove_todo, name='remove')
]