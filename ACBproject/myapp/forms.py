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
    account = forms.ChoiceField(choices=[('com', 'com'),
                                        ('com2', 'com2'),
                                        ('com3', 'com3'),
                                        ('com4', 'com4'),
                                        ('ch', 'ch'),
                                        ('web ch', 'web ch'),
                                        ('n/a', 'n/a'),
                                        ], widget=forms.Select(attrs={'class': ' '}))
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': ''}),
            'day': DateInput(attrs={'type': 'date', 'class': ''}),
            'start_time': TimeInput(attrs={'type': 'time', 'class': ''}),
            'end_time': TimeInput(attrs={'type': 'time', 'class': ''}),
            'account': forms.TextInput(attrs={'class': ''}),
            'host': forms.TextInput(attrs={'class': ' '}),
            'moderator': forms.TextInput(attrs={'class': ' '}),
            'facilitator': forms.TextInput(attrs={'class': ' '}),
            'streamer': forms.TextInput(attrs={'class': ' '}),
            'broadcaster': forms.TextInput(attrs={'class': ' '})
        }
