from django.db import models

class Department( models.Model ):
    Department_Name = models.CharField(max_length = 100, blank = False)
