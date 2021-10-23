from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

@login_required(login_url='login')
def addEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.GET['next'] if 'next' in request.GET else 'aircraftList')

    context = {'form': form}
    return render(request, 'events/event_form.html', context)

@login_required(login_url='login')
def viewEditEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.GET['next'] if 'next' in request.GET else 'aircraftList')

    context = {'form': form}
    return render(request, 'events/event_form.html', context)
