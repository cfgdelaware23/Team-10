from django.shortcuts import render, redirect
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_events(request):
    data = Events.objects.all()
    return render(request, 'display_events.html', {'data': data})


def register_events(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register_events.html', context)


def volunteer(request):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< Updated upstream
    context = {'form': form}
    return render(request, 'register_volunteer.html', context)
def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.days = ",".join(form.cleaned_data['days'])
            volunteer.save()
            return redirect('home')
    else:
        form = VolunteerForm()
    return render(request, 'register_volunteer.html', {'form': form})
=======
    context = {'form':form}
    return render(request, 'register_volunteer.html', context)

def home(request):
    return render(request, 'homepage.html')
>>>>>>> Stashed changes
