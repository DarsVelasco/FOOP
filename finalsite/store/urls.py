from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.MAINView.as_view(), name='MAIN'),
    path('Seller', views.SellerList.as_view(), name='Seller'), 
    path('Seller/add', views.SellerCreateView.as_view(), name='Seller-add'),
    path('Seller/<pk>', views.SellerUpdateView.as_view(), name='Seller-edit'),
    path('Seller/<pk>/delete', views.SellerDeleteView.as_view(), name='Seller-del'),     
    
    path('product/', views.ProductList.as_view(), name='product'),     
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<pk>/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('product/<pk>/delete/', views.ProductDeleteView.as_view(), name='product-del'),

    
    path('brand', views.BrandList.as_view(), name='brand'),
    path('brand/add', views.BrandCreateView.as_view(), name='brand-add'),
    path('brand/<pk>', views.BrandUpdateView.as_view(), name='brand-edit'),
    path('brand/<pk>/delete', views.BrandDeleteView.as_view(), name='brand-del'),    
    
    path('order', views.OrderList.as_view(), name='order'),
    path('order/add', views.OrderCreateView.as_view(), name='order-add'),
    path('order/<pk>', views.OrderUpdateView.as_view(), name='order-edit'),
    path('order/<pk>/delete', views.OrderDeleteView.as_view(), name='order-del'),   
     
    path('customer', views.CustomerList.as_view(), name='customer'),
    path('customer/add', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customer/<pk>', views.CustomerUpdateView.as_view(), name='customer-edit'),
    path('customer/<pk>/delete', views.CustomerDeleteView.as_view(), name='customer-del'),    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)