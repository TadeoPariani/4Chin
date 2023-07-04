from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("home/<str:usernameLogin>", views.home, name="home"),
    path("delete_post/<int:post_id>/<str:username>", views.delete_post, name="delete_post"),
    path("make_comment/<int:post_id>/<str:username>", views.make_comment, name="make_comment"),
]