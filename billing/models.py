from django.db import models
from madmin.models import Product
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
  product = models.ManyToManyField(Product)
  fname = models.CharField(max_length=30)
  lname = models.CharField(max_length=30)
  quantity = models.IntegerField(default=1)
  date = models.DateTimeField( auto_now=False, auto_now_add=False, default=timezone.now)
  def __str__(self):
      return self.fname
