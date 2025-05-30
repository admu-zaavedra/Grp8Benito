from django.db import models
from register.models import Account

class Notifications(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # ForeignKey reference to account in register
    notifications1 = models.BooleanField(default=False) # Notification when a tournament joined is started. 
    notifications2 = models.BooleanField(default=False) # Notification when an application gets accepted
    notifications3 = models.BooleanField(default=False) # Notification when an application gets rejected