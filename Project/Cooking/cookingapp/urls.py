from django.urls import path, include
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('index/', views.index),
    path('', views.main),
    path('liste/', views.liste),
]
