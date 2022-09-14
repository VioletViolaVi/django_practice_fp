from django.contrib import admin

# Register your models here.

from .models import Animal, AnimalType

admin.site.register(Animal)
admin.site.register(AnimalType)
