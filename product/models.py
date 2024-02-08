from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
