from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car,CarModel
from .forms import SellForm
class HomeView(TemplateView):
    template_name = "index.html"


class AllCarsView(ListView):
    template_name = 'all-cars.html'
    model = User


class SellCarsView(LoginRequiredMixin,CreateView):
    template_name = 'sell-car.html'
    model = Car
    form_class = SellForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def load_models(request):
    brand_id = request.GET.get('brand')

    if brand_id:
        models = CarModel.objects.filter(brand=brand_id).order_by('name')
    else:
        models = CarModel.objects.none()
        
    return render(request, 'car_dropdown_list_options.html', {'models': models})