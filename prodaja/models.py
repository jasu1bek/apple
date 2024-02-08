from django.db import models

class Prodaja (models.Model):
    product_name =models.CharField(max_length=255, verbose_name='Product Name ')
    username = models.TextField(verbose_name='Username')
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return f'{self.product_name} - {self.username}'
