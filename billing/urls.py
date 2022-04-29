from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
    path("AddCustomer/", views.AddCustomer, name="Adding Customer"),
    path("invoice/",GeneratePdf.as_view(), name="invoice"),
  
]
