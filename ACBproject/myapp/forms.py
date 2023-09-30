from django.forms import ModelForm, DateInput, TimeInput
from .models import Volunteer, Events
from django import forms

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        # widgets = {
        #     'day': DateInput(attrs={'type': 'date'}),
        #     'time_slot': TimeInput(attrs={'type': 'time'}),
        # }


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-25 d-flex flex-row'}),
            'day': DateInput(attrs={'type': 'date', 'class': 'w-25 d-flex'}),
            'start_time': TimeInput(attrs={'type': 'time', 'class': 'w-25 d-flex'}),
            'end_time': TimeInput(attrs={'type': 'time', 'class': 'w-25 d-flex'}),
            'account': forms.TextInput(attrs={'class': 'w-25 d-flex flex-row'}),
        }
