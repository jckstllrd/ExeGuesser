from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'ecm2434/index.html')


"""def login(request):
    #something
    
def register(request):
    #something 

def logout(request):
    #something """