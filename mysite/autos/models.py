from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Make(models.Model):
    name = models.CharField(
            max_length=200,
            help_text = 'Ingrese como (e. g Dofge))',
            validators = [MinLengthValidator(2, "En el nombre debes ingresar mas de un caracter")]
            )
    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(
                            max_length = 200,
                            validators = [MinLengthValidator(2, "En el Nickname debes ingresar mas de un caracter")]
            )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length = 300)
    make = models.ForeignKey('Make', on_delete = models.CASCADE, null=False)


    def __srt__(self):
        return self.nickname