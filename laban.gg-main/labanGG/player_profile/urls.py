# <appname>/urls.py
from django.urls import path
from .views import index, ProfileView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', ProfileView.as_view(), name='player-detail')
]
# This might be needed, depending on your Django version
app_name = "player_profile"