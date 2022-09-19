from django.shortcuts import render
from katalog.models import CatalogItem
data_katalog_item = CatalogItem.objects.all()
context = {
    'list_katalog': data_katalog_item,
    'nama': 'Carlene Annabel',
    'student_id': '2106752211'
}

def show_catalog(request):
    return render(request, "katalog.html", context)