from django import forms
from .models import Image
from scrapbook.models import Scrapbook, Topic


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image",)




