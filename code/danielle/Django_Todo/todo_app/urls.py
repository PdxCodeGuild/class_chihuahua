from django.urls import path
from .views import display_todo
from todo_app import views

urlpatterns = [
    path('', views.todo_item, name="todo_item"),
    path('redirect/', views.display_todo, name="display_todo")
]