from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True , null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Staff(models.Model):
    name = models.CharField(max_length=100 )
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo/' , default=None)



class ProductList(models.Model):
    name = models.CharField(max_length=200 )
    price = models.DecimalField(max_digits=5 ,decimal_places=2)
    discount = models.DecimalField(max_digits=3 , decimal_places=2)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='photo/', default=True)
    rate = models.DecimalField(max_digits=10 , decimal_places=2)