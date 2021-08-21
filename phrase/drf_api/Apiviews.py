from phrase.models import Phrase, SleepKnowledge

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PhraseSerializer, KnowledgeSerializer

import random

##### API VIEW #####
@api_view(['GET'])
def randomPhrase(req):
    phrases = Phrase.objects.all()
    randomphrases = random.sample(list(phrases), 4)
    serializer = PhraseSerializer(randomphrases, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomKnowledge(req):
    knowledges = SleepKnowledge.objects.all()
    randomknowledges = random.sample(list(knowledges), 4)
    serializer = KnowledgeSerializer(randomknowledges, many=True)
    return Response(serializer.data)
