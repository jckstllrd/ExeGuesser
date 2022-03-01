from django.shortcuts import render

# Create your views here.
def index(request):
    context = {} 
    return render(request, 'users/index.html', context)

def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)