from django.db import models
import uuid
# Create your models here.


class Client(models.Model):
    class ListEvent(models.IntegerChoices):
        CHUVA_EXCESSIVA = 1
        GEADA = 2
        GRANIZO = 3
        SECA = 4
        VENDAVAL = 5
        RAIO = 6
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
