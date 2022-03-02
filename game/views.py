from django.shortcuts import render
from .models import activeGame

# Create your views here.
def home(request):
    context = {}
    return render(request, 'game/home.html', context)

def createGame(request):
    context = {}
    return render(request, 'game/createGame.html', context)

def joinGame(request):
    active_games_list = activeGame.objects.order_by('gameName')
    context = {'active_games_list': active_games_list}
    return render(request, 'game/joinGame.html', context)