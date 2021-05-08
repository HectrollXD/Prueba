from django.contrib import admin
from Providers.models import Provider

class RegisterAdmin( admin.ModelAdmin ):
    list_display = ('Provider_Name',)

admin.site.register(Provider, RegisterAdmin)