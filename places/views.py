from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import PlaceForm
from django.contrib import messages
from .filters import PlaceFilter
from places.models import Place


# Create your views here.

def index(request):
    return render(request, 'index.html')


def sortCity(request):
    filter_based_on_city = PlaceFilter(request.GET, queryset=Place.objects.all())
    return render(request, 'places/sortcity.html', {'filter' : filter_based_on_city})
    



def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            messages.success(request, 'Place added successfully.')
            return redirect('places:index')
    else:
        form = PlaceForm()
    
    return render(request, 'places/add_place.html', {"form":form})

class PlacesListView(generic.ListView):
    model = Place

class PlacesDetailView(generic.DetailView):
    model = Place