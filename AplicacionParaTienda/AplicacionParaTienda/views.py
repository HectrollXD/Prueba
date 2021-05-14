from django.shortcuts import render
from project import NAME_OF_PROJECT
from django.contrib.auth.decorators import login_required





@login_required( login_url = 'loginpage' )
def home_view(request):
    return render( request, 'home-admin.html', {
        'titleOfPage': 'Home',
        'nameOfApplication': NAME_OF_PROJECT
    } )