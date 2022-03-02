from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('createGame/', views.createGame, name='createGame'),
    path('joinGame/', views.joinGame, name='joinGame'),
]

