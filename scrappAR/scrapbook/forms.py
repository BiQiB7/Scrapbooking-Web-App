from django import forms
from .models import Posts, Scrapbook

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder' : 'description ...'
            }))
    image = forms.ImageField(
    required=False,
    widget=forms.ClearableFileInput(attrs={
    'multiple': True
    })  
)
    # scrapbook = forms.ModelChoiceField(
    # label = "Item choices", queryset = Scrapbook.objects.all(), required= True)
    

    class Meta:
        model = Posts
        fields = ['body','scrapbook']
    
    #body = forms.CharField(max_length=2200)
    # drop down select from db

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=2200)