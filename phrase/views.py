from .models import Phrase, SleepKnowledge
from django.shortcuts import get_object_or_404, redirect, render
from .form import KnowledgeForm, PhraseForm

##### UI #####
#Main page
def phraselist(req):
    phrases = Phrase.objects.all()
    knowledges = SleepKnowledge.objects.all()
    return render(req, 'phraselist.html', {'phrases': phrases, 'knowledges': knowledges})

#show detail
def showPhrase(req, id):
    phrase = get_object_or_404(Phrase, pk=id)
    return render(req, 'phrase/detail.html', {'phrase': phrase})

def showKnowledge(req, id):
    knowledge = get_object_or_404(SleepKnowledge, pk=id)
    return render(req, 'knowledge/detail.html', {'knowledge': knowledge})


#### PHRASE ####
#Create
def newphrase(req):
    return render(req, 'phrase/new.html')

def createphrase(req):
    if req.method == 'POST':
        form = PhraseForm(req.POST)
        if form.is_valid():
            phrase = form.save(commit=False)
            phrase.save()
            return redirect('phraselist')
        else:
            return redirect('phraselist')
    
    else:
        form = PhraseForm()
        return render(req, 'phrase/new.html', {'form': form}) 
    
#Update
def editphrase(req):
    return render(req, 'phrase/edit.html')

def updatephrase(req, id):
    phrase = get_object_or_404(Phrase, pk=id)
    if req.method == 'POST':
        form = PhraseForm(req.POST, instance=phrase)
        if form.is_valid():
            phrase = form.save(commit=False)
            phrase.save()
            return redirect('phraselist')
        else:
            return redirect('phraselist')

    else:
        form = PhraseForm(instance=phrase)
        return render(req, 'phrase/edit.html', {'form': form})

#Delete
def deletephrase(req, id):
    phrase = get_object_or_404(Phrase, pk=id)
    phrase.delete()
    return redirect('phraselist')


#### SLEEPKNOWLEDGE ####
#Create
def newknowledge(req):
    return render(req, 'knowledge/new.html')

def createknowledge(req):
    if req.method == 'POST':
        form = KnowledgeForm(req.POST)
        if form.is_valid():
            knowledge = form.save(commit=False)
            knowledge.save()
            return redirect('phraselist')
        else:
            return redirect('phraselist')

    else:
        form = KnowledgeForm()
        return render(req, 'knowledge/new.html', {'form': form})

#Update
def editknowledge(req):
    return render(req, 'knowledge/edit.html')

def updateknowledge(req, id):
    knowledge = get_object_or_404(SleepKnowledge, pk=id)
    if req.method == 'POST':
        form = KnowledgeForm(req.POST, instance=knowledge)
        if form.is_valid():
            knowledge = form.save(commit=False)
            knowledge.save()
            return redirect('phraselist')
        else:
            return redirect('phraselist')
    else:
        form = KnowledgeForm(instance=knowledge)
        return render(req, 'knowledge/edit.html', {'form': form})
    
#Delete
def deleteknowledge(req, id):
    knowledge = get_object_or_404(SleepKnowledge, pk=id)
    knowledge.delete()
    return redirect('phraselist')

