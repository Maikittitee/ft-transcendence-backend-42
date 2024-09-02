from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('user/', views.user, name='user'),
]