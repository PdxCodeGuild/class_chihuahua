from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_as_fav/<int:id>', views.mark_as_fav, name='mark_as_fav'),
    path('fav_list/', views.fav_list, name='fav_list')
]