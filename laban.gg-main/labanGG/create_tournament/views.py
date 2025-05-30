from django.shortcuts import render, redirect
from .forms import TournamentForm
from .models import Tournament
from register.models import Account

def create_tournament(request):
    user = request.user
    if user.isOrganizer == False:
        return redirect('/log_in/')
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.game = form.cleaned_data['game']  # Associate with the selected game

            # Set the tournament organizer to the current user's username
            tournament.tournament_organizer = user.username
            
            # Check if image is provided
            if 'image' not in request.FILES:
                # If no image provided, assign a default image
                tournament.image = "tournament_images/labanlogo.png"

            tournament.save()
            return redirect('/games/')
    else:
        form = TournamentForm()
    return render(request, 'create_tournament.html', {'form': form, 'user': user})
