from random import choices
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

PROFILE_CHOICES = (
    ('user', 'User'),
    ('gamekeeper', 'Game Keeper'),
)


class RegistrationForm(UserCreationForm):
    profile = forms.ChoiceField(choices=PROFILE_CHOICES)

    class Meta:
        model = User
        fields = ('profile', 'username', 'password1', 'password2', )
