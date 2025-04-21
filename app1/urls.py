from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
path('',views.home,name='home')  ,
path('dish/<slug:slug>',views.detail,name='details'),
path('explore/',views.explore,name='explore')  ,
path('contact/',views.form ,name='contact'),
path('about/',views.about,name='about'),
path('login/',views.login_page,name='login'),
path('logout/',views.logout_user, name='logout'),
path('search/', views.search_results, name='search'),
path('dashboard/',views.dashboard,name='dashboard'),
path('booking/',views.booking,name='booking'),

]