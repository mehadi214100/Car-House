from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Car,CarModel,Brand
from .forms import SellForm
class HomeView(TemplateView):
    template_name = "index.html"


class AllCarsView(ListView):
    template_name = 'all-cars.html'
    model = Car
    context_object_name = 'cars'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        brands = self.request.GET.getlist('brand')
        if brands:
            queryset = queryset.filter(brand__id__in = brands)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte = min_price)
        if max_price:
            queryset = queryset.filter(price__lte = max_price)

        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['brands'] = Brand.objects.all()
        context['selected_brands'] = self.request.GET.getlist('brand')
        
        return context
    



class SellCarsView(LoginRequiredMixin,CreateView):
    template_name = 'sell-car.html'
    model = Car
    form_class = SellForm
    success_url = reverse_lazy('all_cars')
    
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


class CarDetailsView(DetailView):
    template_name = "car-details.html"
    model = Car
    context_object_name = 'car'