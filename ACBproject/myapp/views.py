from django.shortcuts import render, redirect
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_events(request):
    # fetching details and saving in a dict
    from django.core import serializers
    data = serializers.serialize("python", Events.objects.all())

    context = {
        'data': data,
    }

    return render(request, 'display_events.html', context)

def register_events(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register_events.html', context)


def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'register_volunteer.html', context)
