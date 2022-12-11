from django.db import models


class nuevoitem(models.Model):
    items=models.CharField(max_length=40)
    precio=models.DateField()
    cualidades=models.IntegerField()

class PERSONAJES(models.Model):
    campeon=models.CharField(max_length=40)
    buffonerfeo=models.DateField()
    modificaciones=models.IntegerField()