from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number']

    def save(self, commit = True):
        user =  super().save(commit=False)
        user.username = user.email 
        if commit:
            user.save()
        return user
        