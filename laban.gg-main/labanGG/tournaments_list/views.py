from django.shortcuts import render
from django.views import View
from .models import Tournament

class TournamentsListView(View):
    def get(self, request):
        tournaments = Tournament.objects.all()  # Retrieve all tournaments
        return render(request, 'tournaments_list/index.html', {'tournaments': tournaments})
