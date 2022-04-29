from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

class AdminRegisterForm(UserCreationForm):
  email = forms.EmailField()
  fname = forms.CharField()
  lname = forms.CharField()
#  dp = forms.ImageField()
  position = forms.CharField()
  
  class Meta:
    model = User
    fields = ['username','password1', 'password2','email','fname','lname','position']

class AddProductToInventory(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('Product_name', 'Description', 'Imported_quantity', 'Sold_quantity', 'Imported_cost','Supplier_name', 'Price', 'Product_type', 'Image',)
