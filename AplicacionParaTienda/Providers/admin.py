from django.contrib import admin
from Providers.models import Provider

class ProvidersAdmin( admin.ModelAdmin ):
    list_display = ('providername',)

    

admin.site.register(Provider, ProvidersAdmin)