from django import forms
from .models import Post

class PostForm(forms.Form):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder' : 'description ...'
        }))
    class Meta:
        model = Post
        fields = ['body']
    #photo = forms.ImageField()
    #body = forms.CharField(max_length=2200)
    # drop down select from db

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=2200)