from django.db import models
from Departments.models import Department
from Providers.models import Provider

class Product( models.Model ):
    Product_Name = models.CharField(max_length = 150, blank = False, null = False)
    Product_Description = models.CharField(max_length = 500, blank = True, null = True)
    Product_ID = models.CharField(max_length = 50, blank = False, null = False)
    Product_Price = models.DecimalField(max_digits = 12, decimal_places = 2, blank = False, null = False, default = 0.0)
    Department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False, null = False)
    Provider = models.ForeignKey(Provider, on_delete = models.CASCADE, blank = False, null = False)