from django.urls import path
from . import views

urlpatterns = [
    path('artist/', views.artist_list, name='artist_list'),
    path('artist/create/', views.artist_create, name='artist_create'),
    path('artist/update/<str:artist_id>/', views.artist_update, name='artist_update'),
    path('artist/delete/<str:artist_id>/', views.artist_delete, name='artist_delete'),
    path('ticket-category/', views.ticket_category_list, name='ticket_category_list'),
    path('ticket-category/create/', views.ticket_category_create, name='ticket_category_create'),
    path('ticket-category/update/<str:category_id>/', views.ticket_category_update, name='ticket_category_update'),
    path('ticket-category/delete/<str:category_id>/', views.ticket_category_delete, name='ticket_category_delete'),
]
