from django.contrib import admin
from django.urls import path
from .views import register, login, AuthenticatedUser, logout, PermissionsAPIView


urlpatterns = [
    path("register/", register),
    path("login", login),
    path("user", AuthenticatedUser.as_view()),
    path("logout", logout),
    path("permissions", PermissionsAPIView.as_view())
]
