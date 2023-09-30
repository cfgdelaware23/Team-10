from django.forms import ModelForm
from .models import Volunteer, Events, DAYS_OF_WEEK
from django import forms 


class VolunteerForm(ModelForm):
    days = forms.MultipleChoiceField(
        choices=DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Volunteer
        fields = ['name', 'days', 'roles']


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"

