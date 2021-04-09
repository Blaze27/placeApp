from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from places.models import Place

def index(request):
    return render(request, 'index.html')

def sortCity(request):
    return render(request, 'sortcity.html')

class PlacesListView(generic.ListView):
    model = Place

class PlacesDetailView(generic.DetailView):
    model = Place