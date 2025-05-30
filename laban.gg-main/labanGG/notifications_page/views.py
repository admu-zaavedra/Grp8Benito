from django.shortcuts import render
from .models import Notifications
from create_tournament.models import Tournament
from join_tournament.models import TournamentPlayer

def get_base_template(request):
    base_template = 'base_organizer.html' if request.user.isOrganizer else 'base_attendee.html'
    return base_template

def notifications_page(request):
    # Retrieve or create the notification settings for the current user
    notifications_page, created = Notifications.objects.get_or_create(account=request.user)

    if request.method == 'POST':
        notifications_page.notifications1 = request.POST.get('notifications1') == 'on'
        notifications_page.notifications2 = request.POST.get('notifications2') == 'on'
        notifications_page.notifications3 = request.POST.get('notifications3') == 'on'
        notifications_page.save()

    message1 = None
    message2 = None
    message3 = None
    tournaments_accepted = []
    tournaments_rejected = []

    # Update message based on tournament status for notifications1
    if notifications_page.notifications1 == True:
        user = request.user
        user_tournaments = TournamentPlayer.objects.filter(account=user, application_status='Accepted')
        for tournament_player in user_tournaments:
            tournament = tournament_player.tournament
            if tournament.status == 'Ongoing':
                message1 = f"The tournament you joined, '{tournament.name}' is now ongoing."
                break

    # Update message based on application status for notifications2
    if notifications_page.notifications2 == True:
        user = request.user
        accepted_applications = TournamentPlayer.objects.filter(account=user, application_status='Accepted')
        tournaments_accepted = [app.tournament.name for app in accepted_applications]

        if tournaments_accepted:
            message2 = f"Congratulations! Your application for the following tournaments has been accepted: {', '.join(tournaments_accepted)}"

    # Update message based on application status for notifications3
    if notifications_page.notifications3 == True:
        user = request.user
        rejected_applications = TournamentPlayer.objects.filter(account=user, application_status='Rejected')
        tournaments_rejected = [app.tournament.name for app in rejected_applications]

        if tournaments_rejected:
            message3 = f"Your application for the following tournaments has been rejected: {', '.join(tournaments_rejected)}"

    base_template = get_base_template(request)

    context = {
        'notifications_page': notifications_page,
        'message1': message1,
        'message2': message2,
        'message3': message3,
        'base_template': base_template,
    }
    return render(request, 'notifications_page.html', context)
