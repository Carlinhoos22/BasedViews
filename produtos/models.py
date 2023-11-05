from django.db import models

# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to="produtos/", blank=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True)