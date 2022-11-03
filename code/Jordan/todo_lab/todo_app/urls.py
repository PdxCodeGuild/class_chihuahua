from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('details/<int:id>', views.see_details, name = 'see_details'),
    path('complete_post/<int:id>', views.complete_post, name = 'complete_post')

]