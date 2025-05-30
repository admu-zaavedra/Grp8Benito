from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images', null = True, blank = True, max_length=100)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('games_list:games-detail', kwargs={'pk':self.pk})

    def get_absolute_games_url(self):
        return reverse('games_list:index')

# Create your models here.
