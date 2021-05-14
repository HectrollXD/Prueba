from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect
from .forms import AddNewEmployeForm
from django.shortcuts import render
from project import NAME_OF_PROJECT
from django.db.models import Q
from .models import Employe






class ShowAllEmployesListView( LoginRequiredMixin, ListView ):
    login_url = 'loginpage'
    template_name = 'showemployes.html'
    queryset = Employe.objects.all()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titleOfPage'] = 'Show employes'
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context





class SearchEmployesListView( LoginRequiredMixin, ListView ):
    login_url = 'loginpage'
    template_name = "searchedemploye.html"

    def get_queryset( self ):
        filters = Q(idemploye__icontains = self.query()) | Q(lastname__icontains = self.query())
        return Employe.objects.filter(filters).order_by('lastname')

    def query( self ):
        return self.request.GET.get('emp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleOfPage'] = 'Show employes'
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context




@login_required( login_url = 'loginpage' )
def addemploye_view( request ):
    form = AddNewEmployeForm( request.POST or None )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('Employes:showemployespage')

    return render( request, 'addemploye.html',{
        'titleOfPage': 'Add employes',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    } )
