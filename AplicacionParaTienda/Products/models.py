from django.db import models
from Departments.models import Department
from Providers.models import Provider

class Product( models.Model ):
    product_name = models.CharField(max_length = 150, blank = False, null = False)
    product_description = models.CharField(max_length = 500, blank = True, null = True)
    product_id = models.CharField(max_length = 50, blank = False, null = False)
    product_price = models.DecimalField(max_digits = 12, decimal_places = 2, blank = False, null = False, default = 0.0)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank = False, null = False)
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE, blank = False, null = False)