from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = "index.html"


class AllCarsView(ListView):
    template_name = 'all-cars.html'
    model = User