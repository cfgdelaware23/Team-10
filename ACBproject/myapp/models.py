from django.db import models

CHOICES = [
    ('Host', 'Host'),
    ('Moderator', 'Moderator'),
    ('Facilitator', 'Facilitator'), 
    ('Streamer', 'Streamer'), 
    ('Broadcaster', 'Broadcaster'),
]
class Volunteer(models.Model):
    name = models.CharField(default=None, max_length=255)
    day = models.DateField(default=None, max_length=255)
    roles = models.CharField(choices=CHOICES, default=None, max_length=255)

    def __str__(self) -> str:
        return f"Name: {self.name}, available day: {self.day}, roles: {self.roles}"


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

    def __str__(self) -> str:
        return f"title: {self.title}, day: {self.day}, time: {self.time}, account: {self.account}"
