from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('createVM/', views.createVM, name='createVM'),
    path('deleteVM/', views.deleteVM, name='deleteVM'),
    path('collectVM/', views.collectVM, name='collectVM'),
    path('powerOn/', views.powerOn, name='powerOn'),
    path('powerOff/',views.powerOff, name='powerOff'),
    path('edit/', views.edit, name='edit'),
    path('editVM/', views.editVM, name='editVM')
]