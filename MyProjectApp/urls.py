from django.urls import path
from MyProjectApp import views

urlpatterns = [
    path('', views.home, name='home'),
]
