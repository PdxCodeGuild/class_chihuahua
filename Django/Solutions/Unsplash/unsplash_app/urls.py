from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_images, name = 'get_images'),
    path('api/images/', views.image_list),
    path('add_pictures/<int:id>', views.add_pictures, name = 'add_pictures'),
    path('board/', views.my_board, name = 'board'),
    path('delete/<int:id>', views.delete, name='delete')

]