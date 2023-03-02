from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'username',
        'email',
        'name',
        'is_staff',
    ]
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
