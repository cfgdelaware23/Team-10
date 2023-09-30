from django.forms import ModelForm, DateInput, TimeInput
from .models import Volunteer, Events

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        widgets = {
            'day': DateInput(attrs={'type': 'date'}),
        }


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            'day': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }
