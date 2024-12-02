from .models import SafetySuggestion 
from django import forms

class SafetySuggestionForm(forms.ModelForm):
    class Meta:
        model = SafetySuggestion
        fields = ('name', 'tip',)