from django.forms import ModelForm
from .models import Volunteer, Events

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
