from django import forms

from .models import Tweet

MAX_TWEEET_LENTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content'] 

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEEET_LENTH:
            raise forms.ValidationError("this tweet is to long") 
        return content

