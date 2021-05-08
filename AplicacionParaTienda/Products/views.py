from django.shortcuts import render
from project import NAME_OF_PROJECT

def showproducts_view( request ):
    return render( request, 'showproducts.html',{
        'titleOfPage': 'Show products',
        'nameOfApplication': NAME_OF_PROJECT
    } )

def addproducts_view( request ):
    return render( request, 'addproduct.html',{
        'titleOfPage': 'Add products',
        'nameOfApplication': NAME_OF_PROJECT
    } )

