from django.db import models

# # Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2, max_length=9, null=True, blank=True)
    in_stock = models.BooleanField(default=False)
    width = models.PositiveSmallIntegerField()
    heigth = models.PositiveSmallIntegerField()
    foto = models.ImageField(upload_to='photos/%Y/%m/%d/',
                             null=True,
                             blank=True,
                             width_field='width',
                             height_field='heigth')
    
    def __str__(self) -> str:
        return super().__str__()
