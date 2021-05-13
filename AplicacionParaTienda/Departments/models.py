from django.db import models

class Department( models.Model ):
    departmentname = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.departmentname