from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.

def validate_contact_number(value):
    """
    Validate that the mobile number has the format #### ### ###
    """
    if len(value.replace(' ', '')) != 11 or not value.replace(' ', '').isdigit():
        raise ValidationError('Mobile number must be in the format #### ### ####')

class Account(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    isOrganizer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username}, {self.email}"
    
    def get_username(self):
        return self.email

    def has_module_perms(self, register):
        return self.is_staff
    
    def get_absolute_url(self):
        return reverse('player_profile:player-detail', kwargs={'pk':self.pk})

class OrganizerAccount(Account):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=32)
    contact_number = models.CharField(max_length=15, validators=[validate_contact_number])
    past_experience = models.TextField(blank = True, null = True)
    additional_comments = models.TextField(blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.username}, {self.email}"
    
    def save(self, *args, **kwargs):
        self.isOrganizer = True
        super().save(*args, **kwargs)