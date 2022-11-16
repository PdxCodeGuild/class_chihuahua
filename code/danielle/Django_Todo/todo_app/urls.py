from django.urls import path
from . import views
from todo_app import views

urlpatterns = [
    path('', views.todo_item, name = 'todo_item'),
    path('display/', views.todo_item, name = 'display_todo'),
]