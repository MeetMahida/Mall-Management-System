from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# forms
from .forms import GenerateBillForm

# models from inventory
from madmin.models import Product

# invoice
from .utils import render_to_pdf

# generic / view
from django.views.generic import View
def AddCustomer(request):
  if request.method == 'POST':
    form = GenerateBillForm(request.POST)
    if form.is_valid():
      customer = form.save()
      messages.success(request, f'{customer.fname} inserted in databse, Bill will be generated shortly...')
      return redirect('Adding Customer')
  else:
    form = GenerateBillForm()
  context = {
    'form' : form
  }
  return render(request, 'billing/AddCustomer.html', context)


# invoice
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': 'today', 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('billing/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')