
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
    path("api/", include("api_rest.urls")),
    path("authorization/", include("api_auth.urls"))
]
