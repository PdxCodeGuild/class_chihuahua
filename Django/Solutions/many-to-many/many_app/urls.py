from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_team/<int:id>', views.add_to_team, name='add_to_team'),
    path('players/', views.players, name='players'),
    path('teams/', views.teams, name='teams'),

]