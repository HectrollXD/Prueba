from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from project import NAME_OF_PROJECT





@login_required( login_url = 'loginpage' )
def settigs_view( request ):
    return render( request, 'settings.html',{
        'titleOfPage': 'Settings',
        'nameOfApplication': NAME_OF_PROJECT
    } )
