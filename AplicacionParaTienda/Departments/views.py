from django.shortcuts import render
from project import NAME_OF_PROJECT

def departments_view( request ):
    return render( request, 'departments.html',{
        'titleOfPage': 'Departments',
        'nameOfApplication': NAME_OF_PROJECT
    } )
