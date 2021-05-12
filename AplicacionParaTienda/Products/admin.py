from django.contrib import admin
from Products.models import Product

class ProductAdmin( admin.ModelAdmin ):
    list_display = (
        'productid',
        'productname',
        'productprice',
    )

admin.site.register(Product, ProductAdmin)