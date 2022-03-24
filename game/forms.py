from django.forms import ModelForm
from .models import activeGame
from .models import locations


#A form for the creation of games
class GameCreatorForm(ModelForm):
    class Meta:
        model = activeGame
        fields = '__all__'
        
#A form for the databse of locations
class LocationForm(ModelForm):
    class Meta:
        model = locations
        fields = ['locationName','locationImage']        
