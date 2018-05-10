from django import forms
from worldcup.models import Games
from django.forms import ModelForm

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ('hometeam', 'otherteam', 'homepoints', 'otherpoints',)