from django.shortcuts import render
# appname/views.py
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from join_tournament.models import TournamentPlayer

def index(request):
    return HttpResponse('Hello World! This came from the index view')

class ProfileView(DetailView):
    model = TournamentPlayer
    template_name = 'player_profile/player_profile.html'

    def get_context_data(self, **kwargs): #Add this to determine which base_account.html to display
        context = super().get_context_data(**kwargs)
        context['base_template'] = 'base_organizer.html' if self.request.user.isOrganizer else 'base_attendee.html'
        return context
# Create your views here.
