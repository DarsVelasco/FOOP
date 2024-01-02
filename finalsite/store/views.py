from django.shortcuts import render
from django.views.generic.list import ListView
from store.models import Seller, Product, Brand,Order,Customer
# Create your views here.

class MAINView(ListView):
    model = Seller
    context_object_name = 'MAIN'
    template_name = 'MAIN.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SellerList(ListView):
    model = Seller
    context_object_name = 'Sellers'
    template_name = 'Seller.html'
    paginate_by = 7
    
class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'
    paginate_by = 7
    
class BrandList(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brand.html'
    paginate_by = 7

class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order.html'
    paginate_by = 7

class CustomerList(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer.html'
    paginate_by = 7
    
