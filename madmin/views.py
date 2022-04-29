from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Class base views
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django_filters.views import FilterView

# auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#filter
from .filters import ProductTableFilter
from .forms import AddProductToInventory, AdminRegisterForm
# models
from .models import AdminData, Product
from billing.models import Customer


def registerAdmin(request):
  if request.method == 'POST':
    form = AdminRegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.position = form.cleaned_data.get('position')
      user.fname = form.cleaned_data.get('fname')
      user.lname = form.cleaned_data.get('lname')
      messages.success(request, f'Account created for {user.username} ')
      return redirect('dashboard') 
  else:
    form = AdminRegisterForm()
  context = {'form' : form}
  return render(request, 'mallm/register.html',context)

def sample(request):
  return render(request,'mallm/common.html')

# def mylogin(request):
#   if request.method == 'POST':
  
#   return render(request, 'mallm/login.html',{'form' :form})

@login_required
def dashboard(request):
  context = {'customers' :  Customer.objects.all().order_by('-pk')[:5]}
  return render(request,'mallm/dashboard.html', context)


@login_required
def addToInventory(request):
  if request.method == 'POST':
    form = AddProductToInventory(request.POST)
    if form.is_valid():
      form.save()
      product_name = form.cleaned_data.get('name')
      messages.success(request, f'{ product_name } is added in inventory')
      return redirect('AddToInventory')
  else:
    form = AddProductToInventory()
  return render(request, 'mallm/AddToInventory.html',{'form' : form})

class AddToInventory(LoginRequiredMixin,CreateView):
  model = Product
  template_name = 'mallm/AddToInventory.html'
  fields = ['Product_name','Product_code', 'Product_type', 'Price', 'Description', 'Supplier_name', 'Imported_cost','Imported_quantity', 'Sold_quantity', 'Available_quantity', 'Imported_cost', 'Profit',  'Image']

class ProductUpdateView(LoginRequiredMixin,UpdateView):
  model = Product
  template_name = 'mallm/AddToInventory.html'
  fields = ['Product_name','Product_code', 'Product_type', 'Price', 'Description', 'Supplier_name', 'Imported_cost','Imported_quantity', 'Sold_quantity', 'Available_quantity', 'Imported_cost', 'Profit',  'Image']

@login_required
def productFilterView(request):
  products = Product.objects.all()
  myFilter = ProductTableFilter(request.GET, queryset=products)
  products = myFilter.qs
  context = {'myFilter' : myFilter,
              'products' : products}
  return render(request, 'mallm/ShowProduct.html',context)


class ProductDetailedView(LoginRequiredMixin, DetailView):
  model = Product
  template_name = 'mallm/ProductDetailedView.html'
 

# delete product
def delete_product(request,pk):
  product_id = pk
  Product.objects.filter(pk= pk).delete()
  return redirect('ShowInventory')


