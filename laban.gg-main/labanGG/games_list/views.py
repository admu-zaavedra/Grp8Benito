from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Game

class GamesListView(ListView):
    model = Game
    template_name = 'games_list/index.html'

    def get_context_data(self, **kwargs): #Add this to determine which base_account.html to display
        context = super().get_context_data(**kwargs)
        context['base_template'] = 'base_organizer.html' if self.request.user.isOrganizer else 'base_attendee.html'
        return context

class GamesDetailView(DetailView):
    model = Game
    template_name = 'games_list/tournaments_per_game.html'

    def get_context_data(self, **kwargs): #Add this to determine which base_account.html to display
        context = super().get_context_data(**kwargs)
        context['base_template'] = 'base_organizer.html' if self.request.user.isOrganizer else 'base_attendee.html'
        return context

class GamesSearchView(ListView):
    model = Game
    template_name = 'games_list/index.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(title__icontains=query).order_by('title')
    
    def get_context_data(self, **kwargs): #Add this to determine which base_account.html to display
        context = super().get_context_data(**kwargs)
        context['base_template'] = 'base_organizer.html' if self.request.user.isOrganizer else 'base_attendee.html'
        return context

def TournamentsListView(request):
    game = Game.objects.filter(title=self.kwargs['title'])
    query = request.GET.get('q')
    tournaments = Tournament.objects.filter(name=game)
    if query:
            tournaments = tournaments.filter(Q(name__icontains=query))  # Filter tournaments by name

    return render(request, 'tournaments_per_game.html', {'tournaments': tournaments})

