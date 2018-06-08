from django import forms
from worldcup.models import Game
from django.forms import ModelForm
from django.contrib.auth.models import User


class BetForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('home', 'away', 'home_goals', 'away_goals',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(LoginForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'placeholder': ''})
        self.fields['password'].widget.attrs['class'] = 'form-control'