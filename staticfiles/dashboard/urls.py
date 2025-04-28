from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sections/', views.sections_list, name='sections_list'),
    path('sections/add/', views.add_section, name='add_section'),
    path('sections/<int:section_id>/', views.section_items, name='section_items'),
    path('sections/<int:section_id>/add-item/', views.add_item, name='add_item'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('items/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('sections/<int:section_id>/edit/', views.edit_section, name='edit_section'),
    path('sections/<int:section_id>/delete/', views.delete_section, name='delete_section'),
    path('items/<slug:slug>/', views.item_detail, name='item_detail'),
    path('contact_form/', views.contact, name='contactform'),
    path('booking_form/', views.booking, name='bookingform'), 

    path('edit-booking/<int:id>/', views.edit_book, name='edit_bookings'),      
    path('booking/delete/<int:id>/', views.delete_book, name='delete_bookings'),

    path('edit-contact/<int:id>/', views.edit_contacts, name='edit_contacts'),
    path('delete/contact/<int:id>/', views.delete_contacts, name='delete_contacts'), 

]
