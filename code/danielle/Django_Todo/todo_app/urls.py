from django.urls import path
from .views import display_todo, completed_list
from todo_app import views
app_name = "todo"

urlpatterns = [
    path('', views.display_todo, name="display_todo"),
    path('create/', views.create, name="create_todo"),
    path('update/<int:id>', views.todo_details, name="update_todo"),
    path('completed/', views.completed_list, name="completed_list"),
]