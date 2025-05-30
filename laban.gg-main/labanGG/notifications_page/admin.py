from django.contrib import admin
from .models import Notifications

class NotificationsAdmin(admin.ModelAdmin):
    model = Notifications

admin.site.register(Notifications, NotificationsAdmin)

