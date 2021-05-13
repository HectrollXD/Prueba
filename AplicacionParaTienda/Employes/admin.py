from django.contrib import admin
from .models import Employe





class EmployeAdmnin( admin.ModelAdmin ):
    list_display = (
        'idemploye',
        'lastname',
        'secondlastname',
        'firstname',
    )

admin.site.register(Employe, EmployeAdmnin)