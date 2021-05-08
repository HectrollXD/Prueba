from django.db import models

class Provider( models.Model ):
    Provider_Name = models.CharField(max_length = 100, blank = False)
