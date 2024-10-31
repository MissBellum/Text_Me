from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('textbot/', views.textbot, name='textbot'),
    path('signup', views.signup, name='signup'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
]
