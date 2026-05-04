from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = []
