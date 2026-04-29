from django.urls import path
from .import views

urlpatterns = [
    path('checkout/customer', views.checkout_view, name='checkout'),
    path('orders/customer', views.orders_view, name='orders'),
]