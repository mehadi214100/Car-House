import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from car.models import Brand, CarModel

class Command(BaseCommand):
    help = 'Load car brands and models from JSON file'

    def handle(self, *args, **kwargs):

        try:
            with open('car_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            for entry in data:
                brand_name = entry['name']
                models_list = entry['models']

                brand, created = Brand.objects.get_or_create(
                    name=brand_name,
                    defaults={'slug': slugify(brand_name)}
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Brand created: {brand_name}'))
                else:
                    self.stdout.write(f'Brand already exists: {brand_name}')

             
                for model_name in models_list:
                    obj, created = CarModel.objects.get_or_create(
                        name=model_name,
                        brand=brand
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'  - Model added: {model_name}'))
            
            self.stdout.write(self.style.SUCCESS('All Data Loaded Successfully!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File "car_data.json" not found in the base directory.'))