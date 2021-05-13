from django.views.generic import ListView
from django.shortcuts import redirect
from django.shortcuts import render
from project import NAME_OF_PROJECT
from .forms import AddProviderForm
from .models import Provider





class ShowProviderListView( ListView ):
    template_name = 'showproviders.html'
    queryset = Provider.objects.all().order_by('providername')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleOfPage'] = "Show providers"
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context






class SearchProviderListView( ListView ):
    template_name = 'searchedprov.html'
    
    def get_queryset( self ):
        return Provider.objects.filter(providername__icontains = self.query()).order_by('providername')

    def query( self ):
        return self.request.GET.get('prov')





def providers_view( request ): #Add new provider and view
    form = AddProviderForm( request.POST or None )
    providers = Provider.objects.all().order_by('providername')

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Providers:showproviderspage')

    return render( request, 'addproviders.html',{
        'titleOfPage': 'Add new provider',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
        'providers': providers,
    } )
