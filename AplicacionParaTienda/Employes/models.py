from django.db import models
from django.contrib.auth.models import User





class Employe( models.Model ):
    firstname = models.CharField(
        max_length = 25,
        blank = False,
        null = False
    )
    secondname = models.CharField(
        max_length = 25,
        null = True,
        blank = True,
    )
    lastname = models.CharField(
        max_length = 25,
        blank = False,
        null = False
    )
    secondlastname = models.CharField(
        max_length = 25,
        blank = False,
        null = False
    )
    idemploye = models.CharField(
        max_length = 20,
        blank = False,
        null = False
    )
    usr = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )

    def __str__( self ):
        return self.idemploye