from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
    # On affiche les 5 derniers sondage inscrits en base de données
    lastsPolls = Question.objects.order_by('-created_at')[:5]
    # On charge la vue index.html
    tpl = loader.get_template('polls/index.html')
    # On envoi les derniers sondages dans la variable data
    data = {
        'lastPolls': lastsPolls,
    }
    
    # On retourne le tout dans le HttpResponse
    return HttpResponse(tpl.render(data, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Méthode alternative plus compact pour rendre la vue :
    data = {
        'question': question
    }
    return render(request, 'polls/detail.html', data)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # On s'occupe de récupérer les données POST et modifier le nombre de votes en base de données
    # On commence d'abord par récupérer le sondage via question_id
    question = get_object_or_404(Question, pk=question_id)
    #Puis on essai de récupérer le choix de la requete POST en vérifiant qu'il existe
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Si le choix n'existe pas alors on retourne un message d'erreur
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Tu n'a pas sélectionné de choix."
        })
    else:
        # Sinon le choix existe et on traite la requête avec un +1 aux votes
        selected_choice.votes += 1
        selected_choice.save()
        # On retourne le tout
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

