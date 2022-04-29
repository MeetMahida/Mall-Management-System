from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

from django.urls import reverse
# Create your models here.

class AdminData(models.Model):
  fname = models.CharField(max_length=25)
  lname = models.CharField(max_length=25)
  position = models.CharField(max_length=20)
  user =  models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
      return self.fname
  



# class Supply(models.Model):
#   name = models.CharField(max_length=50)
#   description = models.CharField(max_length=300)
#   supplierName = models.CharField(max_length=30)
#   supplied_date = models.DateField(auto_now=True)
#   imported_qty = models.IntegerField()
#   imported_cost = models.IntegerField()
#   total_cost = models.DecimalField(max_digits=10, decimal_places=2)
#   img = models.ImageField(default='default.jpg', upload_to='product_pics')
#   def __str__(self):
#       return self.name
  
class Product(models.Model):
  Product_name = models.CharField(max_length=50)
  Supplier_name = models.CharField(max_length=100)
  Description = models.TextField()
  Imported_quantity = models.IntegerField()
  Imported_cost = models.BigIntegerField()
  # Imported_date = models.DateField( auto_now=False,  default=timezone.now())
  Sold_quantity = models.IntegerField()
  Profit = models.IntegerField(default=0)
  Available_quantity = models.IntegerField()
  Price = models.IntegerField()
  Product_type = models.CharField(max_length=30)
  Image = models.ImageField(default='default.png', upload_to='product_pics')
  Product_code = models.CharField(max_length=6, default='DEF000')
  def __str__(self):
      return self.Product_name

  def get_absolute_url(self):
      return reverse("ShowProductDetail", kwargs={"pk": self.pk})
  
  
