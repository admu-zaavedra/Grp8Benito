from django.shortcuts import render, redirect, get_object_or_404
from register.models import Account  
from create_tournament.models import Tournament
from create_tournament.forms import TournamentForm  
from django.db.models import Q  # Import Q for complex queries

def my_tournaments_organizer(request):
    user = request.user
    if user.isOrganizer:
        organizer_name = user.username
        query = request.GET.get('q')  # Get the search query from the URL parameters
        tournaments = Tournament.objects.filter(tournament_organizer=organizer_name)

        if query:
            tournaments = tournaments.filter(Q(name__icontains=query))  # Filter tournaments by name

        return render(request, 'my_tournaments_organizer.html', {'tournaments': tournaments})
    else:
        # Handle the case where the user is not a Tournament Organizer
        return redirect('/games/')

def edit_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    form = TournamentForm(request.POST or None, instance=tournament)  
    if form.is_valid():
        form.save()
        return redirect('/my_tournaments_organizer/')  # Redirect to my_tournaments_organizer page after saving
    return render(request, 'edit_tournament.html', {'form': form, 'tournament': tournament})
