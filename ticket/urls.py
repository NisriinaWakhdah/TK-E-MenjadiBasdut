from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_tickets, name='manage_tickets'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('update/<str:ticket_id>/', views.ticket_update, name='ticket_update'),
    path('delete/<str:ticket_id>/', views.ticket_delete, name='ticket_delete'),
]