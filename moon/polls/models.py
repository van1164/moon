from django.conf import settings
from django.db import models
from django.utils import timezone


class dataxx(models.Model):
    name = models.CharField(max_length =200)
    unit = models.CharField(max_length =200)
    rank = models.CharField(max_length =200)
    number = models.IntegerField(default = 0)
    def __str__(self):
        return self.unit + " " + self.rank + " " + self.name
# Create your models here.
