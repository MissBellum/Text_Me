from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('textbot/', views.textbot, name='textbot'),
]
