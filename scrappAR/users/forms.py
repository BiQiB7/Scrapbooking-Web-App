from django import forms
from django.contrib.auth.models import User
from django.db import models

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationFrom(forms.ModelForm):
    id = models.AutoField(primary_key=True, null= False)
    firstname = forms.CharField(label = 'First name')
    lastname = forms.CharField(label = 'Last name')
    email = forms.EmailField(label = 'Email address', max_length= 200)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    dob = forms.DateField(label = 'birthdaytime')
    
    class Meta:
        model = User
        fields = {'id','firstname','lastname','email','dob'}
    # def check_password(self):
    #    if self.cleaned_data['password'] != self.cleaned_data['password2']:
    #        raise forms.ValidationError('Passwords do not match')
    #    return self.cleaned_data['password2']