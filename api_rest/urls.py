from django.urls import path
from .views import Index, Update, Add, Delete, Details


urlpatterns = [
    path("products", Index.as_view(), name="all"),
    path("products/add", Add.as_view(), name="add"),
    path("products/<str:pk>", Details.as_view(), name="details"),
    path("products/<str:pk>/update", Update.as_view(), name="update"),
    path("products/<str:pk>/delete", Delete.as_view(), name="delete"),
]
