from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
   #USER SINGUP
  path('accounts/signup/', views.signup, name='signup'),
  path('solarenergy/', views.solarenergy_index, name='index'),
]