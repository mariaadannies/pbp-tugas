# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_CatalogItem

app_name = 'katalog'

urlpatterns = [
    path('', show_CatalogItem, name='show_CatalogItem'),
]   