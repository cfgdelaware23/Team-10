from django.shortcuts import render, HttpResponse
from .forms import VolunteerForm, EventsForm
from .models import Events, Volunteer, Registration
import smtplib, ssl

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

def send_email(recipient):
    sender_email = "acbcfg2023@gmail.com"
    password = "jive koth yflp zdqi"
    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()


    subject = "ACB Update"
    body = "Thank you so much for signing up! ACB appreciates you."
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
            user = Volunteer.objects.get(name='Rob 1')

            if event_id:
                event = Events.objects.get(pk=event_id)
                
                Registration.objects.create(volunteer=user, event=event)
                # Call to the email sending
                email = volunteer.email
                send_email(email)
                # send_email(email)
                return HttpResponse("Successfully applied for the event!")
            
            return HttpResponse("Volunteer information saved successfully!")

    else:
        form = VolunteerForm()

    context = {'form': form}
    return render(request, 'register_volunteer.html', context)