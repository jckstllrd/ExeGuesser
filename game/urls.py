from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('createGame/', views.createGame, name='createGame'),
    path('joinGame/', views.joinGame, name='joinGame'),
    path('game/<int:game_id>/', views.game, name='game'),
    path('locationUpload/', views.locationUpload, name = 'locationUpload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
