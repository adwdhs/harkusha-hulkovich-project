from django.urls import path
from .views import Index, Update, Add, Delete, Details, Home
urlpatterns = [
    path("", Home.as_view(), name="index"),
    path("products", Index.as_view(), name="home"),
    path("add", Add.as_view(), name="add"),
    path("delete/<str:pk>", Delete.as_view(), name="delete"),
    path("update/<str:pk>", Update.as_view(), name="update"),
    path("details/<str:pk>", Details.as_view(), name="details")
]
