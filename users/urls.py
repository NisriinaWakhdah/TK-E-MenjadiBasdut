from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_role_view, name='register_role'),
    path('register/customer/', views.register_customer_view, name='register_customer'),
    path('register/organizer/', views.register_organizer_view, name='register_organizer'),
    path('register/admin/', views.register_admin_view, name='register_admin'),
    path('dashboard/admin/', views.admin_dashboard, name='dashboard-admin'),
    path('dashboard/organizer/', views.organizer_dashboard, name='dashboard-organizer'),
    path('dashboard/customer/', views.customer_dashboard, name='dashboard-customer'),
]