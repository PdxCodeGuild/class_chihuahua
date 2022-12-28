
from django.urls import path, include
from django.contrib import admin
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')), 
    path('blogs/', views.blog_posts, name='blogs'),
    path('add/', views.add_post, name='posts'),
    path('about/', views.about, name='about'),
    path('delete/', views.delete_post, name='delete_post'),
    path('details/', views.see_details, name='see_details')
]
