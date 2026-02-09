from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CusotmUserAdmin(UserAdmin):
    list_display = ('email','first_name','phone_number')

admin.site.register(User,CusotmUserAdmin)
