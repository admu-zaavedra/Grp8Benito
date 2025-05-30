from django.contrib import admin

from .models import Account, OrganizerAccount

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    model = Account

class OrganizerAccountAdmin(admin.ModelAdmin):
    model = OrganizerAccount

admin.site.register(Account, AccountAdmin)
admin.site.register(OrganizerAccount, OrganizerAccountAdmin)