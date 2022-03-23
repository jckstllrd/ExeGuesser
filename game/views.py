from django.shortcuts import render, redirect
from .models import activeGame
from .forms import GameCreatorForm
from .models import locations
from .forms import LocationForm
import random

#Home page view
def home(request):
    context = {}
    return render(request, 'game/home.html', context)


def createGame(request):
    #Checks if the create game form is valid and then redirects user to list of active games
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
    #Displays all of the current games and allows the user to click on them
    active_games_list = activeGame.objects.order_by('gameName')
    context = {'active_games_list': active_games_list}
    return render(request, 'game/joinGame.html', context)

def game(request, game_id):
    #Page for the game to take place
    context = {}
    
    return render(request, 'game/gamePage.html', context)

def locationUpload(request):
    #Page to allow a game keeper to add locations for the game
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = LocationForm()
        
    return render(request, 'game/locationUpload.html', {'form':form})
