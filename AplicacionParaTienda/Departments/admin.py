from django.contrib import admin
from Departments.models import Department

class DepartmentAdmin( admin.ModelAdmin ):
    list_display = ('departmentname',)

admin.site.register(Department, DepartmentAdmin)