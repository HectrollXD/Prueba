from . import views
from django.urls import path
from django.urls import include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('', include('Accounts.urls')),
    path('', include('Employes.urls')),
    path('', include('Products.urls')),
    path('', include('Providers.urls')),
    path('', include('Departments.urls')),
    path('home-admin', views.home_view, name = 'homepage'),
]
