from django.shortcuts import redirect
from .forms import AddDepartmentForm
from django.shortcuts import render
from project import NAME_OF_PROJECT
from .models import Department

def departments_view( request ):
    form = AddDepartmentForm( request.POST or None )
    departments = Department.objects.all()

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Departments:showdeppartmentspage')

    return render( request, 'departments.html',{
        'titleOfPage': 'Departments',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
        'departments': departments,
    } )
