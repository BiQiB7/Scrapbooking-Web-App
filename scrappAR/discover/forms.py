from django import forms
from scrapbook.models import Scrapbook, Topic

class CreateScrapbookForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': '1',
            'placeholder' : 'enter scrapbook name'
            }))
    topic = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': '2',
            'placeholder' : 'enter scrapbook topic'
            }))
    
    class Meta:
        model = Scrapbook
        fields = ['name']