from django.urls import path
from .views import Index, Update, Add, Delete, Details, ApiAuth


urlpatterns = [
    path("getToken", ApiAuth.as_view(), name="get_token"),
    path("products", Index.as_view(), name="api_all"),
    path("products/add", Add.as_view(), name="api_add"),
    path("products/<str:pk>", Details.as_view(), name="api_details"),
    path("products/<str:pk>/update", Update.as_view(), name="api_update"),
    path("products/<str:pk>/delete", Delete.as_view(), name="api_delete"),
]
