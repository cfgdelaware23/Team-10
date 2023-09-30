from django.db import models

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

class Volunteer(models.Model):
    name = models.CharField(default=None, max_length=255)
    days = models.CharField(max_length=255, blank=True) 
    roles = models.CharField(default=None, max_length=255)

    def __str__(self):
        return f"Name: {self.name}, available days: {self.days}, roles: {self.roles}"


class Events(models.Model):
    recurring = models.BooleanField(default=None)
    day = models.DateField(default=None)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    title = models.CharField(default=None, max_length=255)
    account = models.CharField(default=None, max_length=255)
    host = models.CharField(default=None, max_length=255)
    moderator = models.CharField(default=None, max_length=255)
    facilitator = models.CharField(default=None, max_length=255)
    broadcaster = models.CharField(default=None, max_length=255)

    def __str__(self) -> str:
        return f"title: {self.title}, day: {self.day}, time: {self.time}, account: {self.account}"
