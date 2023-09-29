from django.db import models


class Volunteer(models.Model):
    name = models.TextField()
    day = models.DateField()
    roles = models.TextField()

    def __str__(self) -> str:
        return f"Name: {self.name}, available day: {self.day}, roles: {self.roles}"


class Events(models.Model):

    recurring = models.BooleanField()
    day = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.TextField()
    account = models.TextField()
    host = models.TextField()
    moderator = models.TextField()
    facilitator = models.TextField()
    broadcaster = models.TextField()

    def __str__(self) -> str:
        return f"title: {self.title}, day: {self.day}, time: {self.time}, account: {self.account}"
