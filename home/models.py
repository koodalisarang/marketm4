from django.db import models

# Create your models here.
class register(models.Model):
    username= models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    phone=models.IntegerField(max_length=10)
    address=models.CharField(max_length=100)

class stokein(models.Model):
    itemid=models.IntegerField(max_length=10)
    img = models.FileField(null=True)
    itemname=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.CharField(max_length=50)
    type= models.BooleanField(default=False)

class busket(models.Model):
    phone=models.IntegerField(max_length=10)
    itemid=models.IntegerField()
    itemname=models.CharField(max_length=50)
    price=models.IntegerField()
    total=models.IntegerField()
class order(models.Model):
    orderid=models.IntegerField()
    phone = models.IntegerField(max_length=10)
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=50)
    price = models.IntegerField()
    total = models.IntegerField()
    date=models.DateField()

class amount(models.Model):
    orderid=models.IntegerField()
    phone = models.IntegerField(max_length=10)
    date=models.DateField()
    price=models.IntegerField()
    status = models.BooleanField(default=False)