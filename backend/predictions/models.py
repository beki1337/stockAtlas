from django.db import models

# Create your models here.
class Predictions(models.Model):
    ticket = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    price = models.IntegerField()
    diraction = models.CharField(max_length=20)
    activ = models.BooleanField(default=True)
