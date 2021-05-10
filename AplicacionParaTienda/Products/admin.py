from django.contrib import admin
from Products.models import Product

class ProductAdmin( admin.ModelAdmin ):
    list_display = (
        'Product_ID',
        'Product_Name',
        'Product_Price',
    )

admin.site.register(Product, ProductAdmin)