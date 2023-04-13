from django import forms

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

class SignUpForm(forms.Form):
    txtUserName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    txtFirstName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    txtLastName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    txtEmail = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    txtPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    txtPassword2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    dateofbirth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    GENDER_CHOICES = [('M', 'Male'),    ('F', 'Female'),    ('O', 'Other')]
    slcgender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
class ChangePasswordForm(forms.Form):
    txtOldPassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    txtNewPassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    txtNewPassword2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_txtOldPassword(self):
        old_password = self.cleaned_data.get("txtOldPassword")
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Invalid old password")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        NewPassword = cleaned_data.get("txtNewPassword")
        NewPassword2 = cleaned_data.get("txtNewPassword2")

        if NewPassword != NewPassword2:
            raise forms.ValidationError("New passwords must match")

        return cleaned_data

    def save(self):
        new_password = self.cleaned_data.get("txtNewPassword")
        self.user.set_password(new_password)
        self.user.save()
