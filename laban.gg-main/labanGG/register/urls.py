from django.urls import path
from .views import register_view

urlpatterns = [
    path('', register_view, name='register_view'),
]
# This might be needed, depending on your Django version
app_name = "register"