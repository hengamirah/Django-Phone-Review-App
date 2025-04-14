# filepath: c:\Users\Amirah\OneDrive\005 UM\07_SOFTWAREDESIGN\DjangoProject\phoneradar\phoneradar\urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),  # List all reviews
    path('add/', views.add_review, name='phonereview_add'),  # Add a new review
]