from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import CharField
from django.db.models import DateTimeField


class Home(models.Model):
    Foto = models.CharField (max_length=200)
    Nama = models.CharField (max_length=100)
    Harga = models.FloatField (max_length=100)

    def __str__ (self):
        return self.Nama    