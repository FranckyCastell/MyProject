from django.urls import path
from Shop import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
]
