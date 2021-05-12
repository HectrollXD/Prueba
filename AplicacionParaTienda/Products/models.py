from django.db import models
from Departments.models import Department
from Providers.models import Provider

class Product( models.Model ):
    productname = models.CharField(max_length = 150, blank = False, null = False)
    productdescription = models.CharField(max_length = 500, blank = True, null = True)
    productid = models.CharField(max_length = 50, blank = False, null = False)
    productprice = models.DecimalField(max_digits = 12, decimal_places = 2, blank = False, null = False, default = 0.0)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False, null = False)
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE, blank = False, null = False)