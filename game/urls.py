from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('createGame/', views.createGame, name='createGame'),
    path('joinGame/', views.joinGame, name='joinGame'),
    path('game/<int:game_id>/', views.game, name='game'),
]

