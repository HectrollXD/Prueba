from django.forms import ModelForm
from .models import Provider

class AddProviderForm( ModelForm ):
    class Meta:
        model = Provider
        fields = [
            'providername'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['providername'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add new provider',
            'onkeyup': 'this.value = this.value.toUpperCase();'
        })