from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect, render
from project import NAME_OF_PROJECT
from .forms import AddNewUserForm
from .forms import LoginForm





def LoginPageView( request ):
    form = LoginForm( request.POST or None )

    if request.method == 'POST' and form.is_valid():
        user = form.cleaned_data.get('user')
        passw = form.cleaned_data.get('password')
        user = authenticate( username = user, password = passw )
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('homepage')
            else:
                print('No es admin')
            
        else:
            print("valio webos la autenticación")

    return render(request, 'login.html', {
        'titleOfPage': 'Login',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form
    })





def AddUserPageView( request ):
    form = AddNewUserForm( request.POST or None )
    
    if request.method == "POST" and form.is_valid():
        user = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        passw = form.cleaned_data.get('password')
        if form.cleaned_data.get('admin') == 'A':
            User.objects.create_user( user, email, passw, is_superuser = True,  is_staff = True)
        else:
            User.objects.create_user( user, email, passw)

    return render(request, 'createuser.html', {
        'titleOfPage': 'Create user',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    })


def Logout( request ):
    logout(request)
    return redirect('loginpage')