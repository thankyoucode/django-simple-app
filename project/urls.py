from django.contrib import admin
from django.urls import include, path

from inventory.views import index

urlpatterns = [
    path("", index, name="index"),
    path("user/", include("users.urls")),
    path("inventory/", include("inventory.urls")),
    path("admin/", admin.site.urls),
]
