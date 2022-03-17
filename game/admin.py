from django.contrib import admin
from .models import activeGame

#Adding active games to the admin page
admin.site.register(activeGame)