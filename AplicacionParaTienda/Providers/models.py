from django.db import models

class Provider( models.Model ):
    providername = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.providername