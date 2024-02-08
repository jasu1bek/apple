from django.db import models

class Prihod (models.Model):
    provider_name = models.CharField(max_length=255)
    username = models.TextField()
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.provider_name
