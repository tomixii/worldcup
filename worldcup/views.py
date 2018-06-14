from django.shortcuts import render
from worldcup.models import *
from worldcup.forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import urllib.request, json


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


def login_user(request):
    if request.user.is_authenticated:
        username = request.POST['username'].replace(" ", "").replace("&", "").lower()
        print(username)
        user = authenticate(request, username=username, password='salasana')
        if user is not None:
            logout(request)
            login(request, user)
            all_users = User.objects.all()
            for us in all_users:
                us.save()


def home(request):
    if request.method == 'POST':
        login_user(request)
    with urllib.request.urlopen('https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json') as url:
        data = json.loads(url.read().decode())
    groups = data['groups']
    teams = data['teams']
    matches = []
    for c, info in groups.items():
        matches.append(info['matches'])
    flat_matches = [item for sublist in matches for item in sublist]

    context = {
        'groups': groups,
        'matches': flat_matches,
        'teams': teams
    }
    print("asdedededeed . ", len(flat_matches))
    return render(request, 'home.html', context)


# @login_required(login_url='token')
def select_profile(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'select_profile.html', context)
