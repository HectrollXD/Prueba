from django.shortcuts import render
from project import NAME_OF_PROJECT

def settigs_view( request ):
    return render( request, 'settings.html',{
        'titleOfPage': 'Settings',
        'nameOfApplication': NAME_OF_PROJECT
    } )
