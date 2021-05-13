from django.forms import ModelForm
from .models import Department

class AddDepartmentForm( ModelForm ):
    class Meta:
        model = Department
        fields = [
            'departmentname'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departmentname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add new department',
            'onkeyup': 'this.value = this.value.toUpperCase();'
        })