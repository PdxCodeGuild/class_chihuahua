from . import views
from django.urls import path

urlpatterns = [
   path('', views.add_reporter, name='add_reporter'),
   path('add_article', views.add_article, name='add_article'),
   path('view_all', views.view_all, name='view_all')

]