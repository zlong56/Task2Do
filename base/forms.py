from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )
    
    phoneno = forms.CharField(
        label='Phone number'
    )
    
    class Meta:
        model = User
        fields = [
            'name', 
            'dob',
            'email',
            'address',
            'phoneno',
            'password1',
            'password2'
            ]
        
        
class UserForm(ModelForm):
    dob = forms.DateField(
        label='Date of Birth'
    )
    
    phoneno = forms.CharField(
        label='Phone number'
    )  
    
    class Meta:
        model = User
        fields = [
            'name', 
            'dob',
            'email',
            'address',
            'phoneno',
            'avatar',
            ]
        