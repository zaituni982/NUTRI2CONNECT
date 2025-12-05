from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='nutriconnect/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),



    # Farmer URLs
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('farmers/add/', views.farmer_create, name='farmer_create'),
    path('farmers/<int:id>/edit/', views.farmer_update, name='farmer_update'),
    path('farmers/<int:id>/delete/', views.farmer_delete, name='farmer_delete'),

    # Client URLs
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'),
    path('clients/<int:id>/edit/', views.client_update, name='client_update'),
    path('clients/<int:id>/delete/', views.client_delete, name='client_delete'),
    path('pay/', views.payment_stk_push, name='initiate_payment')
]

