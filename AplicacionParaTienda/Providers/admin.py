from django.contrib import admin
from Providers.models import Provider

class ProvidersAdmin( admin.ModelAdmin ):
    list_display = ('provider_name',)

    

admin.site.register(Provider, ProvidersAdmin)