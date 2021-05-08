from django.shortcuts import render
from project import NAME_OF_PROJECT

def showemployes_view( request ):
    return render( request, 'showemployes.html',{
        'titleOfPage': 'Show employes',
        'nameOfApplication': NAME_OF_PROJECT
    } )

def addemploye_view( request ):
    return render( request, 'addemploye.html',{
        'titleOfPage': 'Add employes',
        'nameOfApplication': NAME_OF_PROJECT
    } )
