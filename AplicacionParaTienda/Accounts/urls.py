from . import views
from django.urls import path

app_name = 'Accounts'

urlpatterns = [
    path('settings', views.settigs_view, name = "settingspage")
]