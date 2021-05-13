from django.shortcuts import render
from project import NAME_OF_PROJECT
from .forms import AddNewUserForm





def LoginPageView( request ):
    
    return render(request, 'login.html', {
        'titleOfPage': 'Login',
        'nameOfApplication': NAME_OF_PROJECT
    })






def AddUserPageView( request ):
    form = AddNewUserForm()
    return render(request, 'createuser.html', {
        'titleOfPage': 'Create user',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    })

