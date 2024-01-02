from django.forms import ModelForm
from django import forms
from .models import Seller,Product,Brand,Order,Customer

class SellerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Seller
        fields = "__all__"
        
class ProductForm(ModelForm):
    date_post = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Product
        fields = "__all__"

class BrandForm(ModelForm):
    date_post = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Brand
        fields = "__all__"
        
class OrderForm(ModelForm):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Order
        fields = "__all__"

class CustomerForm(ModelForm):
    name = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Customer
        fields = "__all__"