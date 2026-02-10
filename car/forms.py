from django import forms
from .models import Car

class SellForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ['owner']
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 transition duration-200'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'
        self.fields['image'].widget.attrs['class'] = 'w-full px-4 py-2 border border-gray-300 rounded-lg bg-white'
        self.fields['description'].widget.attrs['rows'] = 4