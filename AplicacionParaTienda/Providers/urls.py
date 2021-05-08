from django.urls import path
from . import views

app_name = 'Providers'

urlpatterns = [
    path('show-all-providers/', views.showproviders_view, name = 'showproviderspage'),
    path('add-new-provider/', views.addprovider_view, name = 'addproviderspage'),
]
