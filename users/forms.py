""" sign up form of users"""

# form API
from django import forms

# Profile and User Models
from django.contrib.auth.models import User
from users.models import Profile
# Post model in same level as users, not here

# register aka sign up
class RegisterForm (forms.Form):
    #define fields

    username = forms.CharField(
        min_length = 4,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder':'User Name','class':'form-control'})
    )
    # ! to add validations
    password = forms.CharField(
        min_length = 8,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder':'New Password','class':'form-control'})
    )

    first_name = forms.CharField(
        min_length = 2,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'})
    )

    family_name = forms.CharField(
        min_length = 2,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder':'Family Name','class':'form-control'})
    )

    email = forms.CharField(
        min_length = 8,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder':'Email','class':'form-control'})
    )

    # to add: birthdate, gender drop down

    def reject_username(self):
        username = self.cleaned_data['username']
        username_existed = User.objects.filter(username = username).exists()
        if username_existed:
            raise forms.ValidationError('Username is already in use.')
        return username

    # reject if password not match
    def reject_password(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def create_profile(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        # instantiate new profile
        profile = Profile(user=user)
        profile.save()