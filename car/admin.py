from django.contrib import admin

from .models import Brand,CarModel,Car

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']

admin.site.register(Brand, BrandAdmin)
admin.site.register(CarModel)
admin.site.register(Car)
