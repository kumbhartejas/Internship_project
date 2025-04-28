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
path('booking/',views.booking,name='booking'),
path('details/<str:model_name>/<slug:slug>',views.abt_detail,name='abt_detail'),
]