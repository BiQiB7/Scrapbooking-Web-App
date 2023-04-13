from django import forms
from .models import Posts, Scrapbook, Image


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '7',
            'placeholder': '\n     description ...',
            'style': 'padding-left: 15px; padding-top: 15px; min-width: 24.5em; display: block; box-sizing: border-box;border: 2px solid #fff; -webkit-border-radius:6px;-moz-border-radius:6px;box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.33);-moz-box-shadow: inset 0px 1px 1px rgba(0, 0, 0, 0.5);',


        }))
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True,
            'class' : 'custom-file-upload',
            'style': 'display: none;',
          
        }))

    class Meta:
        model = Posts
        fields = ['body']

class CoverImageForm(forms.ModelForm):
    """Form for the image model"""
    # coverimg = forms.ImageField(label='coverimg', required=False)
    class Meta:
        model = Scrapbook
        fields = ['cover']

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=2200)
