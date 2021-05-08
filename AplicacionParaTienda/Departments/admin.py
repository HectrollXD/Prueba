from django.contrib import admin
from Departments.models import Department

class DepartmentAdmin( admin.ModelAdmin ):
    list_display = ('Department_Name',)

admin.site.register(Department, DepartmentAdmin)