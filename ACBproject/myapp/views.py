from django.shortcuts import render, HttpResponse
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer, Registration
from .email_sender import send_email
from django.http import JsonResponse

# Create your views here.


def run_email_script(request):
    if request.method == 'POST':
        # Call the function from script.py
        message = send_email("juskeerat@gmail.com")
        return JsonResponse({'status': 'success', 'message': message})
    else:
        return JsonResponse({'status': 'failed', 'message': 'Not a POST request'})


def index(request):
    return render(request, 'index.html')


def display_events(request):
    data = Events.objects.all()
    social_events = [
        event for event in data if event.type_of_event == 'social']
    educational_events = [
        event for event in data if event.type_of_event == 'educational']
    return render(request, 'display_events.html', {'data': data}, {'social': social_events}, {'educational': educational_events})


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
                email = "juskeerat@gmail.com"
                send_email(email)
                return HttpResponse("Successfully applied for the event!")
            return HttpResponse("Volunteer information saved successfully!")

    else:
        form = VolunteerForm()

    return render(request, 'register_volunteer.html', {'form': form})


def home(request):
    return render(request, 'homepage.html')
