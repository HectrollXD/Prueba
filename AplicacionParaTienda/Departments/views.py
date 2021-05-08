from django.shortcuts import render
from project import NAME_OF_PROJECT

def showdepartments_view( request ):
    return render( request, 'showdepartments.html',{
        'titleOfPage': 'Show departments',
        'nameOfApplication': NAME_OF_PROJECT
    } )

def adddepartment_view( request ):
    return render( request, 'adddepartment.html',{
        'titleOfPage': 'Add departments',
        'nameOfApplication': NAME_OF_PROJECT
    } )
