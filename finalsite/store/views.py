from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from store.models import Seller, Product, Brand,Order,Customer
from store.forms import SellerForm, ProductForm,BrandForm,OrderForm,CustomerForm

from django.urls import reverse_lazy
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
    paginate_by = 2

class SellerCreateView(CreateView):
    model = Seller
    form_class = SellerForm
    template_name = 'Seller_add.html'
    success_url = reverse_lazy('Seller-list')

class SellerUpdateView(UpdateView):
    model = Seller
    form_class = SellerForm
    template_name = 'Seller_edit.html'
    success_url = reverse_lazy('Seller-list')

class SellerDeleteView(DeleteView):
    model = Seller
    template_name = 'Seller_del.html'
    success_url = reverse_lazy('Seller-list')  
    
    
    
class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'
    paginate_by = 2
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('product-list')  
    
    
    
class BrandList(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brand.html'
    paginate_by = 2
    
class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_add.html'
    success_url = reverse_lazy('brand-list')

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_edit.html'
    success_url = reverse_lazy('brand-list')

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_del.html'
    success_url = reverse_lazy('brand-list')  
       
       

class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order.html'
    paginate_by = 2
    
class OrderCreateView(CreateView):
    model = Seller
    form_class = SellerForm
    template_name = 'order_add.html'
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Seller
    form_class = SellerForm
    template_name = 'order_edit.html'
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Seller
    template_name = 'order_del.html'
    success_url = reverse_lazy('order-list')  
       
       

class CustomerList(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer.html'
    paginate_by = 2
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_add.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_edit.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = CustomerForm
    template_name = 'customer_del.html'
    success_url = reverse_lazy('customer-list')  
       
    
