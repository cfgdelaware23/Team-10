from django.forms import ModelForm, DateInput, TimeInput
from .models import Volunteer, Events
from django.utils import timezone

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        widgets = {
            'day': DateInput(attrs={'type': 'date'}),
            'time_slot': TimeInput(attrs={'type': 'time'}),
        }


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            'day': DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
        }