from django.urls import path
from .views import TournamentsListView
urlpatterns = [
    path('', TournamentsListView.as_view(), name='index'),
]

app_name = "tournaments_list"
