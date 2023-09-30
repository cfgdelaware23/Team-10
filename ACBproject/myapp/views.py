from django.shortcuts import render, HttpResponse
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer, Registration

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
    if request.method == 'POST':
        form = VolunteerForm(request.POST)

        if form.is_valid():
            volunteer = form.save()

            event_id = request.POST.get('events')
            user = Volunteer.objects.get(name=volunteer.name)

            if event_id:
                event = Events.objects.get(pk=event_id)
                role = volunteer.roles.lower()
                setattr(event, role, volunteer.name)
                event.save()
                
                # if Volunteer.objects.filter(name=user, email=e).exists():
                #     print(Volunteer.objects.filter(name=name, email=email).exists())
                #     return HttpResponse("You are already registered for this event.")
                
                # if Registration.objects.filter(volunteer=user, event=event).exists():
                #     print(Registration.objects.filter(volunteer=user, event=event))
                #     return HttpResponse("You are already registered for this event.")
                
                Registration.objects.create(volunteer=user, event=event)
                return HttpResponse("Successfully applied for the event!")
            return HttpResponse("Volunteer information saved successfully!")

    else:
        form = VolunteerForm()

    return render(request, 'register_volunteer.html', {'form': form})

def home(request):
    return render(request, 'homepage.html')
