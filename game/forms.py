from django.forms import ModelForm
from .models import activeGame

class GameCreatorForm(ModelForm):
    class Meta:
        model = activeGame
        fields = '__all__'