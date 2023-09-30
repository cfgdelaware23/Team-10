from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

CHOICES = [
    ('', 'Select Role'),
    ('Host', 'Host'),
    ('Moderator', 'Moderator'),
    ('Facilitator', 'Facilitator'),
    ('Streamer', 'Streamer'),
    ('Broadcaster', 'Broadcaster'),
]

# def validate_future_date(value):
#     if value < timezone.now().date():
#         raise ValidationError('Date cannot be in the past.')

class Events(models.Model):
    title = models.CharField(default=None, max_length=255)
    day = models.DateField(default=None)
    # day = models.DateTimeField(default=None, validators=[validate_future_date])

    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    account = models.CharField(default=None, max_length=255,
                               choices=[('', 'Select Account'),
                                   ('com', 'com'),
                                        ('com2', 'com2'),
                                        ('com3', 'com3'),
                                        ('com4', 'com4'),
                                        ('ch', 'ch'),
                                        ('web ch', 'web ch'),
                                        ('n/a', 'n/a'),
                                        ])
    host = models.CharField(default=None, max_length=255)
    moderator = models.CharField(
        default=None, max_length=255, blank=True, null=True)
    facilitator = models.CharField(
        default=None, max_length=255, blank=True, null=True)
    streamer = models.CharField(
        default=None, max_length=255, blank=True, null=True)
    broadcaster = models.CharField(
        default=None, max_length=255, blank=True, null=True)
    recurring = models.BooleanField(default=None)
    type_of_event = models.CharField(default=None,
                                     max_length=255,
                                     
                                     choices=[
                                         ('', 'Select Type'),
                                         ('Social', 'Social'),
                                              ('Educational', 'Educational')]
                                     )

    def __str__(self) -> str:
        return f"title: {self.title}, account: {self.account}"


class Volunteer(models.Model):
    name = models.CharField(default=None, max_length=255)
    email = models.EmailField(default=None, max_length=255)
    events = models.ManyToManyField(Events)
    roles = models.CharField(choices=CHOICES, default=None, max_length=255)

    def __str__(self) -> str:
        return f"Name: {self.name}, roles: {self.roles}"


class Registration(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.name} registered for {self.event.day} - {self.event.host}"
