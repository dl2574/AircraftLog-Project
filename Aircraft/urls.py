from django.urls import path
from . import views

urlpatterns = [
    path('', views.aircraftList,  name='aircraftList'),
    path('aircraft/<str:pk>/', views.aircraft, name='aircraft'),
    path('add_aircraft/', views.addAircraft, name="addAircraft"),
    path('editAircraftMods/<str:pk>/', views.editAircraftMods, name='editMods'),
]
