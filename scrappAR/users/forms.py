from django import forms
from django.contrib.auth.models import User
from django.db import models

class loginForm(forms.Form):
    UserName = forms.CharField(max_length=100)
    Password = forms.PasswordInput()

class signupForm(forms.Form):
    txtUserName = forms.CharField(max_length=100)
    txtPassword = forms.PasswordInput()
    txtPassword2 = forms.PasswordInput()
    txtFirstName = forms.CharField(max_length=100)
    txtLastName = forms.CharField(max_length=100)
    txtEmail = forms.EmailField()
    dateofbirth = forms.DateField()
    gender = forms.CharField(max_length=30)
    
    # class Meta:
    #    model = User
    #    fields = {'id','txtFirstName','txtLastName','txtEmail','birthdaytime'}
    # def check_password(self):
    #    if self.cleaned_data['password'] != self.cleaned_data['password2']:
    #        raise forms.ValidationError('Passwords do not match')
    #    return self.cleaned_data['password2']