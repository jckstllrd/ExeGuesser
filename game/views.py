from django.shortcuts import render, redirect
from .models import activeGame
from .forms import GameCreatorForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'game/home.html', context)

def createGame(request):
    if request.method == "POST":
        
        form = GameCreatorForm(request.POST)
        
        if form.is_valid():
            game_session = form.save(commit=False)
            game_session.save()
            return redirect('joinGame')
    else:
        form = GameCreatorForm()
        
    return render(request, 'game/createGame.html', {'form':form})

def joinGame(request):
    active_games_list = activeGame.objects.order_by('gameName')
    context = {'active_games_list': active_games_list}
    return render(request, 'game/joinGame.html', context)

def game(request, game_id):
    context = {}
    return render(request, 'game/gamePage.html', context)