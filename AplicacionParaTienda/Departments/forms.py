from django.forms import ModelForm
from .models import Department

class AddDepartmentForm( ModelForm ):
    class Meta:
        model = Department
        fields = [
            'department_name'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add new department'
        })