from django.urls import path
from .views import display_todo, completed_list
from todo_app import views

urlpatterns = [
    path('', views.todo_item, name="todo_item"),
    path('display/', views.display_todo, name="display_todo"),
    path('completed/', views.completed_list, name="completed_list")
]