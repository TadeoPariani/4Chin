from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("home", views.user_list, name="home"),
]