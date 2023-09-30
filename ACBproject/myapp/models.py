from django.db import models

CHOICES = [
    ('Host', 'Host'),
    ('Moderator', 'Moderator'),
    ('Facilitator', 'Facilitator'), 
    ('Streamer', 'Streamer'), 
    ('Broadcaster', 'Broadcaster'),
]

   

class Events(models.Model):
    recurring = models.BooleanField(default=None)
    day = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    title = models.CharField(default=None, max_length=255)
    account = models.CharField(default=None, max_length=255)
    host = models.CharField(default=None, max_length=255)
    moderator = models.CharField(default=None, max_length=255, blank=True, null=True)
    facilitator = models.CharField(default=None, max_length=255, blank=True, null=True)
    streamer = models.CharField(default=None, max_length=255, blank=True, null=True)
    broadcaster = models.CharField(default=None, max_length=255, blank=True, null=True)
    # registrations = models.ManyToManyField(Volunteer, through='Registration')

    def __str__(self) -> str:
        return f"title: {self.title}, account: {self.account}"
   
 
class Volunteer(models.Model):
    name = models.CharField(default=None, max_length=255)
    roles = models.CharField(choices=CHOICES, default=None, max_length=255)
    email = models.EmailField(max_length=255, default=None)
    events = models.ManyToManyField(Events)


    def __str__(self) -> str:
        return f"Name: {self.name}, role: {self.roles}" 
    
class Registration(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.name} registered for {self.event.day} - {self.event.host}"

