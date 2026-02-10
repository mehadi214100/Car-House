from django.urls import path
from .views import HomeView,AllCarsView,SellCarsView,load_models

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('allcars/',AllCarsView.as_view(),name="all_cars"),
    path('sellcar/',SellCarsView.as_view(),name="sellcar"),
    path('ajax/load-models/',load_models,name="ajax_load_models")
]
