from django.db import models

class Category(modes.Model):
    category_name = models.CharFiled(max_length=255, verbose_name='Category Name')

    def __str__(self):
        return self.category_name
