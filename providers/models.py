from django.db import models

class Provider(models.Model):
    name = models.CharField("Name",max_length=255)
    adress = models.CharField("Adress",max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField("Email", max_length=255)

    def __str__(self):
        return self.name
