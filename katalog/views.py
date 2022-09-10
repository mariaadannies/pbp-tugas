from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_CatalogItem(request):
    return render(request, "katalog.html", context)

data_katalog = CatalogItem.objects.all()
context = {
    'list_katalog': data_katalog,
    'name': "Maria Aurellia",
    'id': "2106750862",
}