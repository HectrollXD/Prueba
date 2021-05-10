from django.shortcuts import render
from project import NAME_OF_PROJECT

def providers_view( request ):
    return render( request, 'providers.html',{
        'titleOfPage': 'Providers',
        'nameOfApplication': NAME_OF_PROJECT
    } )