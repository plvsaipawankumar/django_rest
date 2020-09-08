from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Fapp(models.Model):
    name=models.CharField(max_length=100);
    email=models.EmailField();
    fname=models.CharField(max_length=100);
    age=models.IntegerField();
    city=models.CharField(max_length=100);
    state=models.CharField(max_length=100);

    def __str__(self):
        return self.name;