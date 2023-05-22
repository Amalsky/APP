from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User
from django import forms
from .models import User, AdminUser, App
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


class CustomAdminForm(UserCreationForm):
    class Meta:
        model = AdminUser
        fields = ("username",)
        field_classes = {"username": UsernameField}


class AppCreateForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["app_name", "app_category", "app_point", "app_icon"]
        widgets = {
            "app_name": forms.TextInput(attrs={"class": "name"}),
            "app_category": forms.Select(attrs={"class": "category"}),
            "app_point":forms.NumberInput(attrs={"class": "apppoint"}),
            "app_icon":forms.ClearableFileInput(attrs={"class": "icon"})
        }


