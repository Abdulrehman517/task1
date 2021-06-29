from django.db import models

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=500)
    handle =models.TextField()
    body = models.TextField()


class Variant(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prod_var")
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    quantity  = models.IntegerField()



