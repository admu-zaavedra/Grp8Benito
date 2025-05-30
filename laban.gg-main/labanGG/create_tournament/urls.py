from django.urls import path
from .views import create_tournament

urlpatterns = [
    path('createtournament/', create_tournament, name='create_tournament'),
]
