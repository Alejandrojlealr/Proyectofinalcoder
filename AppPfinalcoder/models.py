from datetime import datetime
from django.db import models
#from django.utils.timezone import now

# Create your models here.
class Cakes(models.Model):
    date=models.DateTimeField(default=datetime.now())
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
      return f'Customer order {self.order}'
    
class Dessert(models.Model):
    date=models.DateTimeField(default=datetime.now())
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
       return f'Customer order {self.order}'
    
class Bakery(models.Model):
    date=models.DateTimeField(default=datetime.now())
    order=models.IntegerField(default=0)
    fullname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    product=models.CharField(max_length=30)
    units=models.IntegerField()
    
    def __str__(self):
       return f'Customer order {self.order}'
    
    
    
    