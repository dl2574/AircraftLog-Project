from django.shortcuts import render, redirect
from .models import Aircraft, Mod
from .forms import AircraftForm, ModForm

def aircraftList(request):
    aircraft = Aircraft.objects.all()

    context = {'aircraft': aircraft}
    return render(request, 'Aircraft/aircraftList.html', context)


def aircraft(request, pk):
    airframe = Aircraft.objects.get(serial_number=pk)

    context = {'airframe':airframe}
    return render(request, 'Aircraft/aircraft.html', context)

def addAircraft(request):
    form = AircraftForm()

    if request.method == "POST":
        form=AircraftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form':form}
    return render(request, 'Aircraft/add_aircraft_form.html', context)

def editAircraftMods(request, pk):
    airframe = Aircraft.objects.get(serial_number=pk)
    form = AircraftForm(instance=airframe)

    if request.method == "POST":
        form = AircraftForm(request.POST, instance=airframe)
        if form.is_valid():
            form.save()
            return redirect('aircraft', pk)

    context = {'form': form, 'airframe': airframe}
    return render(request, 'Aircraft/edit_aircraft_mods.html', context)

def addMod(request):
    form = ModForm()
    page = 'add'

    if request.method == "POST":
        form = ModForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form': form, 'page': page}
    return render(request, 'Aircraft/add_mod.html', context)

def viewEditMod(request, pk):
    mod = Mod.objects.get(tcto=pk)
    form = ModForm(instance=mod)
    page = 'view'

    if request.method == "POST":
        form = ModForm(request.POST, instance=mod)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form': form, 'mod': mod, 'page': page}
    return render(request, 'Aircraft/add_mod.html', context)