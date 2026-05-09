from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductsListView.as_view(), name="products_list"),
    path("contacts/", views.contacts, name="contacts"),
    path("product/<int:product_id>/", views.product_details, name="product_details"),
    path("add-product/", views.add_product, name="add_product"),
]
