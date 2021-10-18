from django.shortcuts import render, redirect
from .forms import DiscrepancyForm

def addDiscrepancy(request):
    form = DiscrepancyForm()
    if request.method == "POST":
        form = DiscrepancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraftList')

    context = {'form': form}
    return render(request, 'discrepancies/discrepancy_form.html', context)
