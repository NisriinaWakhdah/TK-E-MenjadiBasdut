from django.urls import path
from .import views

urlpatterns = [
    path('promotionList/', views.promotion_management, name='promotion-all'),
    path('adminPromotionList/', views.admin_promotion_management, name='admin-promotion-list'),
]