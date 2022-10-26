from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts'),
    path('details/<int:id>', views.see_details, name = 'see_details'),
    path('update_post/<int:id>', views.update_post, name = 'update_post')

]