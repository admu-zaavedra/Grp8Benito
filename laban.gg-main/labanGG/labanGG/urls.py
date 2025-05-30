"""labanGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('games/', include('games_list.urls', namespace="games_list")),
    path('tournaments/', include('tournaments_list.urls', namespace="tournaments_list")),
    path('admin/', admin.site.urls),
    path('', include("create_tournament.urls")),
    path('log_in/', include('log_in.urls', namespace="log_in")),
    path('register/', include('register.urls', namespace="register")),
    path('tournament<int:id>/player_applications_list/', include('player_applications_list.urls', namespace="player_applications_list")),
    path('my_tournaments_organizer/', include('my_tournaments_organizer.urls', namespace="my_tournaments_organizer")),
    path('', include('join_tournament.urls', namespace="join_tournament")),
    path('notifications_page/', include('notifications_page.urls', namespace="notifications_page")),
    path('profile/', include('player_profile.urls', namespace="player_profile")),
    path('tournament<int:id>/tournament_details/', include('tournament_details.urls', namespace="tournament_details")),
    path('my_tournaments_attendee/', include('my_tournaments_attendee.urls', namespace="my_tournaments_attendee")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
