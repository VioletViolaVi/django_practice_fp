from operator import mod
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.


class AnimalType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True)
