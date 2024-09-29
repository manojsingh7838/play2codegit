from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, OTP

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, OTP


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }), label='')  # No label for email

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username',
    }), label='')  # No label for username

    password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }),
            label='',
            
        )

    password2 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password',
            }),
            label='',
            help_text=""
        )
    
    phoneno= forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone no',
    }), label='') 

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2",'phoneno']


class OTPVerificationForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ["otp"]


from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "textbox-input"}
        ),
        max_length=254,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "textbox-input"}
        ),
        max_length=128,
    )
