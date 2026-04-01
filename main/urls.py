from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.careRentals_services, name='services'),
    path('password/generate/', views.password_generator, name='generate_password'),
    
]