from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

data_mywatchlist = MyWatchList.objects.all()
context = {
    'mywatchlist' : data_mywatchlist,
    'nama': 'Carlene Annabel',
    'student_id': '2106752211'
}
def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
