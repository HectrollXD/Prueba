from django.forms import ModelForm
from .models import Employe





class AddNewEmployeForm( ModelForm ):
    class Meta:
        model = Employe
        fields = [
            'firstname',
            'secondname',
            'lastname',
            'secondlastname',
            'idemploye',
            'usr',
        ]

    def __init__( self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        self.fields['secondname'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        self.fields['lastname'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        self.fields['secondlastname'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        self.fields['idemploye'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        self.fields['usr'].widget.attrs.update({
            'class': 'form-control',
        })
