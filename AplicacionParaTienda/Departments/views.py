from django.views.generic import ListView
from django.shortcuts import redirect
from .forms import AddDepartmentForm
from django.shortcuts import render
from project import NAME_OF_PROJECT
from .models import Department





class ShowDepartmentsListView( ListView ):
    template_name = 'showdepartments.html'
    queryset = Department.objects.all().order_by('departmentname')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleOfPage'] = "Show all departments"
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context




class SearchDepartmentListView( ListView ):
    template_name = 'searcheddep.html'

    def get_queryset(self):
        return Department.objects.filter(departmentname__icontains = self.query()).order_by('departmentname')
    
    def query( self ):
        return self.request.GET.get('dep')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleOfPage'] = 'Department searched'
        context['nameOfApplication'] = NAME_OF_PROJECT
        return context





def AddDepartmentsView( request ):
    form = AddDepartmentForm( request.POST or None )
    departments = Department.objects.all().order_by('departmentname')

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('Departments:showdeppartmentspage')

    return render( request, 'adddepartment.html',{
        'titleOfPage': 'Add new department',
        'nameOfApplication': NAME_OF_PROJECT,
        'camp': form,
        'departments': departments,
    } )
