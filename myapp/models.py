from django.db import models


class Volunteer(models.Model):
    name = models.CharField(max_length=25)
    day = models.DateField()
    roles = models.TextField()

    def __str__(self) -> str:
        return f"Name: {self.name}, available day: {self.day}, roles: {self.roles}"


class Events(models.Model):

    recurring = models.BooleanField()
    day = models.DateField()
    time = models.DateTimeField()
    title = models.TextField()
    account = models.TextField()
    host = models.TextField()

    def __str__(self) -> str:
        return f"title: {self.title}, day: {self.day}, time: {self.time}, account: {self.account}"
