from django.contrib import admin
from .models import Seller, Product, Brand, Order, Customer

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_type', 'get_sellers', 'email', 'date_post', 'created_at', 'updated_at')

    def get_sellers(self, obj):
        return ", ".join([seller.name_of_seller for seller in obj.name_of_seller.all()])
    get_sellers.short_description = 'Sellers'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'get_products', 'get_brand_types', 'price', 'order_date', 'created_at', 'updated_at')

    def get_products(self, obj):
        return ", ".join([product.product_type for product in obj.product.all()])
    get_products.short_description = 'Products'

    def get_brand_types(self, obj):
        return ", ".join([brand.brand_type for brand in obj.brand.all()])
    get_brand_types.short_description = 'Brands'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'name_of_seller', 'email', 'date_post', 'created_at', 'updated_at')

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name_of_seller', 'sex', 'birthdate', 'description', 'image', 'created_at', 'updated_at')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'cellphone_number', 'created_at', 'updated_at')

admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
