from django.db import models

class Provider( models.Model ):
    provider_name = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.provider_name