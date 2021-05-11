from django.forms import ModelForm
from .models import Provider

class AddProviderForm( ModelForm ):
    class Meta:
        model = Provider
        fields = [
            'Provider_Name'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Provider_Name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add new provider'
        })