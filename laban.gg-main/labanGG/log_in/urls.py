from django.urls import path
from .views import log_in_view

urlpatterns = [
    path('', log_in_view, name='log_in_view'),
    ]
# This might be needed, depending on your Django version
app_name = "log_in"