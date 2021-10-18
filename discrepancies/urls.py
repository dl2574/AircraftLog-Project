from django.urls import path
from . import views

urlpatterns = [
    path('addDiscrepancy/', views.addDiscrepancy,  name='addDiscrepancy'),
]
