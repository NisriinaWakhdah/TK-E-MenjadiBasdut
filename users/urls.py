from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_role_view, name='register_role'),
    path('register/customer/', views.register_customer_view, name='register_customer'),
    path('register/organizer/', views.register_organizer_view, name='register_organizer'),
    path('register/admin/', views.register_admin_view, name='register_admin'),
]