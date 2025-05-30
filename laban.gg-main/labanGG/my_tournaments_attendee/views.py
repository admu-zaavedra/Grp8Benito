from django.shortcuts import render
from join_tournament.models import TournamentPlayer
from create_tournament.models import Tournament
from django.db.models import Q  

def my_tournaments_attendee(request):
    user = request.user
    user_tournaments = TournamentPlayer.objects.filter(account=user, application_status='Accepted')
    query = request.GET.get('q')  

    # Fetch all tournaments
    tournaments = [tournament.tournament for tournament in user_tournaments]

    if query:
        tournaments = [tournament for tournament in tournaments if query.lower() in tournament.name.lower()]

    context = {
        'tournaments': tournaments,
    }

    return render(request, 'my_tournaments_attendee.html', context)
