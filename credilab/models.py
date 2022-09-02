from django.db import models

# Create your models here.


class Client(models.Model):
    class ListEvent(models.IntegerChoices):
        excessive_rain = 1
        frost = 2
        hail = 3
        drought = 4
        gale = 5
        lightning = 6

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=144)
    cpf = models.CharField(max_length=11)
    type_tillage = models.CharField(max_length=144)
    date = models.DateField()
    event = models.IntegerField(choices=ListEvent.choices)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
