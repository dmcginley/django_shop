from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='shop-home'),
    path('', views.welcome, name='shop-welcome'),
]
