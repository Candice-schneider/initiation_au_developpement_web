from django.urls import path

from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('index/', views.index),
    path('main/', views.main),
    path('liste/', views.liste),
]

