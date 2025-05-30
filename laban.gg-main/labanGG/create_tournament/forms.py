from django import forms
from .models import Tournament, Game  # Import Game model

class TournamentForm(forms.ModelForm):
    game = forms.ModelChoiceField(queryset=Game.objects.all())  # Add game field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['application_link'].required = False  # Make application link optional

    class Meta:
        model = Tournament
        fields = ['name', 'game', 'tier', 'location', 'format', 'application_link', 'schedule', 'prize_pool', 'more_details', 'image']
