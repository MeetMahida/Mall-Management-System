from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
#class base views
from .views import ProductDetailedView, AddToInventory, ProductUpdateView

urlpatterns = [
    path('register/',views.registerAdmin,name="Register admin"),
    path('sample/',views.sample,name="SamplePage"),
    path('login/',auth_views.LoginView.as_view(template_name='mallm/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='mallm/logout.html'),name="logout"),
    path('',views.dashboard,name="dashboard"),
    path('addItem/',views.addToInventory,name="AddToInventory"),
    path('ShowItemDetail/<int:pk>/delete/',views.delete_product,name="DeleteProduct"),

    path('addItem2/',AddToInventory.as_view(),name="AddToInventory"),
    path('ShowItem/',views.productFilterView,name="ShowInventory"),
    path('ShowItemDetail/<int:pk>/',ProductDetailedView.as_view(),name="ShowProductDetail"),
    path('ShowItemDetail/<int:pk>/update/',ProductUpdateView.as_view(),name="UpdateProductDetail"),
]
