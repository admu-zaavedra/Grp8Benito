from django.contrib import admin
from .models import Tournament

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'tier', 'location', 'format')
    list_filter = ('game', 'tier', 'format')
    search_fields = ('name', 'game', 'location')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return u'<img src="%s" style="max-width: 200px; max-height: 200px;" />' % obj.image.url
        else:
            return '(No image)'

    image_preview.allow_tags = True
