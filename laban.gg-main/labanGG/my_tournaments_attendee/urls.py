from django.urls import path
from .views import my_tournaments_attendee

urlpatterns = [
    path('', my_tournaments_attendee, name = 'my_tournaments_attendee'),
]

app_name = "my_tournaments_attendee"