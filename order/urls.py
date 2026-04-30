from django.urls import path
from .import views

urlpatterns = [
    path('checkout/customer', views.checkout_view, name='checkout'),
    path('orders/customer', views.customer_orders_view, name='orders-customer'),
    path('orders/organizer', views.organizer_orders_view, name='orders-organizer'),
]