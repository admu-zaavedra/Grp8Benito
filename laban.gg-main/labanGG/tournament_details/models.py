from django.db import models
from create_tournament.models import Tournament
from join_tournament.models import TournamentPlayer


class Bracket(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	classification = models.CharField(max_length=15)


class Matchup(models.Model):
	bracket = models.ForeignKey(Bracket, on_delete=models.CASCADE, related_name='matchups')
	matchNumber = models.IntegerField()
	status = models.CharField(max_length=10, default="Upcoming")
	resultConfirmed = models.BooleanField(default=False)


class PlayerInMatchup(models.Model):
	player = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE)
	matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
	playerNumber = models.IntegerField()
	isWinner = models.BooleanField(null=True)
	score = models.IntegerField(default = -1)

	def __str__(self):
		return f"{self.player.ign} in {self.matchup.matchNumber} of {self.matchup.bracket.classification} Bracket"