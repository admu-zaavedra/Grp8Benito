from django.db import models
from games_list.models import Game  # Import Game model

class Tournament(models.Model):
    tournament_organizer = models.CharField(max_length=32, default = 'No Organizer')
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE) # ForeignKey reference to model in games_list
    tier = models.CharField(max_length=1, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')])
    location = models.CharField(max_length=100)
    format = models.CharField(max_length=100, choices=[('single_elimination', 'Single Elimination'), ('double_elimination', 'Double Elimination')])
    application_link = models.URLField()
    schedule = models.TextField()
    prize_pool = models.TextField()
    more_details = models.TextField()
    image = models.ImageField(upload_to='tournament_images', blank=True, null=True)
    status = models.CharField(max_length=10, default = 'Upcoming')
