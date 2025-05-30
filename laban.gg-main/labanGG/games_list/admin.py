from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    model = Game

admin.site.register(Game, GameAdmin)

# Register your models here.
