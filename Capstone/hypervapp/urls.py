from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('vmlist/', views.vmlist, name = 'vmlist'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('createVM/', views.createVM, name='createVM'),
    path('deleteVM/', views.deleteVM, name='deleteVM'),
    path('collectVM/', views.collectVM, name='collectVM'),
    path('powerOn/<str:vm>', views.powerOn, name='powerOn'),
    path('powerOff/<str:vm>',views.powerOff, name='powerOff'),
    path('edit/', views.edit, name='edit'),
    path('editVM/', views.editVM, name='editVM')
]