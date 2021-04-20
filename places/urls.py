from django.urls import path
from . import views

app_name="places"

urlpatterns = [
    path('', views.index, name = "index"),
    path('all_places/', views.PlacesListView.as_view(), name="all_place"),
    path('sort/', views.sortCity, name="sort"),
    path('all_places/<int:pk>', views.PlacesDetailView.as_view(), name = "place-detail"),
]

#  Update urlpatterns for adding new place

urlpatterns += [
    path('add_place', views.add_place, name="add_place"),
]

# Update urlpatterns for adding distinct cities
