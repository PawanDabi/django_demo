from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('template/', views.template, name='templates'),
]   