from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_seats, name='manage_seats'),
    path('create/', views.seat_create, name='seat_create'),
    path('update/<str:seat_id>/', views.seat_update, name='seat_update'),
    path('delete/<str:seat_id>/', views.seat_delete, name='seat_delete'),
]