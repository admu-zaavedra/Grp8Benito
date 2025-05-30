from django.urls import path
from .views import tournament_details, brackets

urlpatterns = [
    path('', tournament_details, name='tournament_details'),
    path('brackets/', brackets, name='brackets'),
]

app_name = "tournament_details"