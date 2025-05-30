from django.contrib.auth import get_user_model
from register.models import Account

class EmailOrUsernameModelBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = Account.objects.get(username=username)
        except Account.DoesNotExist:
            try:
                user = Account.objects.get(email=username)
            except Account.DoesNotExist:
                return None
        if user and user.password == password:
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None