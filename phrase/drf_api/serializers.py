from rest_framework import serializers
from phrase.models import Phrase, SleepKnowledge

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['content']

class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepKnowledge
        fields = ['content']