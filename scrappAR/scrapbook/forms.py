from django import forms

class PostForm(forms.Form):
    photo = forms.ImageField()
    body = forms.CharField(max_length=2200)
    # drop down select from db

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=2200)