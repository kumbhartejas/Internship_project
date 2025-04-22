from django.contrib import admin
from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
