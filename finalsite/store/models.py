# models.py

from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Seller(BaseModel):
    Sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )

    name_of_seller = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=17, null=True, blank=True, choices=Sex)
    birthdate = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name_of_seller

class Product(BaseModel):
    product_type = models.CharField(max_length=30, null=True, blank=True)
    name_of_seller = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_post = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.product_type

class Brand(BaseModel):
    brand_type = models.CharField(max_length=30, null=True, blank=True)
    name_of_seller = models.ManyToManyField(Seller, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_post = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        seller_names = [seller.name_of_seller for seller in self.name_of_seller.all()]
        return f"{self.brand_type} ({', '.join(seller_names)})"



class Order(BaseModel):
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    brand = models.ManyToManyField(Brand, blank=True)
    price = models.DecimalField(max_digits=9999, decimal_places=2, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)

    def brand_types(self):
        brand_types = [brand.brand_type for brand in self.brand.all()]
        product_names = [product.name_of_seller for product in self.product.all()]
        return ", ".join(brand_types + product_names)

class Customer(BaseModel):
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cellphone_number = models.CharField(max_length=11,null=True, blank=True)
