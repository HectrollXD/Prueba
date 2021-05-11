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
            'product_name',
            'product_description',
            'product_id',
            'product_price',
            'department',
            'provider',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
        })
        
        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['product_id'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['product_price'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['department'].widget.attrs.update({
            'class': 'form-control text-center',
        })

        self.fields['provider'].widget.attrs.update({
            'class': 'form-control text-center',
        })
