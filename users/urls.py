from django.urls import path

from .views import home, login_user, logout_user, register_user

urlpatterns = [
    path("", home, name="user"),
    path("login", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
]
