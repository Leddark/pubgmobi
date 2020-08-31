from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('verification', views.verific, name='verific'),
    path('completed', views.complet, name='completed'),
]
