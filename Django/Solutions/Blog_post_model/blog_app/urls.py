from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('add/', views.add_blog, name='add'),
   path('list/', views.blog_list, name='list'),
   path('delete_post/<int:id>', views.delete_post, name='delete_post'),
   path('post_details/<int:id>', views.post_details, name='post_details'),
   path('update_post/<int:id>', views.update_post, name='update_post'),
   path('search_post/', views.search_post, name='search_post')


]