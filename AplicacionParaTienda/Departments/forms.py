from django.forms import ModelForm
from .models import Department

class AddDepartmentForm( ModelForm ):
    class Meta:
        model = Department
        fields = [
            'Department_Name'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Department_Name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add new department'
        })