from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


# Create your views here.
def index(request):
    context = {} 
    return render(request, 'users/index.html', context)

def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)

def registerPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
            # redirect user to home page
            return redirect('home')
    else:
        form = RegistrationForm()
        

    return render(request, 'users/register.html', {'form': form})