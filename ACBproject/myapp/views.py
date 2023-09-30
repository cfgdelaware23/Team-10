from django.shortcuts import render, HttpResponse
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer, Registration

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_events(request):
    return render(request, 'display_events.html')

def register_events(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'register_events.html', context)

# def volunteer(request):
#     form = VolunteerForm()
#     if request.method == 'POST':
#         form = VolunteerForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'register_volunteer.html', context)

# Assuming you have a view where volunteers apply for events

def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)


        if form.is_valid():
            volunteer = form.save()

            event_id = request.POST.get('events')
            user = Volunteer.objects.get(name='Rob 1')

            if event_id:
                event = Events.objects.get(pk=event_id)
                
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

    context = {'form': form}
    return render(request, 'register_volunteer.html', context)

# def volunteer(request):
#     if request.method == 'POST':
#         form = VolunteerForm(request.POST)
#         if form.is_valid():
#             # Save the volunteer information
#             volunteer = form.save()

#             # Check if there's an event_id in the POST data (assuming you pass it in your form)
#             event_id = request.POST.get('event_id')

#             if event_id:
#                 # Get the event for which the volunteer is applying
#                 event = Events.objects.get(pk=event_id)

#                 # Check if the volunteer is not already registered for the event
#                 if not Registration.objects.filter(volunteer=volunteer, event=event).exists():
#                     # Create a new registration entry to associate the volunteer with the event
#                     Registration.objects.create(volunteer=volunteer, event=event)
#                     return HttpResponse("Successfully applied for the event!")

#                 return HttpResponse("You are already registered for this event.")

#             return HttpResponse("Volunteer information saved successfully!")

#     else:
#         form = VolunteerForm()

#     context = {'form': form}
#     return render(request, 'register_volunteer.html', context)

# from django.shortcuts import get_object_or_404

# def apply_for_event(request, event_id):
#     # Get the volunteer who is applying (you might need to handle user authentication here)
#     volunteer = get_object_or_404(Volunteer, id=request.user.id)

#     # Get the event for which the volunteer is applying
#     event = get_object_or_404(Events, id=event_id)

#     # Check if the volunteer is not already registered for the event
#     if not Registration.objects.filter(volunteer=volunteer, event=event).exists():
#         # Create a new registration entry to associate the volunteer with the event
#         Registration.objects.create(volunteer=volunteer, event=event)
#         return HttpResponse("Successfully applied for the event!")

#     return HttpResponse("You are already registered for this event.")

# # You can create a URL pattern and link it to this view to handle volunteer applications.
