from django.shortcuts import render
from worldcup.models import *
from worldcup.forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'index.html', context)


def token(request):
    if request.method == 'POST':
        password = request.POST['password']
        user = authenticate(request, username="user", password=password)
        if user is not None:
            login(request, user)
            all_users = User.objects.all()
            for us in all_users:
                us.save()
            return render(request, 'select_profile.html')
    print("not a fucking post")
    form = LoginForm()
    return render(request, 'token.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        print("logout")
        logout(request)
    if request.method == 'POST':
        print("POSTI")
        username = request.POST['username'].replace(" ", "").replace("&",
                                                                     "").lower()
        print(username)
        user = authenticate(request, username=username, password='salasana')
        if user is not None:
            login(request, user)
            all_users = User.objects.all()
            for us in all_users:
                us.save()
            return render(request, 'home.html')
    print("gETTI")
    return render(request, 'select_profile.html')


def home(request):
    return render(request, 'home.html')


# @login_required(login_url='token')
def select_profile(request):
    profiles = Profile.objects.all()

    return render(request, 'select_profile.html', {'profiles': profiles})
