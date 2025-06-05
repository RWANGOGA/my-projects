from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.code1home, name='code1home'),
    path('<str:slug>', views.code1post, name='cod1post'),
    
    
    
    
    
    
]