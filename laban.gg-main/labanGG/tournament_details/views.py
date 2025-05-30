import random
from django.shortcuts import render, redirect
from create_tournament.models import Tournament
from register.models import Account
from join_tournament.models import TournamentPlayer
from .models import Bracket, Matchup, PlayerInMatchup

# function that will generate the initial matchups for the tournament
def generateMatchups(tournament):
    winnersBracket = Bracket(tournament=tournament, classification="Winners")
    winnersBracket.save()

    if tournament.format == "double_elimination":
        losersBracket = Bracket(tournament=tournament, classification="Losers")
        losersBracket.save()

    players = TournamentPlayer.objects.filter(tournament=tournament)
    players = list(players.filter(application_status="Accepted"))
    random.shuffle(players)

    # first round matchups
    for i in range(0, len(players)-1, 2):
        matchup = Matchup(bracket=winnersBracket, matchNumber=(i//2)+1, status="Ongoing")
        matchup.save()

        player1 = PlayerInMatchup(player=players[i], matchup=matchup, playerNumber=1)
        player1.save()

        player2 = PlayerInMatchup(player=players[i+1], matchup=matchup, playerNumber=2)
        player2.save()


# function that will update the brackets based on the result of a matchup
def updateBrackets(bracket, matchups, matchNumber, winner, loser, context):
    targetMatchup = ""

    if bracket.classification == "Winners":
        if matchNumber == 8 or (matchNumber == 7 and 'losersBracket' not in context):
            winner.ranking = 1
            loser.ranking = 2

            winner.save()
            loser.save()

            tournament = bracket.tournament
            tournament.status = "Ended"
            tournament.save()

        else:
            if matchups.filter(matchNumber=5+(matchNumber-1)//2):
                targetMatchup = matchups.get(matchNumber=5+(matchNumber-1)//2)
                targetMatchup.status = "Ongoing"
            else:
                targetMatchup = Matchup(bracket=bracket, matchNumber=5+(matchNumber-1)//2)

            targetMatchup.save()

            advancingPlayer = PlayerInMatchup(player=winner, matchup=targetMatchup, playerNumber=(matchNumber-1)%2+1)
            advancingPlayer.save()

            if 'losersBracket' not in context:
                if matchNumber < 5:
                    loser.ranking = 5
                elif matchNumber < 7:
                    loser.ranking = 3

                loser.save()

            else:
                losersMatchups = Matchup.objects.filter(bracket=context['losersBracket'])
                
                if matchNumber < 5:
                    if losersMatchups.filter(matchNumber=(matchNumber-1)//2+1):
                        targetMatchup = losersMatchups.get(matchNumber=(matchNumber-1)//2+1)
                        targetMatchup.status = "Ongoing"

                    else:
                        targetMatchup = Matchup(bracket=context['losersBracket'], matchNumber=(matchNumber-1)//2+1)

                    targetMatchup.save()

                    relegatedPlayer = PlayerInMatchup(player=loser, matchup=targetMatchup, playerNumber=(matchNumber-1)%2+1)
                    relegatedPlayer.save()

                elif matchNumber < 7:
                    if losersMatchups.filter(matchNumber=matchNumber//2+1):
                        targetMatchup = losersMatchups.get(matchNumber=matchNumber//2+1)
                        targetMatchup.status = "Ongoing"

                    else:
                        targetMatchup = Matchup(bracket=context['losersBracket'], matchNumber=matchNumber//2+1)

                    targetMatchup.save()

                    relegatedPlayer = PlayerInMatchup(player=loser, matchup=targetMatchup, playerNumber=(matchNumber-1)%2+1)
                    relegatedPlayer.save()

                elif matchNumber == 7:
                    if losersMatchups.filter(matchNumber=6):
                        targetMatchup = losersMatchups.get(matchNumber=6)
                        targetMatchup.status = "Ongoing"

                    else:
                        targetMatchup = Matchup(bracket=context['losersBracket'], matchNumber=6)

                    targetMatchup.save()

                    relegatedPlayer = PlayerInMatchup(player=loser, matchup=targetMatchup, playerNumber=1)
                    relegatedPlayer.save()

    else:
        if matchNumber < 4:
            if matchups.filter(matchNumber=matchNumber+2):
                targetMatchup = matchups.get(matchNumber=matchNumber+2)
                targetMatchup.status = "Ongoing"
            else:
                targetMatchup = Matchup(bracket=bracket, matchNumber=matchNumber+2)

            targetMatchup.save()

            if matchNumber < 3:
                advancingPlayer = PlayerInMatchup(player=winner, matchup=targetMatchup, playerNumber=matchNumber%2+1)
                loser.ranking = 7
            else:
                advancingPlayer = PlayerInMatchup(player=winner, matchup=targetMatchup, playerNumber=1)
                loser.ranking = 5

            advancingPlayer.save()
            loser.save()

        elif matchNumber < 6:
            if matchups.filter(matchNumber=matchNumber+1):
                targetMatchup = matchups.get(matchNumber=matchNumber+1)
                targetMatchup.status = "Ongoing"
            else:
                targetMatchup = Matchup(bracket=bracket, matchNumber=matchNumber+1)

            targetMatchup.save()

            advancingPlayer = PlayerInMatchup(player=winner, matchup=targetMatchup, playerNumber=2)
            advancingPlayer.save()

            loser.ranking = 9 - matchNumber
            loser.save()

        elif matchNumber == 6:
            winnersMatchups = Matchup.objects.filter(bracket=context['winnersBracket'])

            if winnersMatchups.filter(matchNumber=8):
                targetMatchup = winnersMatchups.get(matchNumber=8)
                targetMatchup.status = "Ongoing"
            else:
                targetMatchup = Matchup(bracket=context['winnersBracket'], matchNumber=8)

            targetMatchup.save()

            advancingPlayer = PlayerInMatchup(player=winner, matchup=targetMatchup, playerNumber=2)
            advancingPlayer.save()

            loser.ranking = 3
            loser.save()


# Create your views here.
def tournament_details(request, id):
    context = {}

    tournament = Tournament.objects.get(id=id)
    
    user = request.user
    context['user'] = user
    context['base_template'] = 'base_organizer.html' if user.isOrganizer else 'base_attendee.html'

    if request.POST.get('updateTourneyStatus'):
        if tournament.status == "Upcoming":
            tournament.status = "Pending"
        elif tournament.status == "Pending":
            tournament.status = "Ongoing"
            generateMatchups(tournament)

        elif tournament.status == "Paused":
            tournament.status = "Ongoing"
        elif tournament.status == "Ongoing":
            tournament.status = "Paused"

        tournament.save()

    elif request.POST.get('notStartingYet'):
        tournament.status = "Upcoming"
        tournament.save()

    elif request.POST.get('goToJoinTourney'):
        return redirect(f'/tournament{id}/jointournament/')

    context['tournament'] = tournament

    return render(request, 'tournament_details.html', context)


def brackets(request, id):
    context = {}

    tournament = Tournament.objects.get(id=id)
    user = request.user

    context['tournament'] = tournament
    context['base_template'] = 'base_organizer.html' if user.isOrganizer else 'base_attendee.html'

    brackets = Bracket.objects.filter(tournament=tournament)

    if brackets.count() >= 1:
        winnersBracket = brackets.get(classification="Winners")
        context['winnersBracket'] = winnersBracket
        
        if brackets.count() == 2:
            losersBracket = brackets.get(classification="Losers")
            context['losersBracket'] = losersBracket

    if request.method == "POST":
        for bracket in brackets:
            matchupFound = False

            matchups = Matchup.objects.filter(bracket=bracket)
            ongoingMatchups = matchups.filter(status="Ongoing")

            for matchup in ongoingMatchups:
                matchNumber = matchup.matchNumber
                prefix = ""

                if request.POST.get(f"reportLMatch{matchNumber}Score"):
                    if bracket.classification == "Winners":
                        break
                    else:
                        prefix = "L"
                        matchupFound = True

                elif request.POST.get(f"reportWMatch{matchNumber}Score"):
                    if bracket.classification == "Losers":
                        break
                    else:
                        prefix = "W"
                        matchupFound = True

                if matchupFound:
                    p1score = int(request.POST.get(f"{prefix}m{matchNumber}p1score"))
                    p2score = int(request.POST.get(f"{prefix}m{matchNumber}p2score"))

                    players = PlayerInMatchup.objects.filter(matchup=matchup)
                    player1 = players.get(playerNumber=1)
                    player2 = players.get(playerNumber=2)

                    winner = ""
                    loser = ""

                    if player1.player.account == user or player2.player.account == user:
                        if player1.score == -1 and player2.score == -1:
                            player1.score = p1score
                            player2.score = p2score

                            context['message'] = f"""Successfully reported score ({p1score} - {p2score}) for Match {matchNumber} in {bracket.classification} Bracket!\n
                                                    Waiting for other player to report to confirm the score..."""

                        elif player1.score == p1score and player2.score == p2score:
                            matchup.resultConfirmed = True
                            matchup.status = "Ended"

                            if p1score > p2score:
                                player1.isWinner = True
                                winner = player1.player

                                player2.isWinner = False
                                loser = player2.player     

                            else:
                                player2.isWinner = True
                                winner = player2.player

                                player1.isWinner = False
                                loser = player1.player

                            updateBrackets(bracket, matchups, matchNumber, winner, loser, context)

                            context['message'] = f"""Successfully reported score ({p1score} - {p2score}) for Match {matchNumber} in {bracket.classification} Bracket!\n
                                                    This score is now official."""

                        else:
                            context['message'] = f"""The score ({p1score} - {p2score}) for Match {matchNumber} in {bracket.classification} Bracket does not match with\n
                                                    previously reported score ({player1.score} - {player2.score}).
                                                    Please report the (accurate) score."""

                            player1.score = -1
                            player2.score = -1

                        
                        player1.save()
                        player2.save()
                        matchup.save()

                    else:
                        context['message'] = f"You are not allowed permission to report the score for Match {matchNumber} in {bracket.classification} Bracket!"
                    
                    return render(request, 'brackets.html', context)

    return render(request, 'brackets.html', context)