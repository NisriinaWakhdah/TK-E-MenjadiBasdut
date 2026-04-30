from django.urls import path
from .import views

urlpatterns = [
    path('promotion-list/', views.promotion_management, name='promotion-all'),
    path('admin-promotion-list/', views.admin_promotion_management, name='admin-promotion-list'),
]