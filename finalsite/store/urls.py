from django.urls import path
from . import views

urlpatterns = [
    path('', views.MAINView.as_view(), name='MAIN'),
    path('Seller', views.SellerList.as_view(), name='Seller'), 
    path('product', views.ProductList.as_view(), name='product'),
    path('brand', views.BrandList.as_view(), name='brand'),
    path('order', views.OrderList.as_view(), name='order'),
    path('customer', views.CustomerList.as_view(), name='customer'),

]