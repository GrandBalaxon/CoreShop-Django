from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductsListView.as_view(), name="products_list"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", views.ProductDetailsView.as_view(), name="product_details"),
    path("product/add/", views.ProductCreateView.as_view(), name="add_product"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="edit_product"),
]
