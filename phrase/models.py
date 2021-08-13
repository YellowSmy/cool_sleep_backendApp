from django.db import models
from django.db.models.fields import CharField

# Create your models here.

#명언
class Phrase(models.Model):
    content = models.CharField(max_length=40)
    
    def __str__(self):
        return self.content
        
class SleepKnowledge(models.Model):
    content = models.CharField(max_length=40)

    def __str__(self):
        return self.content
