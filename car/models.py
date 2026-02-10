from django.db import models
from django.conf import settings

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True) 
    car_model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title