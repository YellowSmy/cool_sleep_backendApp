from phrase.models import Phrase, SleepKnowledge

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PhraseSerializer, KnowledgeSerializer

##### API VIEW #####
@api_view(['GET'])
def randomPhrase(req):
    phrase = Phrase.objects.order_by('?').first()
    serializer = PhraseSerializer(phrase)
    return Response(serializer.data)

@api_view(['GET'])
def randomKnowledge(req):
    knowledge = SleepKnowledge.objects.order_by('?').first()
    serializer = KnowledgeSerializer(knowledge)
    return Response(serializer.data)
