from django.shortcuts import render
from project import NAME_OF_PROJECT

def home_view(request):
    return render( request, 'home.html', {
        'titleOfPage': 'Home',
        'nameOfApplication': NAME_OF_PROJECT
    } )