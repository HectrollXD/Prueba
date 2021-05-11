from django.shortcuts import render
from project import NAME_OF_PROJECT
from .forms import AddProductForm
from Departments.models import Department
from Providers.models import Provider

def showproducts_view( request ):
    return render( request, 'showproducts.html',{
        'titleOfPage': 'Show products',
        'nameOfApplication': NAME_OF_PROJECT
    } )

def addproducts_view( request ):
    form = AddProductForm(request.POST or None)
   

    if request.method == 'POST' and form.is_valid():
        form.save()
        

    return render( request, 'addproduct.html',{
        'titleOfPage': 'Add products',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
    } )
