from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'game/home.html', context)

def createGame(request):
    context = {}
    return render(request, 'game/createGame.html', context)

def joinGame(request):
    context = {}
    return render(request, 'game/joinGame.html', context)