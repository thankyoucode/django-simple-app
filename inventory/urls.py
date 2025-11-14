from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<uuid:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<uuid:product_id>/", views.delete_product, name="delete_product"),
]
