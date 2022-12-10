from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='list'),
    path('add/', views.todo, name='add'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'remove')
]