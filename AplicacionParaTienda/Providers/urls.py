from django.urls import path
from . import views

app_name = 'Providers'

urlpatterns = [
    path('providers/', views.providers_view, name = 'showproviderspage'),
]
