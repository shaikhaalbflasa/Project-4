from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import folium
from .models import Data
from folium import plugins

import requests



r = requests.get('http://windatlas.xyz/api/wind/?lat=-15.968&lon=-68.665&height=100&date_from=2010-01-01&date_to=2011-12-31')

# r['']







# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

def signup (request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up , try again'
    
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
    
@login_required
def solarenergy_index(request):
  data = Data.objects.all()
  data_list =  Data.objects.values_list('latitude','longitude', 'windSpeed')

  map1 = folium.Map(location=[26, 50], zoom_start=7)
  
  plugins.HeatMap(data_list).add_to(map1)
  plugins.Fullscreen(position='topright').add_to(map1)
  
  map1 = map1._repr_html_()
  context = {
    'map1':map1
  }
  return render(request, 'solarenergy/index.html', context)

