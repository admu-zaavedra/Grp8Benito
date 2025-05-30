from django.contrib import admin
from .models import TournamentPlayer

class JTAdmin(admin.ModelAdmin):
    model = TournamentPlayer

admin.site.register(TournamentPlayer, JTAdmin)
# Register your models here.
