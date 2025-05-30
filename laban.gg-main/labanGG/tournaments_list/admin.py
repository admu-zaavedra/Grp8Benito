from django.contrib import admin
from .models import Tournament

class TournamentAdmin(admin.ModelAdmin):
    model = Tournament

admin.site.register(Tournament, TournamentAdmin)
# Register your models here.
