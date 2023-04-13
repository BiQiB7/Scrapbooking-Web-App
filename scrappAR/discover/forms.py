from django import forms
from scrapbook.models import Scrapbook, Topic


class createScrapbookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '2',
        'placeholder': 'Name your scrapbook',
        'style': 'padding-left: 15px; padding-top: 15px; min-width: 24.5em; display: block; box-sizing: border-box;border: 2px solid #fff; -webkit-border-radius:6px;-moz-border-radius:6px;box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.33);-moz-box-shadow: inset 0px 1px 1px rgba(0, 0, 0, 0.5);'
    }))
    topic = forms.ChoiceField(
        required=False,
        choices=[],
        widget=forms.Select(attrs={
            'style': 'padding: 5px; border: 1px solid #ccc;margin-bottom:30px;',
        })
    )
    new_topic = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
        'rows':'2',
        'placeholder': 'Or create a new topic',
        'style': 'padding-left: 15px; padding-top: 15px; min-width: 24.5em; display: block; box-sizing: border-box;border: 2px solid #fff; -webkit-border-radius:6px;-moz-border-radius:6px;box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.33);-moz-box-shadow: inset 0px 1px 1px rgba(0, 0, 0, 0.5);margin-bottom:30px;'
    }))

    class Meta:
        model = Scrapbook
        fields = ['title', 'topic', 'new_topic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].choices = self.get_topic_choices()

    def get_topic_choices(self):
        topics = Topic.objects.values_list('id', 'name')
        choices = list(topics)
        choices.insert(0, ('', 'Select a topic'))
        return choices

    def clean(self):
        cleaned_data = super().clean()
        topic = cleaned_data.get('topic')
        new_topic = cleaned_data.get('new_topic')
        if topic and new_topic:
            raise forms.ValidationError(
                'You cannot select an existing topic and enter a new one')
        elif not topic:
            if new_topic:
                topic = Topic.objects.create(name=new_topic)
                cleaned_data['topic'] = topic
            else:
                cleaned_data['topic'] = None
        elif topic == '':
            cleaned_data['topic'] = None

        else:
            cleaned_data['topic'] = Topic.objects.get(id=topic)
        return cleaned_data
