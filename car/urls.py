from django.urls import path
from .views import HomeView,AllCarsView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('allcars/',AllCarsView.as_view(),name="all_cars"),
]
