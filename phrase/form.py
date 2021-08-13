from django import forms
from django.forms import fields
from .models import Phrase, SleepKnowledge

class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ['content']

class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = SleepKnowledge
        fields = ['content']
