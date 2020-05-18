from django import forms
from django.conf import settings

from .models import Tweet



class TweetForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content)>settings.MAX_LENGTH:
            raise forms.ValidationError("This tweet is to long.")
        return content