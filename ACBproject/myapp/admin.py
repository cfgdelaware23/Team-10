from django.contrib import admin
from .models import Events, Volunteer, Registration
# Register your models here.
admin.site.register(Events)
admin.site.register(Volunteer)
admin.site.register(Registration)