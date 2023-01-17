from django.urls import path
from .views import TodoListView, ToDoListCreateView, TodoListUpdate

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('add/todo/', ToDoListCreateView.as_view(), name='add_todo'),
    path('todo/<int:pk>/update/', TodoListUpdate.as_view(), name='todo_update')
]
