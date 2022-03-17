from django.forms import ModelForm
from .models import activeGame


#A form for the creation of games
class GameCreatorForm(ModelForm):
    class Meta:
        model = activeGame
        fields = '__all__'