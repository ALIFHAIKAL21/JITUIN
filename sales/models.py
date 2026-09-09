from django.db.models import CharField
from django.db import models

# Create your models here.
class HistoricalSales(models.Model):
    Lokasi = CharField(max_length=130)
    Produk = CharField(max_length=130)
    Tanggal = models.DateField()
    Nilai = models.IntegerField()
    Nilai_Adjustment = models.IntegerField(default=0)