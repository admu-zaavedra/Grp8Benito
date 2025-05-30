from django.contrib import admin
from .models import Bracket, Matchup, PlayerInMatchup


class BracketAdmin(admin.ModelAdmin):
	model = Bracket


class MatchupAdmin(admin.ModelAdmin):
	model = Matchup


class PlayerInMatchupAdmin(admin.ModelAdmin):
	model = PlayerInMatchup


admin.site.register(Bracket, BracketAdmin)
admin.site.register(Matchup, MatchupAdmin)
admin.site.register(PlayerInMatchup, PlayerInMatchupAdmin)