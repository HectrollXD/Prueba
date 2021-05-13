from django.urls import path
from . import views

app_name = 'Providers'

urlpatterns = [
    path('search-provider', views.SearchProviderListView.as_view(), name = 'searchprovider'),
    path('add-provider/', views.providers_view, name = 'addproviderpage'),
    path('show-providers/', views.ShowProviderListView.as_view(), name = 'showproviderspage'),
]
