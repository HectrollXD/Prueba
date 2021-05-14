from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from project import NAME_OF_PROJECT
from django.contrib import messages
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
                messages.success(request, 'Welcome: {}.'.format(user.username))
                return redirect('homepage')
            else:
                messages.success(request, 'Welcome: {}.'.format(user.username))
                return redirect('homepage') 
        else:
            messages.error(request, 'Incorrect user or password.')

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

        if User.objects.filter(username = user).exists():
            messages.error( request, 'Please, verify that the user entered does not belong to someone else.')
            return redirect('createuserpage')
        else:
            if form.cleaned_data.get('admin') == 'A':            
                if User.objects.create_user( user, email, passw, is_superuser = True,  is_staff = True):
                    messages.success( request, 'Created user admin successfully!')
                    return redirect('createuserpage')
                else:
                    messages.error( request, 'Sorry, an problem was ocurred.')
                    return redirect('createuserpage')
            else:
                if User.objects.create_user( user, email, passw):
                    messages.success( request, 'Created user employe successfully!')
                    return redirect('createuserpage')
                else:
                    messages.error( request, 'Sorry, an problem was ocurred.')
                    return redirect('createuserpage')

    return render(request, 'createuser.html', {
        'titleOfPage': 'Create user',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    })





def Logout( request ):
    logout(request)
    return redirect('loginpage')