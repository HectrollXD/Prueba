from django.forms import ModelForm
from Providers.models import Provider
from django.db import models
from django.db.models import fields
from django.forms.widgets import Widget
from .models import Product

class AddProductForm( ModelForm ):
    class Meta:
        model = Product
        fields = [
            'productname',
            'productdescription',
            'productid',
            'productprice',
            'department',
            'provider',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['productname'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })
        
        self.fields['productdescription'].widget.attrs.update({
            'class': 'form-control',
            'onkeyup': 'this.value = this.value.toUpperCase();',
        })

        self.fields['productid'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['productprice'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['department'].widget.attrs.update({
            'class': 'form-control text-center',
        })

        self.fields['provider'].widget.attrs.update({
            'class': 'form-control text-center',
        })
