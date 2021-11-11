from django.urls import path
from Shop import views

urlpatterns = [
    path('shop/category/<int:id>', views.category, name='category'),
]
