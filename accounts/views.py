from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

class UserLoginView(TemplateView):
    template_name = 'login.html'