from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet, PostViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comentarios', CommentViewSet)
router.register(r'categorias', CategoryViewSet)

urlpatterns = [
    path("", views.register, name="register"),
    path("login", views.login, name="login"),
    path("home/<str:usernameLogin>", views.home, name="home"),
    path("delete_post/<int:post_id>/<str:username>", views.delete_post, name="delete_post"),
    path("make_comment/<int:post_id>/<str:username>", views.make_comment, name="make_comment"),
    path("delete_comment/<int:comment_id>/<str:username>", views.delete_comment, name="delete_comment"),
]

urlpatterns += [
    path('api/', include(router.urls)),
]