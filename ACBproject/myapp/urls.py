from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("events/", views.display_events),
    path("register/", views.register_events),
    path("volunteer/", views.volunteer),
]
