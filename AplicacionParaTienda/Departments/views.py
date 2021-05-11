from django.shortcuts import render
from django.shortcuts import redirect
from project import NAME_OF_PROJECT
from django.contrib import messages
from .forms import AddDepartmentForm

def departments_view( request ):
    form = AddDepartmentForm( request.POST or None )

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'The department has added.')
        return redirect('Departments:showdeppartmentspage')

    return render( request, 'departments.html',{
        'titleOfPage': 'Departments',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form
    } )
