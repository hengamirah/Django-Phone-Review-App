from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),  # Root URL now uses index view
    #path('homepage/', views.homepage, name='homepage'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_phone/', views.add_phone, name='add_phone'),
    path('explore_phones/', views.explore_phones, name='explore_phones'),
    path('reviews/', views.reviews_page, name='reviews'),  
    path('register/', views.register, name='register'), 
    path('logout/', views.logout_view, name='logout'),
]
