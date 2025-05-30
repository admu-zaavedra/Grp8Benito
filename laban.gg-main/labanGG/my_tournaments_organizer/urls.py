from django.urls import path
from .views import my_tournaments_organizer, edit_tournament
from my_tournaments_organizer import views

urlpatterns = [
    path('', my_tournaments_organizer, name='my_tournaments_organizer'),
    path('edit_tournament/<int:tournament_id>/', views.edit_tournament, name='edit_tournament'),  
]

app_name = "my_tournaments_organizer"