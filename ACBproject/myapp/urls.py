from django.urls import path
from . import views
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import run_email_script

urlpatterns = [
    #path("", views.index),
    path("events/", views.display_events),
    path("register/", views.register_events),
    path("volunteer/", views.volunteer),
    path('', home, name='home'),
    path('run-email-script/', run_email_script, name='run_email_script'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

