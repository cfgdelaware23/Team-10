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
    body = '''
    <!DOCTYPE html>
<html>
<head>
    <title>Thank You for Volunteering</title>
</head>
<body>
    <p>
        Dear [Volunteer's Name],
    </p>
    
    <p>
        We want to extend our heartfelt gratitude to you for signing up to be a volunteer at our upcoming <strong>[Event Name]</strong>. Your commitment to giving your time and energy to support our cause is truly inspiring, and we can't wait to work together to make this event a resounding success.
    </p>

    <p>
        Your willingness to step up and lend a hand is invaluable to us, and it's people like you who make our mission possible. Your dedication to our cause is a testament to the power of community and the positive change that we can create when we come together.
    </p>

    <p><strong>Here's what you can expect next:</strong></p>
    <ol>
        <li><strong>Orientation:</strong> In the coming days, we will send you an orientation package that includes all the details you need to know about the event, your role, and any training or materials you may require.</li>
        <li><strong>Team Assignments:</strong> You will be assigned to a dedicated team of fellow volunteers. This will be a fantastic opportunity to connect with like-minded individuals who share your passion for our cause.</li>
        <li><strong>Upcoming Meetings:</strong> We will be organizing regular meetings to ensure that everyone is on the same page and feels prepared for the event. Your input and ideas are always welcome.</li>
        <li><strong>Stay Informed:</strong> Keep an eye on your inbox and our social media channels for updates, news, and exciting announcements about the event.</li>
    </ol>

    <p>
        Once again, thank you for joining us on this journey to make a positive impact. Your involvement means the world to us, and we can't wait to see the incredible contributions you'll bring to our cause.
    </p>

    <p>
        If you have any questions or need further information before our orientation, please don't hesitate to contact us at <a href="mailto:[Email Address]">[Email Address]</a> or [Phone Number]. We're here to support you every step of the way.
    </p>

    <p>
        Thank you for being an essential part of our team, and we look forward to meeting you in person at the <strong>[Event Name]</strong>!
    </p>

    <p>With gratitude,</p>
    <p>[Your Name]<br>[Your Title]<br>[Organization Name]<br>[Contact Information]</p>
</body>
</html>

    '''
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