from django.shortcuts import render
from worldcup.models import *
from worldcup.forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'index.html', context)


def login_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        user = authenticate(request, username="user", password=password)
        if user is not None:
            login(request, user)
            all_users = User.objects.all()
            for us in all_users:
                us.save()
            print("TÄÄLLÄ MOI")
            return render(request, 'index.html')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'login.html', context)
