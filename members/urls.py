from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
]
