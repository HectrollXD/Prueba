from django.views.generic.list import ListView
from Departments.models import Department
from django.shortcuts import redirect
from Providers.models import Provider
from django.shortcuts import render
from project import NAME_OF_PROJECT
from django.forms.forms import Form
from .forms import AddProductForm
from .models import Product
import Products

class ShowproductsListView( ListView ): #show product view and return objects
    template_name = 'showproducts.html'
    queryset = Product.objects.all().order_by('productname')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context

class SearchProductsListView( ListView ): #search product and return objects 
    template_name = 'searched.html'

    def get_queryset( self ): #meke the consult
        return Product.objects.filter( productname__icontains = self.query() ).order_by('productname')

    def query( self ): #obtain arguments whit the get method
        return self.request.GET.get('key')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context


def addproducts_view( request ): #add new product
    form = AddProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Products:addproductspage')

    return render( request, 'addproduct.html',{
        'titleOfPage': 'Add products',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    } )
