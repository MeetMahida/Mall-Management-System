from django import forms
from .models import Customer

class GenerateBillForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ('product', 'quantity', 'fname', 'lname', 'date')