from django.shortcuts import render, HttpResponse
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer, Registration
import smtplib
import ssl

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
    social_events = Events.objects.filter(type_of_event='social')
    educational_events = Events.objects.filter(type_of_event='educational')
    return render(request, 'display_events.html', {'data': data})


def register_events(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register_events.html', context)


def send_email(recipient, event):
    sender_email = "acbcfg2023@gmail.com"
    password = "jive koth yflp zdqi"
    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()

    subject = "ACB Update"
    body = f"Thank you so much for signing up for {event.title} from \
{event.start_time} to {event.end_time} on {event.day}! ACB appreciates you."
    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, message)

        print("Email sent. ")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server.quit()


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
                # return render(request, 'confirm.html')
            return HttpResponse("Volunteer information saved successfully!")

    else:
        form = VolunteerForm()

    return render(request, 'register_volunteer.html', {'form': form})


def home(request):
    return render(request, 'homepage.html')
