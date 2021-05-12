from django.shortcuts import redirect
from django.shortcuts import render
from project import NAME_OF_PROJECT
from .forms import AddProviderForm
from .models import Provider

def providers_view( request ):
    form = AddProviderForm( request.POST or None )
    providers = Provider.objects.all()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Providers:showproviderspage')

    return render( request, 'providers.html',{
        'titleOfPage': 'Providers',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
        'providers': providers,
    } )
