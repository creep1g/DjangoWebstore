from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from cereal.urls import *
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('search_history', views.search_history_view, name='search_history'),
    path('order_history', views.order_history_view, name='order_history')
]
