from django.contrib import admin
from django.urls import path, include

from todo.views import SignUpView, logout_view

urlpatterns = [

    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", SignUpView.as_view(), name='signup'),
    path("accounts/logout/", logout_view, name='logout'),

    path('', include("todo.urls"))
]
