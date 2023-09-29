from django.db import models


class Volunteer(models.Model):
    name = models.TextField(default=None)
    day = models.DateField(default=None)
    roles = models.TextField(default=None)

    def __str__(self) -> str:
        return f"Name: {self.name}, available day: {self.day}, roles: {self.roles}"


class Events(models.Model):
    recurring = models.BooleanField(default=None)
    day = models.DateField(default=None)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    title = models.TextField(default=None)
    account = models.TextField(default=None)
    host = models.TextField(default=None)
    moderator = models.TextField(default=None)
    facilitator = models.TextField(default=None)
    broadcaster = models.TextField(default=None)

    def __str__(self) -> str:
        return f"title: {self.title}, day: {self.day}, time: {self.time}, account: {self.account}"
