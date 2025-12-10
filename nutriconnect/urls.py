from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Core & Auth URLs
    path('', views.home, name='home'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('register/', views.register, name='register'),
    path('clients/', views.client_list, name='client_list'),
    path('login/', auth_views.LoginView.as_view(
            template_name='nutriconnect/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Payments
    path('pay/', views.payment_stk_push, name='initiate_payment'),
    path('daraja/stk-callback/<int:order_id>/', views.mpesa_callback, name='mpesa_callback'),

    # Produce Purchase
    path('farmer/<int:id>/produce/', views.farmer_produce, name='farmer_produce'),
    path('buy/<int:id>/', views.buy_produce, name='buy_produce'),

    # Farmer CRUD
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('farmers/add/', views.farmer_create, name='farmer_create'),
    path('farmers/<int:id>/edit/', views.farmer_update, name='farmer_update'),
    path('farmers/<int:id>/delete/', views.farmer_delete, name='farmer_delete'),
    # Add this under Farmer URLs
    path('farmers/<int:farmer_id>/produce/add/', views.add_produce, name='add_produce'),
    path('produce/', views.produce_list, name='produce_list'),
    path('produce/add/', views.produce_create, name='produce_create'),
    # Add this inside your urlpatterns
    path('farmers/<int:farmer_id>/produce/add/', views.add_produce, name='add_produce'),


    # Client CRUD
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'),
    path('clients/<int:id>/edit/', views.client_update, name='client_update'),
    path('clients/<int:id>/delete/', views.client_delete, name='client_delete'),
]
