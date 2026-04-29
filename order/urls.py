from django.urls import path
from .import views

urlpatterns = [
    path('checkout/costumer', views.checkout_view, name='checkout'),
]