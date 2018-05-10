from django.shortcuts import render
from worldcup.models import Games
from worldcup.forms import AddGameForm
from django.http import HttpResponse

def index(request):
    games = Games.objects.all()
    context = {'games': games}
    return render(request, 'index.html', context)

def home(request):
    games = Games.objects.all()
    context = {'games': games}
    return render(request, 'base.html', context)