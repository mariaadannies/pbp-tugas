from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):    
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_json_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

data_mywatchlist = MyWatchList.objects.all()   
context = {
    'list_watchlist': data_mywatchlist,
    'watched': MyWatchList.objects.filter(watched="Ya").count(),
    'not_watched': MyWatchList.objects.filter(watched="Tidak").count()
}