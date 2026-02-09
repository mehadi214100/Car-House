from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
   
    def get_success_url(self):
        return reverse_lazy('home')


class HomeView(TemplateView):
    template_name = 'index.html'