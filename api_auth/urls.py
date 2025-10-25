from django.urls import path
from .views import Login, Register
from . import views

urlpatterns = [
   path("login", Login.as_view(), name="login"),
   path("register", Register.as_view(), name="register"),
   path("logout", views.logout_view, name="logout")

]