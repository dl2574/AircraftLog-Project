from django.urls import path
from . import views

urlpatterns = [
    path('addEvent/', views.addEvent, name='addEvent'),
    path('ViewEdit/<str:pk>', views.viewEditEvent, name='viewEditEvent')
]