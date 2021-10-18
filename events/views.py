from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def addEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form': form}
    return render(request, 'events/event_form.html', context)

def viewEditEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form': form}
    return render(request, 'events/event_form.html', context)
