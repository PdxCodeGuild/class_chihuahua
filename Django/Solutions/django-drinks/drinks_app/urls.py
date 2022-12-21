from django.urls import path
from . import views

urlpatterns = [
   path('', views.all_drinks, name='all'),
   path('favs', views.fav_drinks, name='favs'),
   path('mark_as_fav/<int:id>', views.mark_as_fav, name='mark_as_fav')
]
