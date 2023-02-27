from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
    lastNews = News.objects.order_by('-created_at')[:3]
    return render(request, 'news/index.html', {"news": lastNews})

def view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    
    # Construction du breadcrumb
    breadcrumb = [
        ('Accueil', '/'),
        ('Actus', '/news/'),
        (news.name, ''),
    ]
    
    return render(request, 'news/view.html', {'news': news, 'breadcrumb': breadcrumb})