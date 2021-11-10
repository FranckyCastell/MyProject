from django.urls import path
from Register import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(
        template_name='Register/login.html'), name='login'),
    path('logout', LogoutView.as_view(
        template_name='Register/logout.html'), name='logout'),
]
