from django.urls import path
from .views import GamesListView, GamesDetailView, GamesSearchView

urlpatterns = [
    path('', GamesListView.as_view(), name='index'),
    path('<int:pk>/', GamesDetailView.as_view(), name='games-detail'),
    path('search-games/', GamesSearchView.as_view(), name='games-search'),

]
# This might be needed, depending on your Django version
app_name = "games_list"
