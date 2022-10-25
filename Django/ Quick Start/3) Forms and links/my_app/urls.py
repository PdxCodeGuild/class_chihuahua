from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post')

]