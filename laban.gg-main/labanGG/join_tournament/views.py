from django.shortcuts import render, redirect
from .models import TournamentPlayer
from register.models import Account
from create_tournament.models import Tournament

def join_tournament(request, id):
    tournament = Tournament.objects.get(id=id)
    user = request.user
    if user.isOrganizer == True:
        return redirect('/log_in/')
    if request.method == 'POST':
        accountUser = user.username
        ign = request.POST.get('ign')
        age = request.POST.get('age')
        country = request.POST.get('country')

        jt = TournamentPlayer(ign=ign, age=age, country=country, accountUser=accountUser, account=user, tournament=tournament)
        jt.save()

        return render(request, 'join_tournament.html', {'join_tournament': jt, 'user':user})
    
    return render(request, 'join_tournament.html', {'user': user})
