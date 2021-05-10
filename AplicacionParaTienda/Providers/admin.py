from django.contrib import admin
from Providers.models import Provider

class ProvidersAdmin( admin.ModelAdmin ):
    list_display = ('Provider_Name',)

admin.site.register(Provider, ProvidersAdmin)