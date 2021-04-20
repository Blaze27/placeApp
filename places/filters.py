import django_filters
from .models import Place

class PlaceFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = {
            'city' : ['icontains'],
        }