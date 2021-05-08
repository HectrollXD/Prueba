from django.shortcuts import render
from project import NAME_OF_PROJECT

def showproviders_view( request ):
    return render( request, 'showproviders.html',{
        'titleOfPage': 'Show providers',
        'nameOfApplication': NAME_OF_PROJECT
    } )

def addprovider_view( request ):
    return render( request, 'addprovider.html',{
        'titleOfPage': 'Add providers',
        'nameOfApplication': NAME_OF_PROJECT
    } )
