import django_filters
from .models import Product
class ProductTableFilter(django_filters.FilterSet):
  Product_type = django_filters.CharFilter(field_name='Product_type', lookup_expr='icontains', label='Product type :')
  Product_name = django_filters.CharFilter(field_name='Product_name', lookup_expr='icontains', label='Product name :')
  Supplier_name = django_filters.CharFilter(field_name='Supplier_name', lookup_expr='icontains', label='Supplier name :')
 