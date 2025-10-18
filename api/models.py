from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)